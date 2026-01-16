import google.generativeai as genai
import os

def generar_copy():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

    prompt = """
    Escribe un copy corto, emocional y profesional,
    ideal para Instagram o TikTok.
    Máximo 2 líneas.
    En español.
    """

    response = model.generate_content(prompt)
    return response.text



