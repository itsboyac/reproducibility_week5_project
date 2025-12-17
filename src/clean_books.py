import pandas as pd
import sqlite3, os

input_file = "data/processed/books.csv"
df = pd.read_csv(input_file)

df["title"] = (
    df["title"].str.lower().str.strip()
)

os.makedirs("data/processed", exist_ok=True)
cleaned_file = "data/processed/books_clean.csv"
df.to_csv(cleaned_file, index=False)
print(f"Saved cleaned data to {cleaned_file}")

os.makedirs("data", exist_ok=True)
db_file = "data/books.db"
conn = sqlite3.connect(db_file)
df.to_sql("books", conn, if_exists="replace", index=False)
conn.close()
print(f"Saved data to SQLite database at {db_file}")

conn = sqlite3.connect(db_file)
check = pd.read_sql("SELECT * FROM books LIMIT 5;", conn)
conn.close()

print("Preview from SQLite:")
print(check)
