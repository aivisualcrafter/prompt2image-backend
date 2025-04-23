import os
import requests
from datetime import datetime

def generate_image(prompt, image_name, description):
    api_key = os.getenv("SCALABILITY_API_KEY")
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{image_name}_{description[:20].replace(' ', '_')}_{timestamp}.png"
    filepath = os.path.join("static", filename)

    payload = {
        "key": api_key,
        "prompt": prompt,
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "30"
    }

    response = requests.post("https://stablediffusionapi.com/api/v3/text2img", json=payload)

    if response.status_code == 200:
        image_url = response.json()['output'][0]
        img_data = requests.get(image_url).content
        with open(filepath, 'wb') as handler:
            handler.write(img_data)
        return filename
    else:
        return None