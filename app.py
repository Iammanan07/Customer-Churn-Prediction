# NOTE: This code requires Streamlit and joblib to be installed.
# Install with: pip install streamlit joblib pandas pillow

try:
    import streamlit as st
    import joblib
    import pandas as pd
    from PIL import Image
except ModuleNotFoundError as e:
    print("Required module missing: ", e)
    print("Please install it using pip before running this script.")
    exit()

# Load the model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    st.error("🔴 Model file 'model.pkl' not found. Please make sure it is in the same directory as this script.")
    st.stop()

# Set page config
st.set_page_config(page_title="Customer Churn Predictor", page_icon="📈", layout="wide")

# Custom banner or header
st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #6A0DAD; font-size: 3.5em;">📊 Customer Churn Prediction App</h1>
        <p style="font-size: 1.2em;">Predict whether a customer will churn based on their account data</p>
        <hr>
    </div>
""", unsafe_allow_html=True)

# Input layout
with st.form("churn_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        senior = st.selectbox("Senior Citizen", ["No", "Yes"])
        partner = st.selectbox("Has Partner", ["No", "Yes"])
        dependents = st.selectbox("Has Dependents", ["No", "Yes"])
        tenure = st.slider("Tenure (Months)", 0, 72, 24)
        phone_service = st.selectbox("Phone Service", ["No", "Yes"])

    with col2:
        multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        online_security = st.selectbox("Online Security", ["No", "Yes"])
        online_backup = st.selectbox("Online Backup", ["No", "Yes"])
        device_protection = st.selectbox("Device Protection", ["No", "Yes"])
        tech_support = st.selectbox("Tech Support", ["No", "Yes"])

    with col3:
        streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"])
        streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"])
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        paperless = st.selectbox("Paperless Billing", ["No", "Yes"])
        payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
        monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
        total_charges = st.number_input("Total Charges", 0.0, 10000.0, 1500.0)

    submitted = st.form_submit_button("🔮 Predict")

# Map input to model format
if submitted:
    input_dict = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if phone_service == "Yes" else 0,
        "MultipleLines": 1 if multiple_lines == "Yes" else 0,
        "InternetService": {"DSL": 0, "Fiber optic": 1, "No": 2}[internet_service],
        "OnlineSecurity": 1 if online_security == "Yes" else 0,
        "OnlineBackup": 1 if online_backup == "Yes" else 0,
        "DeviceProtection": 1 if device_protection == "Yes" else 0,
        "TechSupport": 1 if tech_support == "Yes" else 0,
        "StreamingTV": 1 if streaming_tv == "Yes" else 0,
        "StreamingMovies": 1 if streaming_movies == "Yes" else 0,
        "Contract": {"Month-to-month": 0, "One year": 1, "Two year": 2}[contract],
        "PaperlessBilling": 1 if paperless == "Yes" else 0,
        "PaymentMethod": {"Electronic check": 0, "Mailed check": 1, "Bank transfer": 2, "Credit card": 3}[payment_method],
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]

    st.markdown("""
        <hr>
        <h2 style="text-align: center; color: #333;">🎯 Prediction Result:</h2>
    """, unsafe_allow_html=True)

    if prediction == 1:
        st.error("❌ The customer is likely to CHURN.", icon="⚠️")
    else:
        st.success("✅ The customer is likely to STAY.", icon="👍")
