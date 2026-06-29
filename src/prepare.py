import os
import psycopg2
import pandas as pd

IS_CI = os.getenv("CI")

host = "localhost" if IS_CI else "postgres"

conn = psycopg2.connect(
    host=host,
    port=5432,
    database="db",
    user="postgres",
    password="pass"
)

df = pd.read_sql("SELECT * FROM data", conn)

# Simple feature engineering (IMPORTANT)
df["feature1"] = df["age"]
df["feature2"] = df["pressure"]

os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/data.csv", index=False)

print("Prepared data successfully")