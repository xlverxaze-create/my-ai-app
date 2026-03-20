from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    story = data.get('story', '')
    # ဒါက Demo Video Link ပါ
    video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
    return jsonify({"video": video_url})

# Vercel အတွက် လိုအပ်တဲ့ code
if __name__ == "__main__":
    app.run()
