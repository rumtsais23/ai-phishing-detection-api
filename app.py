from flask import Flask
from routes.phishing import phishing_bp
from routes.security import security_bp
from routes.analyze import analyze_bp

app = Flask(__name__)

app.register_blueprint(phishing_bp)
app.register_blueprint(security_bp)
app.register_blueprint(analyze_bp)

if __name__ == "__main__":
    app.run(debug=True)