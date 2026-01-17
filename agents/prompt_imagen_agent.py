import requests
import os


def generar_prompt_imagen(copy_texto):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError("No se encontró la variable de entorno GROQ_API_KEY")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = (
        "Genera un prompt detallado para crear una imagen motivacional "
        "realista y profesional para redes sociales, basada en el siguiente copy:\n\n"
        f"{copy_texto}\n\n"
        "El prompt debe describir escena, emoción, iluminación y estilo visual."
    )

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "system",
                "content": "Eres un experto en prompts para generación de imágenes con IA."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.json()["choices"][0]["message"]["content"]

