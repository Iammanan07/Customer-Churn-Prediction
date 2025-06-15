<h1 align="center" style="color:#6A0DAD;">📈 Customer Churn Prediction App</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Accuracy-98%25-success" alt="accuracy" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-blue" alt="ML model" />
  <img src="https://img.shields.io/badge/Deployed%20With-Streamlit-%23FF4B4B" alt="Deployment" />
  <img src="https://img.shields.io/badge/Python-3.9-green" alt="Python" />
</p>

---

## 🚀 Overview

This is a full-stack **Customer Churn Prediction App** that leverages real-world telecom customer data to **predict churn behavior**. The model allows businesses to identify customers likely to leave and take proactive steps to retain them.

✨ **Live Demo**: [https://customerchurnanalyzer.streamlit.app/]  
📦 **GitHub Repo**:

---

## 🧠 Tech Stack

- **Python** 🐍  
- **Pandas, NumPy, Matplotlib, Seaborn** 📊  
- **Scikit-Learn, Joblib** 🔍  
- **Streamlit** (for the UI) 🌐  
- **Git & GitHub** for version control 🛠

---

## 🔍 Features

✅ Interactive Streamlit UI  
✅ Clean and responsive layout  
✅ Takes real-time input from users  
✅ Predicts if a customer is likely to churn or not  
✅ 98% accuracy on test data  
✅ Model serialized using `joblib`

---
You can check out this out Live - https://customerchurnanalyzer.streamlit.app/

## 📁 Project Structure

```bash
Customer-Churn-Prediction/
│
├── app.py                  # Streamlit App
├── model.pkl               # Trained Logistic Regression Model
├── requirements.txt        # All dependencies
├── churn_notebook.ipynb    # EDA and model building notebook
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset
├── README.md               # You're reading it ;)

📊 Input Fields
1.Gender, Senior Citizen, Partner, Dependents

2.Tenure, Phone Service, Internet Service

3.Online Security, Backup, Protection, Tech Support

4.Contract type, Paperless Billing

5.Payment Method, Monthly & Total Charges
