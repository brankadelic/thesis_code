TEST_PATIENTS_HYPERTENSION = [
    (1,  110, 60,  False, False, "NonElevated",         "Screen_3y"),
    (2,  110, 60,  True,  False, "NonElevated",         "Screen_1y"),
    (11, 120, 70,  False, False, "Elevated",            "Screen_1y"),
    (12, 120, 70,  False, True,  "Elevated",            "Confirm"),
    (13, 120, 70,  True,  False, "Elevated",            "Screen_1y"),
    (14, 120, 70,  True,  True,  "Elevated",            "Confirm"),
    (26, 140, 90,  False, False, "HTN_140_159_90_99",   "Confirm"),
    (31, 118, 92,  False, False, "HTN_140_159_90_99",   "Confirm"),
    (33, 152, 68,  False, False, "HTN_140_159_90_99",   "Confirm"),
    (41, 160, 100, False, False, "HTN_160_179_100_109", "ConfirmPromptly"),
    (44, 165, 90,  False, False, "HTN_160_179_100_109", "ConfirmPromptly"),
    (45, 120, 105, True,  False, "HTN_160_179_100_109", "ConfirmPromptly"),
    (51, 180, 110, False, False, "HTN_ge_180_110",      "EvaluateEmergency"),
    (59, 180, 90,  False, False, "HTN_ge_180_110",      "EvaluateEmergency"),
    (56, 118, 110, True,  False, "HTN_ge_180_110",      "EvaluateEmergency"),
]

TEST_PATIENTS_ASTHMA = [
    (1,  True,  30.0, False, 0.0,  0.0,   0.0,  0.0,  False, "Asthma"),
    (2,  False, 55.0, False, 0.0,  0.0,   0.0,  0.0,  False, "Asthma"),
    (3,  True,  55.0, False, 0.0,  0.0,   0.0,  0.0,  False, "Asthma"),
    (4,  False, 50.0, False, 0.0,  0.0,   0.0,  0.0,  False, "Asthma"),
    (11, False, 30.0, True,  13.0, 210.0, 5.0,  0.0,  False, "Asthma"),
    (12, False, 30.0, True,  5.0,  100.0, 11.0, 0.0,  False, "Asthma"),
    (13, False, 30.0, True,  12.0, 200.0, 5.0,  0.0,  False, "Asthma"),
    (21, False, 30.0, False, 0.0,  0.0,   0.0,  22.0, False, "Asthma"),
    (22, False, 30.0, False, 0.0,  0.0,   0.0,  20.0, False, "Asthma"),
    (31, False, 30.0, True,  5.0,  100.0, 5.0,  0.0,  True,  "Asthma"),
    (32, False, 30.0, False, 0.0,  0.0,   0.0,  10.0, True,  "Asthma"),
    (41, False, 30.0, True,  13.0, 150.0, 5.0,  0.0,  False, "AlternativeDiagnosis"),
    (42, False, 30.0, True,  5.0,  210.0, 5.0,  0.0,  False, "AlternativeDiagnosis"),
    (51, False, 30.0, True,  5.0,  100.0, 5.0,  10.0, False, "AlternativeDiagnosis"),
    (52, False, 30.0, False, 0.0,  0.0,   0.0,  10.0, False, "AlternativeDiagnosis"),
]

TEST_PATIENTS_CURB = [
    (1,  10, 5.0,  16, 120, 80, False, "Group1"),
    (11, 9,  5.0,  16, 120, 80, True,  "Group1"),
    (12, 8,  5.0,  16, 120, 80, True,  "Group2"),
    (13, 10, 7.0,  16, 120, 80, True,  "Group1"),
    (14, 10, 7.1,  16, 120, 80, True,  "Group2"),
    (15, 10, 5.0,  29, 120, 80, True,  "Group1"),
    (16, 10, 5.0,  30, 120, 80, True,  "Group2"),
    (17, 10, 5.0,  16, 120, 61, True,  "Group1"),
    (18, 10, 5.0,  16, 120, 60, True,  "Group2"),
    (19, 10, 5.0,  16, 90,  80, True,  "Group1"),
    (20, 10, 5.0,  16, 89,  80, True,  "Group2"),
    (21, 10, 5.0,  16, 85,  55, True,  "Group2"),
    (22, 8,  5.0,  16, 120, 80, False, "Group1"),
    (31, 8,  8.0,  16, 120, 80, False, "Group2"),
    (32, 8,  8.0,  32, 120, 80, False, "Group3"),
    (41, 5,  10.0, 35, 85,  70, False, "Group3"),
    (42, 3,  12.0, 40, 80,  50, True,  "Group3"),
    (51, 6,  5.0,  18, 130, 75, True,  "Group2"),
    (52, 10, 4.0,  34, 82,  55, False, "Group2"),
    (61, 10, 5.0,  16, 120, 61, True,  "Group1"),
    (62, 10, 5.0,  16, 120, 60, True,  "Group2"),
    (63, 10, 5.0,  16, 120, 59, True,  "Group2"),
    (64, 10, 5.0,  16, 90,  80, True,  "Group1"),
    (65, 10, 5.0,  16, 89,  80, True,  "Group2"),
    (66, 10, 5.0,  16, 91,  80, True,  "Group1"),
    (67, 10, 5.0,  16, 90,  60, True,  "Group2"),
    (68, 10, 5.0,  16, 90,  61, True,  "Group1"),
]

TEST_PATIENTS_DVT = [
    (1,  False, False, False, False, False, False, False, False, False, False, "Negative", "Negative", "ExcludeDVT"),
    (2,  False, False, False, False, False, False, False, False, False, False, "Negative", "Positive", "ExcludeDVT"),
    (3,  False, False, False, False, False, False, False, False, False, False, "Positive", "Negative", "ExcludeDVT"),
    (4,  False, False, False, False, False, False, False, False, False, False, "Positive", "Positive", "TreatAnticoagulation"),
    (11, True,  True,  False, False, False, False, False, False, False, False, "Negative", "Negative", "ExcludeDVT"),
    (12, True,  True,  False, False, False, False, False, False, False, False, "Negative", "Positive", "TreatAnticoagulation"),
    (13, True,  True,  False, False, False, False, False, False, False, False, "Positive", "Positive", "TreatAnticoagulation"),
    (14, True,  True,  False, False, False, False, False, False, False, False, "Positive", "Negative", "RepeatUltrasoundIn1Week"),
    (21, False, False, False, False, False, False, False, False, True,  False, "Positive", "Negative", "ExcludeDVT"),
    (22, True,  False, False, False, False, False, False, False, True,  False, "Positive", "Negative", "RepeatUltrasoundIn1Week"),
    (23, False, True,  False, False, False, False, False, False, True,  False, "Positive", "Negative", "RepeatUltrasoundIn1Week"),
    (24, False, False, True,  False, False, False, False, False, True,  False, "Positive", "Negative", "RepeatUltrasoundIn1Week"),
    (25, False, False, False, True,  False, False, False, False, True,  False, "Positive", "Negative", "RepeatUltrasoundIn1Week"),
    (26, False, False, False, False, True,  False, False, False, True,  False, "Positive", "Negative", "RepeatUltrasoundIn1Week"),
    (27, False, False, False, False, False, True,  False, False, True,  False, "Positive", "Negative", "RepeatUltrasoundIn1Week"),
    (28, False, False, False, False, False, False, True,  False, True,  False, "Positive", "Negative", "RepeatUltrasoundIn1Week"),
    (29, False, False, False, False, False, False, False, True,  True,  False, "Positive", "Negative", "RepeatUltrasoundIn1Week"),
    (31, True,  False, False, False, False, False, False, False, True,  True,  "Positive", "Negative", "ExcludeDVT"),
    (32, False, False, False, False, False, False, False, False, False, True,  "Negative", "Negative", "ExcludeDVT"),
    (41, True,  True,  True,  True,  True,  False, False, False, False, False, "Negative", "Positive", "TreatAnticoagulation"),
]

def patient_to_narrative_hypertension(patient):
    pid, systolic, diastolic, age_ge_40, high_cvd_risk, _, _ = patient
    age_str = "aged 40 or older" if age_ge_40 else "under 40 years of age"
    cvd_str = "has high cardiovascular risk" if high_cvd_risk else "does not have high cardiovascular risk"
    return (f"The patient is {age_str} and presents with a systolic blood pressure "
            f"of {systolic} mmHg and a diastolic blood pressure of {diastolic} mmHg. "
            f"The patient {cvd_str}.")

def patient_to_narrative_asthma(patient):
    pid, eosinophils_high, feno_level, spirometry_available, \
    fev1_increase_percent, fev1_increase_ml, fev1_predicted_increase_percent, \
    pef_variability_percent, bronchial_hyperresponsiveness, _ = patient
    eosino_str = "elevated" if eosinophils_high else "not elevated"
    spiro_str = "is available" if spirometry_available else "is not available"
    bronch_str = "is present" if bronchial_hyperresponsiveness else "is not present"
    return (f"The patient presents with a blood eosinophil count that is {eosino_str} "
            f"and a FeNO level of {feno_level} ppb. Spirometry {spiro_str}. "
            f"FEV1 increase is {fev1_increase_percent}% and {fev1_increase_ml} ml, "
            f"with a predicted FEV1 increase of {fev1_predicted_increase_percent}%. "
            f"PEF variability is {pef_variability_percent}%. "
            f"Bronchial hyperresponsiveness {bronch_str}.")


def patient_to_narrative_dvt(patient):
    pid, active_cancer, paralysis_or_immobilisation, bedridden_or_recent_surgery, localised_tenderness, entire_leg_swelling, calf_swelling_ge_3cm, pittingoedema, collateral_veins, previous_dvt, alternative_diagnosis_likely, ddimer, ultrasound, _ = patient

    def yn(flag):
        return "present" if flag else "absent"

    return (f"Active cancer is {yn(active_cancer)}. Paralysis, paresis, or recent plaster "
            f"immobilization of the lower extremities is {yn(paralysis_or_immobilisation)}. "
            f"Recent bedridden status of more than 3 days or major surgery within the previous "
            f"12 weeks is {yn(bedridden_or_recent_surgery)}. Localized tenderness along the deep "
            f"venous system is {yn(localised_tenderness)}. Swelling of the entire leg is "
            f"{yn(entire_leg_swelling)}. Calf swelling more than 3 cm larger than the asymptomatic "
            f"side is {yn(calf_swelling_ge_3cm)}. Pitting edema confined to the symptomatic leg is "
            f"{yn(pittingoedema)}. Collateral superficial (nonvaricose) veins are "
            f"{yn(collateral_veins)}. A previously documented DVT is {yn(previous_dvt)}. An "
            f"alternative diagnosis at least as likely as DVT is {yn(alternative_diagnosis_likely)}. "
            f"The D-dimer test result is {ddimer}. The compression ultrasound result is {ultrasound}.")


def patinet_to_narrative_curb(patient):
    pid, confusion, urea, resp_rate, systolic, diastolic, age_ge_65, _ = patient
    age_str = "65 years of age or older" if age_ge_65 else "younger than 65 years of age"
    return (f"The patient has an Abbreviated Mental Test Score (AMTS) of {confusion} out of 10. "
            f"Blood urea is {urea} mmol/L. Respiratory rate is {resp_rate} breaths per minute. "
            f"Blood pressure is {systolic}/{diastolic} mmHg. "
            f"The patient is {age_str}.")



def get_patients_and_narrative(DISEASE):
    if DISEASE == "hypertension":
        return TEST_PATIENTS_HYPERTENSION, patient_to_narrative_hypertension, -1
    elif DISEASE == 'asthma':
        return TEST_PATIENTS_ASTHMA, patient_to_narrative_asthma, -1
    elif DISEASE == 'dvt':
        return TEST_PATIENTS_DVT, patient_to_narrative_dvt, -1
    elif DISEASE == 'curb':
         return TEST_PATIENTS_CURB, patinet_to_narrative_curb, -1