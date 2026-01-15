import requests
import os

def generar_prompt_imagen():
    api_key = os.getenv("GEMINI_API_KEY")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

    prompt = """
    Crea un prompt detallado para generar una imagen
    realista, profesional y emocional,
    ideal para redes sociales.
    
    Requisitos:
    - Formato vertical 9:16
    - Estilo cinematográfico
    - Iluminación natural
    - Alta calidad
    - En español
    """

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]
