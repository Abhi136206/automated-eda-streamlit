"""
Customer Churn Prediction - Simple Single-File ML Project
Run: python churn_prediction.py
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# ------------------------------------------------------------
# 1. CREATE DATASET (synthetic, realistic telecom churn data)
# ------------------------------------------------------------
np.random.seed(42)
n = 2000

data = pd.DataFrame({
    "gender": np.random.choice(["Male", "Female"], n),
    "SeniorCitizen": np.random.choice([0, 1], n, p=[0.85, 0.15]),
    "Partner": np.random.choice(["Yes", "No"], n),
    "tenure": np.random.randint(0, 72, n),
    "Contract": np.random.choice(["Month-to-month", "One year", "Two year"], n, p=[0.55, 0.25, 0.20]),
    "MonthlyCharges": np.round(np.random.uniform(20, 120, n), 2),
    "TechSupport": np.random.choice(["Yes", "No"], n),
    "NumSupportCalls": np.random.poisson(1.5, n),
})

# Create churn label using realistic rules + randomness
churn_score = (
    (data["Contract"] == "Month-to-month").astype(int) * 2
    - data["tenure"] / 24
    + data["MonthlyCharges"] / 60
    + data["NumSupportCalls"] * 0.4
    - (data["TechSupport"] == "Yes").astype(int)
    + np.random.normal(0, 1, n)
)
data["Churn"] = np.where(churn_score > churn_score.median(), "Yes", "No")

print("Dataset created:", data.shape)
print(data["Churn"].value_counts())

# ------------------------------------------------------------
# 2. ENCODE CATEGORICAL COLUMNS
# ------------------------------------------------------------
df = data.copy()
encoders = {}
for col in ["gender", "Partner", "Contract", "TechSupport"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df.drop("Churn", axis=1)
y = (df["Churn"] == "Yes").astype(int)

# ------------------------------------------------------------
# 3. TRAIN / TEST SPLIT
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------------------------------------------
# 4. TRAIN MODELS AND COMPARE
# ------------------------------------------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
}

best_model = None
best_f1 = 0
best_name = ""

print("\n--- Model Comparison ---")
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds)
    rec = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    print(f"{name}: Accuracy={acc:.2f}, Precision={prec:.2f}, Recall={rec:.2f}, F1={f1:.2f}")

    if f1 > best_f1:
        best_f1 = f1
        best_model = model
        best_name = name

print(f"\nBest Model: {best_name} (F1 = {best_f1:.2f})")

# ------------------------------------------------------------
# 5. SAVE MODEL
# ------------------------------------------------------------
joblib.dump({"model": best_model, "encoders": encoders, "columns": list(X.columns)}, "churn_model.joblib")
print("Model saved as churn_model.joblib")

# ------------------------------------------------------------
# 6. PREDICT ON A NEW CUSTOMER (example)
# ------------------------------------------------------------
def predict_churn(customer: dict):
    row = pd.DataFrame([customer])
    for col, le in encoders.items():
        row[col] = le.transform(row[col])
    row = row[X.columns]
    prob = best_model.predict_proba(row)[0][1]
    pred = "Yes" if prob >= 0.5 else "No"
    return pred, round(prob, 2)


new_customer = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "No",
    "tenure": 3,
    "Contract": "Month-to-month",
    "MonthlyCharges": 95.0,
    "TechSupport": "No",
    "NumSupportCalls": 4,
}

pred, prob = predict_churn(new_customer)
print(f"\nExample Prediction -> Churn: {pred} (Probability: {prob})")