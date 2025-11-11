from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from database import save_message, get_all_messages
from generate_image import generate_image
from dotenv import load_dotenv
import os

load_dotenv()  # تحميل القيم من ملف .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__, static_folder='.')


@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.post("/api/chat")
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    save_message("user", user_message)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "أنت مساعد ذكي أنيق وودود."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content
    save_message("assistant", reply)
    return jsonify({"reply": reply})

@app.post("/api/generate-image")
def gen_image():
    data = request.get_json()
    prompt = data.get("prompt", "")
    filename = generate_image(prompt)
    return jsonify({"image": filename})

@app.get("/admin")
def admin():
    messages = get_all_messages()
    html = "<h2>سجل المحادثات</h2><ul>"
    for role, content in messages:
        html += f"<li><b>{role}:</b> {content}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    print("✅ السيرفر يعمل الآن على: http://127.0.0.1:3000")
    app.run(port=3000, debug=True)
