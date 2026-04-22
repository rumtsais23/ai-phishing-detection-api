from flask import Flask
from routes.phishing import phishing_bp

app = Flask(__name__)

app.register_blueprint(phishing_bp)

if __name__ == "__main__":
    app.run(debug=True)