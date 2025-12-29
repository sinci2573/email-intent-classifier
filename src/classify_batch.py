print("🚀 classify_batch.py is running")

import pandas as pd
from llm_client import classify_email

print("✅ Imports successful")

df = pd.read_csv("data/labelled_emails.csv")
print("✅ Data loaded:", len(df), "rows")

results = []

for _, row in df.iterrows():
    result = classify_email(row["subject"], row["body"])
    results.append(result)

df["predicted_intent"] = [r["intent"] for r in results]
df["predicted_priority"] = [r["priority"] for r in results]
df["predicted_sentiment"] = [r["sentiment"] for r in results]

df.to_csv("data/predictions.csv", index=False)

print("✅ predictions.csv written successfully")
