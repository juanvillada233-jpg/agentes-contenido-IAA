import requests
import os

def generar_copy(tipo):
    api_key = os.getenv("GROQ_API_KEY")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompts = {
        "inspiracional": "Escribe un copy motivacional corto, positivo e inspirador para empezar el día. Sin CTA. En español.",
        "disciplina": "Escribe un copy motivacional enfocado en disciplina, constancia y esfuerzo diario. Sin CTA. En español.",
        "cta": "Escribe un copy motivacional con cierre poderoso e incluye un CTA suave para seguir la cuenta o compartir. En español."
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Eres un experto en marketing motivacional para redes sociales."},
            {"role": "user", "content": prompts[tipo]}
        ],
        "temperature": 0.8
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.json()["choices"][0]["message"]["content"]
