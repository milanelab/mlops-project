import os
import json
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, RocCurveDisplay
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/data.csv")

X = df[["feature1", "feature2", "cholesterol"]]
y = df["target"]

model = joblib.load("models/model.pkl")

preds = model.predict(X)

# Metrics
accuracy = accuracy_score(y, preds)
report = classification_report(y, preds, output_dict=True)

os.makedirs("metrics", exist_ok=True)

with open("metrics/metrics.json", "w") as f:
    json.dump({
        "accuracy": accuracy,
        "report": report
    }, f, indent=4)

# ROC curve
plt.figure()
RocCurveDisplay.from_estimator(model, X, y)
plt.savefig("metrics/roc.png")

print("Evaluation done")