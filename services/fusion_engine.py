from services.llm_service import LLMService

# Hybrid AI security fusion system combining:
# - rule-based detection
# - threat modeling (STRIDE-inspired)
# - LLM-based reasoning

class AISecurityFusionEngine:

    def __init__(self, security_engine, threat_engine, llm_service):
        self.security_engine = security_engine
        self.threat_engine = threat_engine
        self.llm_service = llm_service

    def analyze(self, text):

        # 1. Rule-based security scan
        security_result = self.security_engine.analyze(text)
        security_score = security_result["score"]

        # 2. Threat modeling (STRIDE-like)
        threat_result = self.threat_engine.analyze(text)

        threat_score = 0
        if threat_result["risk_level"] == "phishing":
            threat_score = 70
        elif threat_result["risk_level"] == "suspicious":
            threat_score = 40

        # 3. LLM analysis
        llm_result = self.llm_service.analyze(text)
        llm_text = llm_result.get("analysis", "").lower()
        llm_text = str(llm_result.get("analysis", "")).lower()

        llm_score = 0
        if "phishing" in llm_text:
            llm_score += 30
        if "malicious" in llm_text:
            llm_score += 20

        # 4. Weighted fusion scoring
        final_score = int(
            (security_score * 0.5) +
            (threat_score * 0.3) +
            (llm_score * 0.2)
        )

        final_score = min(100, final_score)

        # 5. Risk classification
        if final_score >= 85:
            risk_level = "critical"
        elif final_score >= 65:
            risk_level = "high"
        elif final_score >= 40:
            risk_level = "medium"
        else:
            risk_level = "low"

        # 6. Final decision
        verdict = "BLOCK" if final_score >= 70 else "ALLOW"

        return {
            "final_risk_level": risk_level,
            "risk_score": final_score,
            "verdict": verdict,
            "security_analysis": security_result,
            "threat_analysis": threat_result,
            "llm_analysis": llm_result
        }