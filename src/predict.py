import joblib
import pandas as pd

model = joblib.load("models/predictmaint_rf.joblib")

sample_machine = pd.DataFrame({
    "Type": ["L"],
    "Air temperature [K]": [300.0],
    "Process temperature [K]": [310.0],
    "Rotational speed [rpm]": [1500],
    "Torque [Nm]": [45.0],
    "Tool wear [min]": [100]
})

prediction = model.predict(sample_machine)
probability = model.predict_proba(sample_machine)[0, 1]

print("Prediction:", prediction[0])
print("Failure probability:", probability)