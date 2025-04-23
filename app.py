import requests
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

@app.route('/generate_image', methods=['POST'])
def generate_image():
    try:
        data = request.get_json()
        prompt = data['prompt']
        
        # Call Stability API for image generation
        response = requests.post(
            "https://api.stability.ai/v2beta/stable-image/generate/core",
            headers={
                "Authorization": f"Bearer {STABILITY_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "stable-diffusion-xl-1024-v1-0",
                "prompt": prompt,
                "output_format": "png"
            }
        )
        if response.status_code == 200:
            result = response.json()
            return jsonify(result)
        else:
            return jsonify({"error": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

@app.route("/")
def home():
    return "Your AI Image Generator is Running!"

