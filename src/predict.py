import joblib
import pandas as pd

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

model = joblib.load("models/predictmaint_rf.joblib")

machine_type = input("Enter machine type (L/M/H): ").upper()

while machine_type not in ["L", "M", "H"]:
    print("Invalid machine type. Please enter L, M, or H.")
    machine_type = input("Enter machine type (L/M/H): ").upper()
    
air_temperature = get_positive_float("Enter air temperature [K]: ")
process_temperature = get_positive_float("Enter process temperature [K]: ")
rotational_speed = get_positive_float("Enter rotational speed [rpm]: ")
torque = get_positive_float("Enter torque [Nm]: ")
tool_wear = get_positive_float("Enter tool wear [min]: ")

machine = pd.DataFrame({
    "Type": [machine_type],
    "Air temperature [K]": [air_temperature],
    "Process temperature [K]": [process_temperature],
    "Rotational speed [rpm]": [rotational_speed],
    "Torque [Nm]": [torque],
    "Tool wear [min]": [tool_wear]
})

prediction = model.predict(machine)
probability = model.predict_proba(machine)[0, 1]

status = "FAILURE RISK" if prediction[0] == 1 else "NORMAL"

print("\nMachine Status:", status)
print("Failure Probability:", f"{probability:.2%}")