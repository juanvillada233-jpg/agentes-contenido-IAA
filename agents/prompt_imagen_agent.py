
import requests
import os
from datetime import datetime

def generar_prompt_imagen(copy_texto):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY no está configurada")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    prompt = f"""
    A partir del siguiente copy para redes sociales:

    "{copy_texto}"

    Crea un prompt detallado para generar una imagen:
    - Realista y emocional
    - Estilo cinematográfico
    - Formato vertical 9:16
    - Iluminación natural
    - Alta calidad
    - Sin texto en la imagen
    - Descripción clara de escenario, sujeto, emociones y ambiente
    - En español

    El resultado debe ser SOLO el prompt de imagen.
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
        raise RuntimeError(f"Error Gemini imagen: {response.text}")

    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"].strip()
