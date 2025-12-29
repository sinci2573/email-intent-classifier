import pandas as pd

print("Script started")

df = pd.read_csv("data/labelled_emails.csv")

print("First 5 emails:")
print(df.head())

print("\nIntent counts:")
print(df["intent"].value_counts())

print("\nPriority counts:")
print(df["priority"].value_counts())

print("\nSentiment counts:")
print(df["sentiment"].value_counts())
