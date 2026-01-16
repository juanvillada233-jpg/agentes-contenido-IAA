import google.generativeai as genai
import os
from datetime import datetime
import random

def generar_copy():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY no configurada")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    estilos = [
        "motivacional",
        "emocional",
        "minimalista",
        "inspirador",
        "profesional"
    ]

    prompt = f"""
    Escribe un copy corto para Instagram o TikTok.
    Estilo: {random.choice(estilos)}
    Máximo 2 líneas.
    En español.
    Sin hashtags.
    Fecha: {datetime.now().strftime('%Y-%m-%d')}
    """

    response = model.generate_content(prompt)

    return response.text.strip()


