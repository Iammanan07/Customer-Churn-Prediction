# 📊 Customer Churn Prediction App - Abhishek Pandey.

Predict customer churn with up to **98% accuracy** using machine learning, wrapped in a sleek and intuitive web interface powered by **Streamlit**.

![Streamlit App UI](https://i.imgur.com/nv6ZRYI.png) <!-- Replace with your actual image if needed -->

---

## 🚀 Live Demo

👉 [Click here to try the app](https://abhishek-pandey-churn-predictor.streamlit.app)  
_Real-time churn prediction at your fingertips!_

---

## 🔍 Overview

This project leverages a machine learning model trained on telecom customer data to **predict whether a customer will churn or stay**. It provides a user-friendly interface built using **Streamlit**, allowing business users and analysts to make instant predictions based on customer attributes.

💡 Powered by:
- Logistic Regression (chosen after comparing multiple models)
- Streamlit for the frontend
- Joblib for model persistence
- Python’s Pandas & Scikit-learn for data handling and ML

---

## 🧠 Features

✅ Predict churn with a few simple inputs  
✅ Intuitive, responsive web interface  
✅ Lightweight and fast backend  
✅ Model trained and tuned for high accuracy  
✅ Easily deployable on Streamlit Community Cloud  

---

## 📦 Project Structure

📁 churn_deployment/
├── app.py ← Streamlit app file
├── model.pkl ← Trained ML model (joblib format)
├── requirements.txt ← Python dependencies
├── README.md ← This file
└── Optional files (EDA, training scripts, assets)


## 🛠️ Tech Stack

- **Language**: Python 🐍  
- **Machine Learning**: scikit-learn  
- **Data Manipulation**: pandas  
- **Model Persistence**: joblib  
- **UI**: Streamlit  
- **Hosting**: Streamlit Community Cloud  

---

## 🧪 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhishekpandey-dev/customer-churn-predictor.git
   cd customer-churn-predictor Install dependencies

2. pip install -r requirements.txt
3. Run the app
streamlit run app.py
