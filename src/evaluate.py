import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
import json

df = pd.read_csv("data/processed/data.csv")

X = df[["feature1", "feature2"]]
y = df["label"]

model = joblib.load("models/model.pkl")

pred = model.predict(X)

acc = accuracy_score(y, pred)

metrics = {"accuracy": acc}

with open("metrics/metrics.json", "w") as f:
    json.dump(metrics, f)

print(metrics)