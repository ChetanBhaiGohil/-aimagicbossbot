import requests

def generate_image(prompt: str):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {"Authorization": f"Bearer YOUR_HF_API_KEY"}

    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content  # Image bytes
    else:
        return None