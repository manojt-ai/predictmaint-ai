# PredictMaint AI

An end-to-end machine learning system for predicting industrial machine failure using sensor measurements.

## Overview

PredictMaint AI uses machine sensor data to estimate the probability of machine failure and provides an interactive Streamlit dashboard for prediction.

## Features

- Exploratory Data Analysis
- Data preprocessing
- Logistic Regression baseline
- Balanced Logistic Regression
- Random Forest classification
- Precision-Recall analysis
- Probability threshold analysis
- Saved ML pipeline using Joblib
- Interactive prediction script
- Input validation
- Professional Streamlit dashboard
- Failure probability visualization
- Machine sensor summary
- Prediction interpretation

## Machine Inputs

- Machine Type
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

## Model

The final baseline model is a Random Forest classifier with preprocessing integrated into a Scikit-learn Pipeline.

Validation results on the test set:

| Metric | Score |
|---|---:|
| Precision | 0.71 |
| Recall | 0.66 |
| F1 Score | 0.69 |
| Average Precision | 0.762 |

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

## Project Structure

```text
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
├── requirements.txt
├── .gitignore
└── README.md