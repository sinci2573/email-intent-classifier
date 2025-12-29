import pandas as pd
from sklearn.metrics import classification_report

# Load predictions
df = pd.read_csv("data/predictions.csv")

print("📊 EVALUATION RESULTS")

# Intent evaluation
print("\nIntent classification report:")
print(
    classification_report(
        df["intent"],
        df["predicted_intent"],
        zero_division=0
    )
)

# Priority evaluation
print("\nPriority classification report:")
print(
    classification_report(
        df["priority"],
        df["predicted_priority"],
        zero_division=0
    )
)

# Sentiment evaluation
print("\nSentiment classification report:")
print(
    classification_report(
        df["sentiment"],
        df["predicted_sentiment"],
        zero_division=0
    )
)
