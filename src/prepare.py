import os
import psycopg2
import pandas as pd

# CI flag (GitHub Actions automatski setuje CI=true)
IS_CI = os.getenv("CI")

if IS_CI:
    # GitHub Actions PostgreSQL service
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="db",
        user="postgres",
        password="pass"
    )
else:
    # Lokalno (Docker Compose)
    conn = psycopg2.connect(
        host="postgres",
        port=5432,
        database="db",
        user="postgres",
        password="pass"
    )

# Load data from DB
df = pd.read_sql("SELECT * FROM data", conn)

# Save processed data
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/data.csv", index=False)

print("Prepared data successfully")