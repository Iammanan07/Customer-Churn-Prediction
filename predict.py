import joblib
import pandas as pd

def predict_churn(input_data):
    # Load trained model
    model = joblib.load("model.pkl")
    
    # Convert input to DataFrame (must match training format)
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    prediction = model.predict(input_df)
    
    return prediction[0]  # Return 0 or 1

# -------------------------------
# Manual test section
# -------------------------------
if __name__ == "__main__":
    # Sample input: must match model's expected features (same column names, order doesn't matter)
    sample_input = {
        "gender": 1,
        "SeniorCitizen": 0,
        "Partner": 1,
        "Dependents": 0,
        "tenure": 24,
        "PhoneService": 1,
        "MultipleLines": 0,
        "InternetService": 1,
        "OnlineSecurity": 1,
        "OnlineBackup": 0,
        "DeviceProtection": 1,
        "TechSupport": 1,
        "StreamingTV": 0,
        "StreamingMovies": 1,
        "Contract": 1,
        "PaperlessBilling": 1,
        "PaymentMethod": 2,
        "MonthlyCharges": 69.45,
        "TotalCharges": 1550.35
    }

    result = predict_churn(sample_input)
    print("Prediction result:", "Churn" if result == 1 else "No Churn")
