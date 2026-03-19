from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/generate", methods=["POST"])
def generate():
    video_url = "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"
    return jsonify({"video": video_url})

if __name__ == "__main__":
    app.run()
