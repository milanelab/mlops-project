import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="postgres",
    database="ml_db",
    user="user",
    password="pass"
)

df = pd.read_sql("SELECT * FROM data", conn)

df.to_csv("data/processed/data.csv", index=False)

print("Prepared data")