symptom(flu).
symptom(yellowish_eyes_and_skin).
symptom(dark_color_urine).
symptom(pale_bowel_movement).
symptom(fatigue).
symptom(vomitting).
symptom(fever).
symptom(pain_in_joints).
symptom(weakness).
symptom(stomach_pain).

disease(hemochromatosis) :-
    symptom(stomach_pain),
    symptom(pain_in_joints),
    symptom(weakness),
    symptom(dark_color_urine),
    symptom(yellowish_eyes_and_skin).

disease(hepatitis_c) :-
    not(disease(hemochromatosis)),
    symptom(pain_in_joints),
    symptom(fever),
    symptom(fatigue),
    symptom(vomitting),
    symptom(pale_bowel_movement).

disease(hepatitis_b) :-
    not(disease(hemochromatosis)),
    not(disease(hepatitis_c)),
    symptom(pale_bowel_movement),
    symptom(dark_color_urine),
    symptom(yellowish_eyes_and_skin).

disease(hepatitis_a) :-
    not(disease(hemochromatosis)),
    not(disease(hepatitis_c)),
    not(disease(hepatitis_b)),
    symptom(flu),
    symptom(yellowish_eyes_and_skin).

disease(jaundice) :-
    not(disease(hemochromatosis)),
    not(disease(hepatitis_c)),
    not(disease(hepatitis_b)),























