from med_guard import MedGuardBackend

backend = MedGuardBackend(dr_model="gpt-4o-mini")
backend.set_patient_profile(age="40", gender="Male")

while True:
    user_text = input("You (patient): ")
    if user_text.lower() in ("quit", "exit"):
        break

    out = backend.patient_turn(user_text)
    print("\nDoctor:", out["doctor_reply"], "\n")

    if out["dx_ready"]:
        print("Final diagnosis:", out["final_diagnosis"])
        break
