class PhishingEngine:

    def analyze(self, text: str, url: str = None):

        score = 0
        indicators = []

        text_lower = text.lower()

        # 1. Urgency patterns
        urgency_keywords = ["urgent", "immediately", "act now", "limited time"]
        if any(word in text_lower for word in urgency_keywords):
            score += 25
            indicators.append("Urgency language detected")

        # 2. Credential requests
        if any(word in text_lower for word in ["password", "login", "verify account"]):
            score += 35
            indicators.append("Credential request detected")

        # 3. Money / scam signals
        if any(word in text_lower for word in ["bank", "payment", "invoice", "suspended"]):
            score += 20
            indicators.append("Financial scam indicators")

        # 4. URL check (basic)
        if url:
            if "http" in url and not url.startswith("https"):
                score += 20
                indicators.append("Non-secure HTTP link")

        # Final classification
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