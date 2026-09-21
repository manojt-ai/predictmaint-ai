import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="PredictMaint AI",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ PredictMaint AI")
st.subheader("Industrial Predictive Maintenance System")
st.write("Predict machine failure risk using machine sensor measurements.")

st.divider()

st.subheader("Machine Sensor Inputs")

col1, col2 = st.columns(2)

with col1:
    machine_type = st.selectbox(
        "Machine Type",
        ["L", "M", "H"]
    )

    air_temperature = st.number_input(
        "Air Temperature [K]",
        min_value=0.0,
        value=300.0
    )

    rotational_speed = st.number_input(
        "Rotational Speed [rpm]",
        min_value=0.0,
        value=1500.0
    )

with col2:
    process_temperature = st.number_input(
        "Process Temperature [K]",
        min_value=0.0,
        value=310.0
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

st.divider()

if st.button("🔍 Predict Machine Failure", use_container_width=True):
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

    st.divider()
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ MACHINE FAILURE RISK")

        st.metric(
            "Failure Probability",
            f"{probability:.2%}"
        )

        st.progress(probability)

        st.warning(
            "The model detected an elevated risk of machine failure. "
            "Consider inspecting the machine and its operating conditions."
        )

    else:
        st.success("✅ MACHINE STATUS: NORMAL")

        st.metric(
            "Failure Probability",
            f"{probability:.2%}"
        )

        st.progress(probability)

        st.info(
            "The model did not detect a failure risk for the provided "
            "sensor measurements."
        )

    st.divider()
    st.subheader("📊 Machine Sensor Summary")

    summary = pd.DataFrame({
        "Parameter": [
            "Machine Type",
            "Air Temperature [K]",
            "Process Temperature [K]",
            "Rotational Speed [rpm]",
            "Torque [Nm]",
            "Tool Wear [min]"
        ],
        "Value": [
            machine_type,
            air_temperature,
            process_temperature,
            rotational_speed,
            torque,
            tool_wear
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Failure probability represents the model's estimated probability "
        "for the provided sensor measurements."
    )

st.divider()

st.caption(
    "PredictMaint AI • Industrial Predictive Maintenance"
)