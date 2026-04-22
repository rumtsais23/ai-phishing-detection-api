import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise Exception("Missing OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

class LLMService:

    def analyze(self, text: str):

        prompt = f"""
You are a cybersecurity phishing detection expert.

Analyze this message and detect phishing risk:

Text:
{text}

Return:
- risk explanation
- phishing indicators
- confidence (0-100)
"""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            return {
                "source": "openai",
                "analysis": response.choices[0].message.content
            }

        except Exception as e:
            # 🔥 FALLBACK (МНОГО ВАЖНО)
            return {
                "source": "mock",
                "analysis": f"[MOCK] Potential phishing detected in: {text}",
                "note": "OpenAI quota exceeded, using fallback"
            }