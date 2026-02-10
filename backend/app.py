from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_engine import interpret_query
from db import init_db, save_chat

app = Flask(__name__)
CORS(app)

# Initialize database
init_db()


@app.route("/")
def index():
    return "Shadow Interpreter API is running", 200


@app.route("/health")
def health():
    return "OK", 200


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Invalid command."}), 400

    message = data["message"].strip()
    if not message:
        return jsonify({"reply": "Empty command rejected."})

    try:
        reply = interpret_query(message)
    except Exception:
        reply = "Shadow link unstable. Retry command."

    save_chat(message, reply)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
