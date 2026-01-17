import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generar_copy():
    if not GROQ_API_KEY:
        raise ValueError("❌ GROQ_API_KEY no está definida")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "system",
                "content": "Eres un experto en marketing digital y copywriting."
            },
            {
                "role": "user",
                "content": "Crea un copy publicitario profesional, persuasivo y corto para redes sociales."
            }
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
