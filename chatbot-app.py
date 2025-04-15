from flask import Flask, request, jsonify
import random
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    # (same pairs as above)
]

chatbot = Chat(pairs, reflections)

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
    