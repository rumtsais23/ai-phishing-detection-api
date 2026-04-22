class URLAnalyzer:

    def analyze(self, url: str):

        if not url:
            return {"risk": "none"}

        risk = 0
        reasons = []

        if "bit.ly" in url or "tinyurl" in url:
            risk += 30
            reasons.append("URL shortener used")

        if not url.startswith("https"):
            risk += 20
            reasons.append("No HTTPS")

        return {
            "url_risk": risk,
            "reasons": reasons
        }