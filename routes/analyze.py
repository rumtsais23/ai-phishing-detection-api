from flask import Blueprint, request, jsonify

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/ai-analyze", methods=["POST"])
def ai_analyze():

    data = request.json or {}
    text = data.get("input", "")

    return jsonify({
        "message": "AI analyze endpoint working",
        "input": text
    })