
import google.generativeai as genai
import os
from datetime import datetime

def generar_prompt_imagen(copy_texto):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY no configurada")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    A partir del siguiente copy:

    "{copy_texto}"

    Genera un prompt de imagen con estas características:
    - Estilo cinematográfico
    - Emocional
    - Realista
    - Vertical 9:16
    - Iluminación natural
    - Alta calidad
    - Sin texto en la imagen
    - En español

    Devuelve SOLO el prompt de imagen.
    Fecha: {datetime.now().strftime('%Y-%m-%d')}
    """

    response = model.generate_content(prompt)

    return response.text.strip()

