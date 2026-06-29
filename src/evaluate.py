import os
import json
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/processed/data.csv")

X = df[["feature1", "feature2", "cholesterol"]]
y = df["target"]

model = joblib.load("models/model.pkl")

preds = model.predict(X)

accuracy = accuracy_score(y, preds)
report = classification_report(y, preds, output_dict=True)

print("Accuracy:", accuracy)

os.makedirs("metrics", exist_ok=True)

metrics = {
    "accuracy": accuracy,
    "classification_report": report
}

with open("metrics/metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("Evaluation done")