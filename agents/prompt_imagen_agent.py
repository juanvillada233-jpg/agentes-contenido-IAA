import requests
import os
import json

def generar_prompt_imagen():
    api_key = os.getenv("GEMINI_API_KEY")

    url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key
    }

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
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
