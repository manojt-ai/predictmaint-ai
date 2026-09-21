import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="PredictMaint AI",
    page_icon="⚙️",
    layout="centered"
)

st.title("PredictMaint AI")
st.write("Industrial Machine Failure Prediction")

st.subheader("Machine Sensor Inputs")

machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temperature = st.number_input(
    "Air Temperature [K]",
    min_value=0.0,
    value=300.0
)

process_temperature = st.number_input(
    "Process Temperature [K]",
    min_value=0.0,
    value=310.0
)

rotational_speed = st.number_input(
    "Rotational Speed [rpm]",
    min_value=0.0,
    value=1500.0
)

torque = st.number_input(
    "Torque [Nm]",
    min_value=0.0,
    value=45.0
)

tool_wear = st.number_input(
    "Tool Wear [min]",
    min_value=0.0,
    value=100.0
)

if st.button("Predict Failure"):
    model = joblib.load("models/predictmaint_rf.joblib")

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

    if prediction[0] == 1:
        st.error("Machine Failure Risk Detected")
    else:
        st.success("Machine Status: NORMAL")

    st.write(f"Failure Probability: {probability:.2%}")