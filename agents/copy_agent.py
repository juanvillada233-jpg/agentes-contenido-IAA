import requests
import os

def generar_copy_experto(tipo):
    """
    Agente especializado en copywriting estoico y espiritual.
    Entrenado con ingeniería inversa de cuentas virales (500k+ followers).
    """
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # --- CONFIGURACIÓN TÉCNICA DEL PROMPT (EL "ENTRENAMIENTO") ---
    system_prompt = (
        "Eres un autor de élite en Instagram especializado en 'Minimalismo Emocional'. "
        "Tu audiencia son personas que buscan sanar, ponerse primero y fortalecer su fe. "
        "\n\nDIRECTRICES DE ESTILO (INGENIERÍA INVERSA):\n"
        "1. ESTRUCTURA DE IMPACTO: Comienza con una verdad cruda o una decisión difícil. "
        "2. FILOSOFÍA: Mezcla el estoicismo (autocontrol) con la fe en Dios. "
        "3. RITMO: Usa frases cortas. Evita párrafos largos. Cada línea debe ser un golpe de sabiduría. "
        "4. LENGUAJE: No uses palabras de relleno ('increíble', 'maravilloso'). Usa verbos de acción ('elegí', 'solté', 'avancé'). "
        "5. RESTRICCIÓN VISUAL: Máximo 40 palabras. Sin hashtags. Máximo 1 emoji de color neutro (🤍, ✨, 🙏)."
    )

    # --- EJEMPLOS DE ENTRENAMIENTO (FEW-SHOT) ---
    # Esto le enseña al modelo el 'tono' exacto de tus imágenes de ejemplo.
    ejemplos_guia = (
        "\n\nEJEMPLOS DEL TONO DESEADO:\n"
        "- 'Me dolió, pero tuve que elegirme a mí antes que a alguien que no sabía qué quería'.\n"
        "- 'Si perderte me acercó a Dios, entonces perderte fue mi mayor victoria'.\n"
        "- 'Mi paz no es negociable, ni por amor, ni por amistad, ni por nadie'."
    )

    # --- CATEGORÍAS SEGÚN TUS FOTOS ---
    temas = {
        "resiliencia": "Sobre el valor de irse de donde no te valoran y proteger tu energía.",
        "fe": "Sobre confiar en los tiempos de Dios cuando todo parece ir mal.",
        "autoestima": "Sobre ser una buena mujer/persona y no competir con nadie por atención.",
        "leccion": "Sobre aprender que las personas no cambian y tu silencio es tu mejor respuesta."
    }

    prompt_usuario = f"Tema de hoy: {temas.get(tipo, temas['resiliencia'])}. Escribe una frase viral siguiendo el estilo entrenado."

    data = {
        "model": "llama-3.1-8b-instant", # Modelo potente para captar el matiz emocional
        "messages": [
            {"role": "system", "content": system_prompt + ejemplos_guia},
            {"role": "user", "content": prompt_usuario}
        ],
        "temperature": 0.6, # Creatividad controlada para no perder la esencia
        "top_p": 0.9
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise RuntimeError(f"Error en la API de Groq: {response.text}")

    # PROCESAMIENTO FINAL DEL TEXTO
    resultado = response.json()["choices"][0]["message"]["content"].strip()
    
    # Limpieza: quitamos comillas si la IA las añade por error
    resultado = resultado.replace('"', '').replace('“', '').replace('”', '')
    
    return resultado
