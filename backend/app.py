from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
import traceback

# 🔐 Set your Gemini API key
load_dotenv()

API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

# 📡 Setup Flask
app = Flask(__name__)
CORS(app)

# 🤖 Load Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-pro")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "Please enter a message."})

    try:
        response = model.generate_content(user_message)
        print(response)
        reply = response.text.strip()
        return jsonify({"reply": reply})
    except Exception as e:
      print("Gemini Error:", e)
      traceback.print_exc()  # Add this line
      return jsonify({"reply": "Something went wrong with the AI model."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
