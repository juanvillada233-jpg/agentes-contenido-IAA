import requests
import os

def generar_copy():
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
                "content": "Eres un experto en marketing digital y redes sociales."
            },
            {
                "role": "user",
                "content": (
                    "Escribe un copy corto, emocional y profesional "
                    "para Instagram o TikTok. Máximo 2 líneas. En español."
                )
            }
        ],
        "temperature": 0.8
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.json()["choices"][0]["message"]["content"]
