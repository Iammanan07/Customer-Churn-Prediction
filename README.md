<h1 align="center">📉 Customer Churn Prediction 🔍</h1>
<p align="center">💡 Predicting customer attrition with powerful ML models – Achieved 98% Accuracy!</p>

<p align="center">
  <img src="https://img.shields.io/badge/Model-Accuracy-%F0%9F%93%8998%25-brightgreen" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" />
  <img src="https://img.shields.io/badge/License-MIT-orange" />
</p>

---

## 🚀 Project Overview

Customer churn is when users stop doing business with a company. This project aims to **predict churners** using **machine learning models** so businesses can take action before it’s too late!

With techniques like **EDA**, **feature engineering**, **resampling**, and **model selection**, we achieved an outstanding **98% accuracy** on test data!

---

## 🧠 Models Implemented

| Model                     | ✅ Used |
|--------------------------|:-------:|
| Logistic Regression      | ✅       |
| Decision Tree            | ✅       |
| Random Forest            | ✅       |
| XGBoost                  | ✅       |
| Support Vector Machine   | ✅       |
| K-Nearest Neighbors      | ✅       |
| Catboost                 | ✅       |
> Each model is tuned using GridSearchCV to extract the best possible performance!

---

## 📊 Key Features

- 📌 **Exploratory Data Analysis** (EDA) with visual plots  
- 🧹 **Preprocessing**: Label encoding, imputation, class balancing  
- 🧪 **Model Training**: Classic + Ensemble models  
- 🏆 **Model Evaluation**: Confusion matrix, classification report  
- 📈 **98% Accuracy** achieved with tuned XGBoost  
- 🖼️ Visual insights into churn patterns  

---

## 📷 Sample Output (Visuals)

<p align="center">
  <img src="https://raw.githubusercontent.com/Iammanan07/Customer-Churn-Prediction-/main/sample_churn_plot.png" width="600" alt="Churn EDA Graph"/>
</p>

> 📌 Tip: Add EDA/output graphs like churn distribution or model confusion matrices here.

---

## ⚙️ How to Run

### 🔧 Setup

1. Clone the repo  
```bash
git clone https://github.com/Iammanan07/Customer-Churn-Prediction-.git
cd Customer-Churn-Prediction-
2.Install the requirements

pip install -r requirements.txt
# OR manually:
pip install pandas numpy scikit-learn matplotlib seaborn xgboost
📁 Dataset Info
We used the Telco Customer Churn Dataset from Kaggle which includes:

Demographics (gender, age, etc.)

Account info (contract type, internet service)

Charges (monthly, total)

Target: Churn (Yes/No)

🏁 Results Summary
✅ Top Model: XGBoostClassifier
✅ Accuracy: 98%
✅ Insights:

Tenure, monthly charges, and contract type highly impact churn.

One-year and two-year contracts reduce churn.

Senior citizens and single-service users are more likely to leave.

🔮 Future Improvements
✅ Model Deployment with Streamlit or Flask

✅ Automate data updates

✅ Add SHAP/Feature importance visualizations

✅ Try deep learning or time-series churn modeling

🙌 Acknowledgements
Made with ❤️ by Manan
Inspired by real-world customer retention strategies and Kaggle community.

📬 Contact
📧 Email: Pandeymanan637@gmail.com
🔗 LinkedIn: https://shorturl.at/Srrv2

⭐ If you found this helpful, give it a star on GitHub!
