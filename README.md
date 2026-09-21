<div align="center">

# ⚙️ PredictMaint AI

### Industrial Predictive Maintenance System

**An end-to-end Machine Learning project for predicting industrial machine failure risk using sensor measurements.**

<br>

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/manojt-ai/predictmaint-ai)

<br>

![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)
![Domain](https://img.shields.io/badge/Domain-Predictive%20Maintenance-orange?style=flat-square)
![Project](https://img.shields.io/badge/Type-Machine%20Learning-blueviolet?style=flat-square)

</div>

---

## 🚀 Overview

**PredictMaint AI** is my first end-to-end Machine Learning project, built to understand how predictive maintenance can be applied to industrial machines.

The system uses machine sensor measurements such as:

- 🌡️ Air Temperature
- 🌡️ Process Temperature
- ⚙️ Rotational Speed
- 🔩 Torque
- 🛠️ Tool Wear
- 🏭 Machine Type

to estimate whether a machine is at risk of failure.

The project covers the complete Machine Learning workflow:

**Data → EDA → Preprocessing → Model Development → Evaluation → Model Saving → Prediction → Streamlit Application**

---

## 🎯 Project Goal

> **Use machine sensor measurements to estimate industrial machine failure risk using Machine Learning.**

The main goal was not only to train a model, but to understand how a Machine Learning model can be taken from a dataset and converted into a usable application.

---

# 🧠 Machine Learning Workflow

<div align="center">

**📂 Dataset**

⬇️

**🔍 Exploratory Data Analysis**

⬇️

**🧹 Data Preprocessing**

⬇️

**🤖 Model Development**

⬇️

**📊 Model Evaluation**

⬇️

**🎚️ Probability & Threshold Analysis**

⬇️

**💾 Model Persistence**

⬇️

**🖥️ Streamlit Application**

⬇️

**⚙️ Machine Failure Prediction**

</div>

---

# 🔍 What I Built

| Component | Implementation |
|---|---|
| 📊 Data Analysis | Exploratory Data Analysis and failure pattern analysis |
| 🧹 Preprocessing | Categorical encoding and feature preparation |
| 📈 Baseline Model | Logistic Regression |
| 🌲 Final Model | Random Forest Classifier |
| ⚖️ Imbalanced Data | Class-weighted model training |
| 🎯 Evaluation | Precision, Recall, F1-score and Average Precision |
| 🎚️ Threshold Analysis | Failure probability threshold evaluation |
| 💾 Model Saving | Joblib |
| 🖥️ Web Application | Streamlit |
| ✅ Input Validation | Machine type and sensor input validation |
| 📋 Sensor Summary | Displays machine measurements used for prediction |
| ⚠️ Prediction Interpretation | Normal and failure-risk prediction messages |

---

# 📊 Dataset

The project uses the **AI4I 2020 Predictive Maintenance Dataset** from the **UCI Machine Learning Repository**.

### Dataset Overview

| Property | Value |
|---|---:|
| Total Records | **10,000** |
| Normal Cases | **9,661** |
| Failure Cases | **339** |
| Target | **Machine Failure** |
| Machine Types | **L / M / H** |

The target variable is highly imbalanced, with machine failures representing a small portion of the dataset.

Because of this imbalance, the project focuses on metrics beyond accuracy.

---

# 🔎 Exploratory Data Analysis

The EDA phase included:

- Dataset structure analysis
- Missing value analysis
- Duplicate detection
- Target distribution
- Failure rate by machine type
- Sensor statistics
- Feature correlation analysis
- Sensor distribution analysis

### Important observations

The analysis showed that some sensor measurements had stronger relationships with machine failure than others.

The model also showed that **Torque, Rotational Speed, and Tool Wear** were important features for the Random Forest model.

---

# 🧹 Data Preprocessing

The following features were used for the predictive model:

```text
Type
Air temperature [K]
Process temperature [K]
Rotational speed [rpm]
Torque [Nm]
Tool wear [min]
```

Identifier columns such as `UDI` and `Product ID` were excluded.

Failure-type indicator columns were excluded from the initial predictive model to avoid relying on information that could directly represent failure outcomes.

### Train-Test Split

The dataset was divided using:

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

This resulted in:

- Training samples: **8,000**
- Testing samples: **2,000**

Stratification was used to preserve the class distribution between training and testing data.

---

# 🤖 Machine Learning Models

## 1️⃣ Logistic Regression

Logistic Regression was implemented as the baseline classification model.

This provided a reference point for evaluating a more flexible tree-based model.

---

## 2️⃣ Balanced Logistic Regression

A class-weighted Logistic Regression model was also evaluated to understand how class imbalance affects recall and precision.

---

## 3️⃣ Random Forest

The final model uses a Random Forest classifier:

```text
n_estimators = 200
class_weight = balanced
random_state = 42
```

The preprocessing and Random Forest model were integrated into a single **Scikit-learn Pipeline**.

This allows the complete preprocessing and prediction workflow to be saved and reused.

---

# 📈 Model Performance

## 🌲 Random Forest Results

| Metric | Score |
|:---:|---:|
| 🎯 Precision | **0.71** |
| 🔎 Recall | **0.66** |
| ⚖️ F1 Score | **0.69** |
| 📊 Average Precision | **0.762** |

The model was evaluated on a held-out test set.

### Why these metrics?

Because machine failure is an imbalanced classification problem, accuracy alone does not provide enough information.

Therefore, this project focuses on:

**Precision**  
How many predicted failures were actually failures.

**Recall**  
How many actual failures were detected.

**F1 Score**  
The balance between precision and recall.

**Average Precision**  
Model performance across different probability thresholds.

---

# 🎚️ Probability Threshold Analysis

The Random Forest model generates a probability of machine failure.

Different thresholds were evaluated to understand the trade-off between precision and recall.

| Threshold | Precision | Recall | F1 Score |
|:---:|---:|---:|---:|
| **0.20** | 0.39 | 0.88 | 0.54 |
| **0.30** | 0.51 | 0.84 | 0.64 |
| **0.40** | 0.61 | 0.75 | 0.67 |
| **0.50** | **0.71** | **0.66** | **0.69** |
| **0.60** | 0.85 | 0.57 | 0.68 |

The application currently uses a **0.50 operating threshold**.

> The appropriate threshold can depend on the operational cost of missed failures versus false alarms.

---

# 🖥️ Streamlit Application

PredictMaint AI includes an interactive Streamlit dashboard.

### Dashboard capabilities

- 🏭 Select machine type
- 🌡️ Enter sensor measurements
- 🔍 Run machine failure prediction
- 📊 Display estimated failure probability
- ⚠️ Display failure-risk interpretation
- 📋 Display machine sensor summary

### Prediction Flow

```text
Select Machine Type
        ↓
Enter Sensor Measurements
        ↓
Run Prediction
        ↓
Machine Status
        ↓
Failure Probability
        ↓
Sensor Summary
```

---

# 📋 Application Inputs

| Input | Description |
|---|---|
| 🏭 Machine Type | L / M / H |
| 🌡️ Air Temperature | Air temperature in Kelvin |
| 🌡️ Process Temperature | Process temperature in Kelvin |
| ⚙️ Rotational Speed | Machine speed in RPM |
| 🔩 Torque | Machine torque in Nm |
| 🛠️ Tool Wear | Tool wear in minutes |

---

# ✅ Example: Normal Prediction

Example input:

```text
Machine Type        : L
Air Temperature     : 300 K
Process Temperature : 310 K
Rotational Speed    : 1500 RPM
Torque              : 45 Nm
Tool Wear           : 100 min
```

### Result

```text
MACHINE STATUS: NORMAL
Failure Probability: 0.00%
```

---

# ⚠️ Example: Failure-Risk Prediction

Example input:

```text
Machine Type        : L
Air Temperature     : 300 K
Process Temperature : 310 K
Rotational Speed    : 1400 RPM
Torque              : 70 Nm
Tool Wear           : 200 min
```

### Result

```text
MACHINE FAILURE RISK
Failure Probability: 81.00%
```

> The displayed probability represents the model's estimated probability for the provided sensor measurements. It should not be treated as a guarantee of actual machine failure.

---

# 🏗️ Project Structure

```text
predictmaint-ai/
│
├── 📁 app/
│   └── app.py
│
├── 📁 data/
│   └── ai4i2020.csv
│
├── 📁 models/
│   └── predictmaint_rf.joblib
│
├── 📁 notebooks/
│   ├── 01_eda.ipynb
│   └── 02_preprocessing.ipynb
│
├── 📁 src/
│   └── predict.py
│
├── 📄 .gitignore
├── 📄 README.md
└── 📄 requirements.txt
```

---

# 🧪 Notebooks

## `01_eda.ipynb`

Contains:

- Dataset exploration
- Missing-value analysis
- Duplicate analysis
- Target distribution
- Failure rate analysis
- Sensor statistics
- Correlation analysis
- Visualizations

## `02_preprocessing.ipynb`

Contains:

- Feature preparation
- Train-test split
- Preprocessing pipeline
- Logistic Regression
- Balanced Logistic Regression
- Random Forest
- Model evaluation
- Probability analysis
- Threshold analysis
- Feature importance
- Model saving

---

# 💾 Model Persistence

The trained model is saved as:

```text
models/predictmaint_rf.joblib
```

The saved object contains the complete Scikit-learn pipeline, including preprocessing and the Random Forest classifier.

This allows the same preprocessing and model logic to be reused during inference.

---

# 🧪 Command-Line Prediction

A standalone prediction script is included in:

```text
src/predict.py
```

Run it using:

```bash
python src/predict.py
```

The script accepts:

- Machine Type
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

and returns:

```text
Machine Status
Failure Probability
```

Input validation is included for machine type and numerical sensor values.

---

# 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| 💻 Programming | Python |
| 📊 Data Analysis | Pandas, NumPy |
| 📈 Visualization | Matplotlib, Seaborn |
| 🤖 Machine Learning | Scikit-learn |
| 🌲 Classification | Random Forest |
| 📉 Baseline | Logistic Regression |
| 💾 Model Persistence | Joblib |
| 🖥️ Application | Streamlit |
| 🔄 Version Control | Git, GitHub |

---

# ⚙️ Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/manojt-ai/predictmaint-ai.git
```

```bash
cd predictmaint-ai
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

## 3. Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the Streamlit application

```bash
python -m streamlit run app/app.py
```

The application will open at:

```text
http://localhost:8501
```

---

# 🔄 End-to-End Architecture

```text
┌─────────────────────────────┐
│     AI4I 2020 Dataset       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Exploratory Data Analysis   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Data Preprocessing      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Logistic Regression      │
│         Baseline            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Random Forest          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Model Evaluation        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Probability & Threshold     │
│         Analysis            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Joblib Pipeline        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Streamlit Dashboard     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Machine Failure Prediction  │
└─────────────────────────────┘
```

---

# 🎓 What I Learned

Building PredictMaint AI helped me understand how different parts of a Machine Learning project connect together.

### Key learning areas

- Exploratory Data Analysis
- Feature selection
- Data preprocessing
- Classification algorithms
- Imbalanced classification
- Precision vs Recall
- F1-score
- Probability prediction
- Threshold analysis
- Feature importance
- Scikit-learn Pipelines
- Model persistence
- Input validation
- Streamlit application development
- Git and GitHub workflow

Most importantly, this project helped me move from **learning individual ML concepts to building a complete working ML application.**

---

# 📚 Dataset Source

**AI4I 2020 Predictive Maintenance Dataset**

UCI Machine Learning Repository

The dataset contains synthetic industrial machine measurements designed for predictive maintenance research and experimentation.

---

# 🔮 Future Improvements

Possible future extensions include:

- 🔍 Explainable AI
- 📊 Advanced monitoring dashboard
- 🚨 Anomaly detection
- ⏱️ Remaining Useful Life estimation
- ☁️ Cloud deployment
- 📡 Real-time sensor integration
- 📈 Model monitoring

These are potential future directions and are **not part of the current implementation**.

---

# ⚠️ Disclaimer

PredictMaint AI is an educational and portfolio Machine Learning project.

The predicted probability represents the model's estimated probability based on the provided sensor measurements.

It should **not** be treated as a guarantee of actual machine failure or as a substitute for professional industrial monitoring and safety systems.

---

# 👨‍💻 Author

<div align="center">

## Manojkumar T

**Final-Year B.Tech CSBS Student | Aspiring AI/ML Engineer**

<br>

[![GitHub](https://img.shields.io/badge/GitHub-manojt--ai-181717?style=for-the-badge&logo=github)](https://github.com/manojt-ai)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Manojkumar%20T-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/manojt-ai/)

</div>

---

<div align="center">

### ⚙️ PredictMaint AI

**From sensor data to machine failure prediction.**

<br>

⭐ If you found this project interesting, consider giving the repository a star!

</div>
