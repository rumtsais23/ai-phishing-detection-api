import os
from openai import OpenAI

class LLMService:

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        # safety check (important for production systems)
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            self.client = None

    def analyze(self, text):

        # 1. Try real OpenAI call
        try:
            if self.client:

                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "user",
                            "content": f"""
You are a cybersecurity AI assistant.

Analyze if this text is phishing or malicious:

{text}

Return:
- classification
- short explanation
"""
                        }
                    ]
                )

                return {
                    "analysis": response.choices[0].message.content,
                    "source": "openai"
                }

        except Exception as e:
            # fallback triggered if quota / API fails
            return self._fallback(text, str(e))

        # 2. If no API key or failure → fallback
        return self._fallback(text, "no_openai_key")

    def _fallback(self, text, reason):

        # deterministic fallback (important for demo stability)
        keywords = ["password", "login", "urgent", "verify", "click"]

        risk = "safe"
        if any(k in text.lower() for k in keywords):
            risk = "suspicious"

        return {
            "analysis": f"[FALLBACK MODE] Basic heuristic analysis applied to: {text}",
            "classification": risk,
            "source": "fallback",
            "reason": reason
        }