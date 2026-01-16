import google.generativeai as genai
import os

def generar_prompt_imagen():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel("gemini-1.5-pro")

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

    response = model.generate_content(prompt)
    return response.text



