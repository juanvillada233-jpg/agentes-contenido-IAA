import requests
import os

def generar_prompt_imagen():
    api_key = os.getenv("GROQ_API_KEY")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": "Eres un experto en creación de prompts para IA generadora de imágenes."
            },
            {
                "role": "user",
                "content": (
                    "Crea un prompt detallado para generar una imagen realista, "
                    "profesional y emocional para redes sociales. "
                    "Formato vertical 9:16, estilo cinematográfico, iluminación natural, "
                    "alta calidad. En español."
                )
            }
        ],
        "temperature": 0.8
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.json()["choices"][0]["message"]["content"]

