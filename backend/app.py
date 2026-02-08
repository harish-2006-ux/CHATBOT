from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_engine import interpret_query

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Invalid command."}), 400

    message = data["message"].strip()
    if message == "":
        return jsonify({"reply": "Empty command rejected."})

    reply = interpret_query(message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
