from flask import Blueprint, request, jsonify
from services.phishing_engine import PhishingEngine
from services.llm_service import LLMService

phishing_bp = Blueprint("phishing", __name__)

engine = PhishingEngine()
llm = LLMService()

@phishing_bp.route("/phishing-analyze", methods=["POST"])
def phishing_analyze():

    data = request.json or {}

    text = data.get("text", "")
    url = data.get("url")

    rule_result = engine.analyze(text, url)
    llm_result = llm.analyze(text)

    # 🔥 FUSION LOGIC
    final_score = rule_result["score"]

    if "phishing" in llm_result["analysis"].lower():
        final_score += 10

    if final_score >= 90:
        final = "phishing"
    elif final_score >= 50:
        final = "suspicious"
    else:
        final = "safe"

    return jsonify({
    "final_verdict": final,
    "confidence": final_score,
    "details": {
        "rule_based": rule_result,
        "llm_analysis": llm_result
    }
})