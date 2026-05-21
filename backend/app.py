from flask import Flask, jsonify
from flask_cors import CORS
from routes.appointments_r import appointments_bp
from routes.users_r import users_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(appointments_bp)
app.register_blueprint(users_bp)

@app.route("/")
def home():
    return jsonify({"message": "BackEnd del salon funcionando correctamente"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)