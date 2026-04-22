from flask import Blueprint, request, jsonify

security_bp = Blueprint("security", __name__)

@security_bp.route("/security-scan", methods=["POST"])
def security_scan():
    data = request.json or {}
    text = data.get("input", "")

    # примерен резултат (или твоя engine)
    return jsonify({
        "ok": True,
        "input": text
    })