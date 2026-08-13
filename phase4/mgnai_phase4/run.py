import os
import json
from pathlib import Path
import requests
from dotenv import load_dotenv
from make_patient import get_patients_and_narrative, get_expected_for_conflict

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY is not set.")

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"


DISEASE = "dvt"  # change this per disease for the experiments
# possible diseases: hypertension, asthma, curb, dvt

CONFLICT_TYPES = ["threshold_small", "threshold_large", "action"]
PROMPTS = ["with_guideline"]
GUIDELINES_DIR = Path(f"data/guidelines/{DISEASE}_changes")
GUIDELINE_FILE = f"data/guidelines/{DISEASE}_guideline.txt"
OUTPUT_DIR = Path("outputs") / DISEASE

VALID_DECISIONS = {
    "hypertension": ["Screen_3y", "Screen_1y", "Confirm", "ConfirmPromptly", "EvaluateEmergency"],
    "asthma": ["Asthma", "AlternativeDiagnosis"],
    "dvt": ["ExcludeDVT", "TreatAnticoagulation", "RepeatUltrasoundIn1Week"],
    "curb": ["Group1", "Group2", "Group3"],
}


def parse_decision(raw_output):
    print(f"RAW: {raw_output[:200]}")

    raw_output = raw_output.strip()

    if "```" in raw_output:
        raw_output = raw_output.split("```")[1]
        if raw_output.startswith("json"):
            raw_output = raw_output[4:]
        raw_output = raw_output.strip()

    try:
        parsed = json.loads(raw_output)
        return parsed.get("decision", None)
    except json.JSONDecodeError:
        return None


def call_openrouter(model_config, prompt):
    response = requests.post(
        BASE_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model_config["model_name"],
            "messages": [{"role": "user", "content": prompt}],
            "temperature": model_config.get("temperature", 0),
            "max_tokens": 100,
        },
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


def load_models():
    with open("config/models.json", "r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt(prompt_type, narrative, guideline):
    valid = ", ".join(VALID_DECISIONS[DISEASE])
    template = Path(f"prompts/{prompt_type}.txt").read_text(encoding="utf-8")

    prompt = template.replace("[[PATIENT_DESCRIPTION]]", narrative)
    prompt = prompt.replace("[[VALID_DECISIONS]]", valid)
    prompt = prompt.replace("[[GUIDELINE]]", guideline)

    return prompt


def call_for_patient(patient, narrative_fn, expected, prompt_type, guideline, model_config):
    pid = patient[0]
    narrative = narrative_fn(patient)
    prompt = build_prompt(prompt_type, narrative, guideline)
 
    try:
        response = call_openrouter(model_config, prompt)
        clean_response = parse_decision(response)
        correct = clean_response == expected
 
        if correct:
            status = "ok"
        elif clean_response is None:
            status = "Parse error"
        else:
            status = "wrong"
 
        print(f"  Patient {pid:2d}: {status}  (got={clean_response}, expected={expected})")
 
    except Exception as e:
        clean_response = None
        correct = False
        print(f"  Patient {pid:2d}: ERROR  ({str(e)[:60]})")
 
    return pid, expected, clean_response, correct, narrative
 
 
def run_all():
    models = load_models()
    patients, narrative_fn, _ = get_patients_and_narrative(DISEASE)
 
    all_results = []
 
    for conflict_type in CONFLICT_TYPES:
        guideline_path = GUIDELINES_DIR / f"{DISEASE}_guideline_{conflict_type}.txt"
        if not guideline_path.exists():
            print(f"[SKIP] Guideline not found: {guideline_path}")
            continue
 
        guideline = guideline_path.read_text(encoding="utf-8")
 
        for model_key, model_config in models.items():
            for prompt_type in PROMPTS:
                print(f"\n=== {model_key.upper()} / {conflict_type} / {prompt_type} ===")
                model_results = []
 
                for patient in patients:
                    expected = get_expected_for_conflict(DISEASE, conflict_type, patient)
 
                    pid, expected, clean_response, correct, narrative = call_for_patient(
                        patient, narrative_fn, expected, prompt_type, guideline, model_config
                    )
                    model_results.append({
                        "patient_id": pid,
                        "expected": expected,
                        "decision_of_the_model": clean_response,
                        "correct": correct,
                        "narrative": narrative,
                    })
 
                sat_count = sum(r["correct"] for r in model_results)
                accuracy = round(sat_count / len(patients) * 100, 1)
                print(f"  => Accuracy: {accuracy}%  ({sat_count}/{len(patients)})")
 
                all_results.append({
                    "model": model_key,
                    "prompt": prompt_type,
                    "conflict_type": conflict_type,
                    "accuracy_pct": accuracy,
                    "sat_count": sat_count,
                    "total": len(patients),
                    "patients": model_results,
                })
 
    output_dir = Path("outputs") / "evaluation"
    output_dir.mkdir(parents=True, exist_ok=True)
 
    json_path = output_dir / f"{DISEASE}_phase4_results.json"
    json_path.write_text(json.dumps(all_results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved: {json_path}")
 
    print("\n" + "=" * 70)
    print(f"{'MODEL':<10} {'CONFLICT':<20} {'CORRECT':>9} {'ACC%':>7}")
    print("-" * 70)
    for r in all_results:
        print(f"{r['model']:<10} {r['conflict_type']:<20} "
              f"{r['sat_count']:>4}/{r['total']:<4} "
              f"{r['accuracy_pct']:>6}%")
    print("=" * 70)
 
 
if __name__ == "__main__":
    run_all()