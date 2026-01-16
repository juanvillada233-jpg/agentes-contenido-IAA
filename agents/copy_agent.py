import requests
import os
import json

def generar_copy():
    api_key = os.getenv("GEMINI_API_KEY")

    url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key
    }

    prompt = """
    Escribe un copy corto, emocional y profesional,
    ideal para Instagram o TikTok.
    Máximo 2 líneas.
    En español.
    """

    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
