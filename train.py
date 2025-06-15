# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Load the dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df.drop("customerID", axis=1, inplace=True)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.dropna(inplace=True)

# 2. Encode categorical variables
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    if col != "Churn":
        df[col] = le.fit_transform(df[col])
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# 3. Split features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Build a pipeline: scale data + logistic regression
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(solver="saga", max_iter=3000)
)
model.fit(X_train, y_train)

# 5. Save the trained model
joblib.dump(model, "model.pkl")
print("Model training complete! Saved to model.pkl")
