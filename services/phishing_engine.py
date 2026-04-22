import re

PHISHING_PATTERNS = [
    r"urgent action required",
    r"verify your account",
    r"password will expire",
    r"login immediately",
    r"click here",
    r"account suspended",
    r"unauthorized login",
    r"confirm identity"
]

URL_PATTERN = r"https?://[^\s]+"

class PhishingEngine:

    def analyze(self, text, url=None):

    score = 0
    indicators = []

    text_lower = text.lower()

    # pattern detection
    for pattern in PHISHING_PATTERNS:
        if re.search(pattern, text_lower):
            score += 15
            indicators.append(f"Pattern matched: {pattern}")

    # urgency
    urgency_words = ["immediately", "urgent", "now", "asap"]
    if any(word in text_lower for word in urgency_words):
        score += 10
        indicators.append("Urgency language detected")

    # credential harvesting
    if "password" in text_lower or "login" in text_lower:
        score += 20
        indicators.append("Credential-related request detected")

    # URL detection
    if re.search(URL_PATTERN, text):
        score += 25
        indicators.append("URL detected")

    # final classification
    if score >= 70:
        risk = "phishing"
    elif score >= 40:
        risk = "suspicious"
    else:
        risk = "safe"

    return {
        "risk_level": risk,
        "score": score,
        "indicators": indicators
    }