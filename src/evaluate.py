import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/processed/data.csv")

X = df[["feature1", "feature2", "cholesterol"]]
y = df["target"]

model = joblib.load("models/model.pkl")

preds = model.predict(X)

print("Accuracy:", accuracy_score(y, preds))
print(classification_report(y, preds))

print("Evaluation done")