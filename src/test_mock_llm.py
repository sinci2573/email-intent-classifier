from llm_client import classify_email

subject = "Payment failed"
body = "My payment failed but the amount was deducted from my account."

result = classify_email(subject, body)

print("Mock LLM result:")
print(result)
