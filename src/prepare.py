import os
import psycopg2
import pandas as pd

# Detect CI environment
IS_CI = os.getenv("CI")

if IS_CI:
    host = "localhost"
else:
    host = "postgres"

conn = psycopg2.connect(
    host=host,
    port=5432,
    database="db",
    user="postgres",
    password="pass"
)

# Load data
df = pd.read_sql("SELECT * FROM data", conn)

# Save processed data
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/data.csv", index=False)

print("Prepared data successfully")