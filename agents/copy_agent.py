import requests
import os

def generar_copy():
    api_key = os.getenv("GEMINI_API_KEY")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

    prompt = """
    Escribe un copy corto, emocional y profesional,
    ideal para Instagram o TikTok.
    Máximo 2 líneas.
    En español.
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
