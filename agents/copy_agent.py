import requests
import os
from datetime import datetime
import random

def generar_copy():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY no está configurada")

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.0-pro:generateContent?key={api_key}"

    estilos = [
        "motivacional",
        "emocional",
        "minimalista",
        "inspirador",
        "profesional"
    ]

    prompt = f"""
    Escribe un copy corto para redes sociales (Instagram o TikTok).
    Estilo: {random.choice(estilos)}.
    Máximo 2 líneas.
    En español.
    No uses hashtags.
    Fecha: {datetime.now().strftime('%Y-%m-%d')}
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

    response = requests.post(url, json=data, timeout=30)

    if response.status_code != 200:
        raise RuntimeError(f"Error Gemini: {response.text}")

    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"].strip()

