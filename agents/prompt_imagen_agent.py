import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generar_prompt_imagen():
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
                "content": "Eres un director creativo experto en campañas visuales."
            },
            {
                "role": "user",
                "content": (
                    "Genera un prompt detallado para crear una imagen publicitaria "
                    "profesional para redes sociales. Debe ser realista, atractiva "
                    "y enfocada en marketing digital."
                )
            }
        ],
        "temperature": 0.8,
        "max_tokens": 400
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]

