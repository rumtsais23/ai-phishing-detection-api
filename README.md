# 🛡️ AI Phishing Detection & Security Analysis API

A production-style AI-powered security system that detects phishing attempts, prompt injection attacks, and performs basic threat modeling using a hybrid rule-based + AI fusion approach.

---

## 🚀 Live Demo

https://ai-phishing-detection-api-w6lf.onrender.com/

---

## 🧠 Features

### 🔍 Phishing Detection Engine
- Rule-based pattern detection
- URL analysis
- Credential harvesting detection
- Urgency & social engineering signals

### 🧠 AI Security Layer
- Prompt injection detection
- Malicious instruction recognition
- Security classification (safe / suspicious / malicious)

### ⚖️ Threat Modeling (light STRIDE-inspired)
- Information disclosure detection
- Privilege escalation detection
- Spoofing patterns

### 🔥 AI Fusion Engine
- Combines:
  - Rule-based score
  - Threat model score
  - LLM analysis (fallback/mock supported)

- Outputs final:
  - risk_score (0–100)
  - risk_level (low / medium / high / critical)
  - verdict (ALLOW / BLOCK)

---

## 🧪 API Endpoints

### 1. Phishing Detection
`POST /phishing-analyze`

```json
{
  "text": "Your account will be suspended, login immediately"
}
