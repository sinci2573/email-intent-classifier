def classify_email(subject: str, body: str) -> dict:
    """
    Final hardened mock LLM classifier.
    Handles intent, priority, and sentiment with strong rule hierarchy.
    """

    text = f"{subject} {body}".lower()

    # Defaults
    intent = "Other"
    priority = "Low"
    sentiment = "Neutral"

    # 1️⃣ SENTIMENT (first, independent)
    if any(word in text for word in [
        "thank", "thanks", "appreciate", "great", "happy", "love", "excellent"
    ]):
        sentiment = "Positive"

    if any(word in text for word in [
        "frustrating", "angry", "upset", "not working",
        "failed", "error", "hacked", "compromised"
    ]):
        sentiment = "Negative"

    # 2️⃣ SECURITY ISSUES (always complaints, always high priority)
    if any(word in text for word in [
        "security", "hacked", "suspicious", "compromised", "unauthorized"
    ]):
        intent = "Complaint"
        priority = "High"
        sentiment = "Negative"

    # 3️⃣ PERFORMANCE ISSUES (non-payment complaints)
    elif any(word in text for word in [ 
        "slow", "freezes", "lag", "laggy", "performance", "unresponsive"
]):
        intent = "Complaint"
        priority = "Medium"
        sentiment = "Negative"

    # 4 PAYMENT & SERVICE FAILURES (complaints)
    elif any(word in text for word in [
        "payment", "charged", "deducted",
        "not activated", "not active",
        "service not working", "subscription"
    ]):
        intent = "Complaint"
        priority = "High"
        sentiment = "Negative"

    # 5 FEATURE REQUESTS
    elif any(word in text for word in [
        "add", "feature", "request", "could you", "please add", "suggestion"
    ]):
        intent = "Request"
        priority = "Low"

    # 6 QUESTIONS / QUERIES
    elif any(word in text for word in [
        "how", "what", "can you explain", "when", "why"
    ]):
        intent = "Query"
        priority = "Low"

    # 7 PURE FEEDBACK (protected)
    elif sentiment == "Positive":
        intent = "Feedback"
        priority = "Low"

    return {
        "intent": intent,
        "priority": priority,
        "sentiment": sentiment
    }
