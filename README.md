<div align="center">

# ⚙️ PredictMaint AI

### Industrial Predictive Maintenance System

Predict machine failure risk using industrial sensor measurements and machine learning.

<br>

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Joblib](https://img.shields.io/badge/Joblib-Model%20Persistence-green)
![GitHub](https://img.shields.io/badge/Git-GitHub-black?logo=github)

</div>

---

## 🚀 Overview

**PredictMaint AI** is an end-to-end machine learning project designed to predict industrial machine failure using sensor measurements.

The project follows a complete machine learning workflow:

**Data → EDA → Preprocessing → Model Development → Evaluation → Model Saving → Prediction → Streamlit Application**

The system takes machine sensor measurements such as:

- 🌡️ Air Temperature
- 🌡️ Process Temperature
- ⚙️ Rotational Speed
- 🔩 Torque
- 🛠️ Tool Wear
- 🏭 Machine Type

and predicts whether the machine is at risk of failure.

---

## 🎯 Project Objectives

- Understand industrial machine failure patterns
- Perform exploratory data analysis
- Handle an imbalanced classification problem
- Compare different machine learning approaches
- Evaluate models using appropriate classification metrics
- Build a reusable ML pipeline
- Save and load the trained model
- Create an interactive prediction application

---

## 🔍 Key Features

| Feature | Description |
|---|---|
| 📊 Exploratory Data Analysis | Analyze sensor patterns and machine failures |
| 🧹 Data Preprocessing | Prepare categorical and numerical features |
| 🤖 Logistic Regression | Baseline classification model |
| 🌲 Random Forest | Final classification model |
| 📈 Model Evaluation | Precision, Recall, F1 and Average Precision |
| 🎚️ Threshold Analysis | Analyze probability thresholds |
| 💾 Model Persistence | Save ML pipeline using Joblib |
| 🔎 Prediction Script | Standalone command-line prediction |
| 🖥️ Streamlit Dashboard | Interactive web application |
| ✅ Input Validation | Validate user-provided sensor values |
| 📋 Sensor Summary | Display input measurements |
| ⚠️ Failure Interpretation | Explain normal and failure-risk predictions |

---

## 🧠 Machine Learning Approach

### 1. Dataset

The project uses the **AI4I 2020 Predictive Maintenance Dataset** from the UCI Machine Learning Repository.

Dataset size:

**10,000 machine records**

The target variable is:

```text
Machine failure

2. Exploratory Data Analysis
The analysis included:
- Dataset structure
- Missing value analysis
- Duplicate detection
- Target distribution
- Failure rate by machine type
- Sensor statistics
- Feature correlations
- Sensor distribution analysis
The target variable is highly imbalanced, making metrics such as Precision, Recall and F1-score important for evaluation.
3. Preprocessing
The model uses:
- One-hot encoding for machine type
- Numerical sensor features
- Stratified train-test splitting
- Integrated preprocessing using Scikit-learn Pipeline
4. Model Development
Two approaches were explored:
Logistic Regression
Used as the baseline classification model.
Random Forest
A Random Forest classifier was developed with:
n_estimators = 200
class_weight = balanced
random_state = 42
The preprocessing and model were integrated into a single Scikit-learn pipeline.
📊 Model Performance
Random Forest
Metric	Score
Precision	0.71
Recall	0.66
F1 Score	0.69
Average Precision	0.762


The model was evaluated on a held-out test set.
Why these metrics?
Because machine failure is an imbalanced classification problem, accuracy alone does not provide enough information.
Therefore, the project focuses on:
- Precision — How many predicted failures were actually failures
- Recall — How many actual failures were detected
- F1 Score — Balance between precision and recall
- Average Precision — Performance across probability thresholds
🎚️ Probability Threshold Analysis
The Random Forest model produces a failure probability for each machine.
Different thresholds were evaluated to understand the trade-off between precision and recall.
Threshold	Precision	Recall	F1
0.20	0.39	0.88	0.54
0.30	0.51	0.84	0.64
0.40	0.61	0.75	0.67
0.50	0.71	0.66	0.69
0.60	0.85	0.57	0.68


The application currently uses a 0.50 operating threshold.
🖥️ Streamlit Application
The project includes an interactive Streamlit dashboard where users can enter machine sensor measurements.
Dashboard capabilities
- Select machine type
- Enter sensor measurements
- Predict machine failure
- Display estimated failure probability
- Show prediction interpretation
- Display machine sensor summary
Example predictions
Normal condition
Machine Status: NORMAL
Failure Probability: 0.00%
Failure-risk condition
Machine Status: FAILURE RISK
Failure Probability: 81.00%
The displayed probability represents the model's estimated probability for the provided sensor measurements and should not be treated as a guarantee of actual machine failure.

🏗️ Project Structure
predictmaint-ai/
│
├── app/
│   └── app.py
│
├── data/
│   └── ai4i2020.csv
│
├── models/
│   └── predictmaint_rf.joblib
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_preprocessing.ipynb
│
├── src/
│   └── predict.py
│
├── .gitignore
├── README.md
└── requirements.txt
⚙️ Run Locally
1. Clone the repository
git clone https://github.com/manojt-ai/predictmaint-ai.git
cd predictmaint-ai
2. Create virtual environment
python -m venv .venv
3. Activate environment
Windows
.venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run the Streamlit application
python -m streamlit run app/app.py
The application will open at:
http://localhost:8501
🧪 Command-Line Prediction
The project also includes a standalone prediction script:
python src/predict.py
The script accepts machine sensor values and returns:
- Machine status
- Failure probability
🛠️ Tech Stack
Programming
- Python
Data Analysis
- Pandas
- NumPy
- Matplotlib
- Seaborn
Machine Learning
- Scikit-learn
- Logistic Regression
- Random Forest
Model Persistence
- Joblib
Application
- Streamlit
Version Control
- Git
- GitHub
📚 Dataset
This project uses the:
AI4I 2020 Predictive Maintenance Dataset
provided through the UCI Machine Learning Repository.
The dataset contains industrial machine sensor measurements and machine failure information.
🎓 What I Learned
This project helped me understand the complete machine learning workflow:
Raw Dataset
     ↓
Exploratory Data Analysis
     ↓
Data Preprocessing
     ↓
Baseline Model
     ↓
Random Forest
     ↓
Model Evaluation
     ↓
Threshold Analysis
     ↓
Model Persistence
     ↓
Prediction Script
     ↓
Streamlit Application
More importantly, it helped me move from learning individual ML concepts to building a complete working ML application.
👨‍💻 Author
Manojkumar T
Final-Year B.Tech CSBS Student
Aspiring AI/ML Engineer
🔗 GitHub:
https://github.com/manojt-ai
🔗 LinkedIn:
https://www.linkedin.com/in/manojkumar-t-aiml/
