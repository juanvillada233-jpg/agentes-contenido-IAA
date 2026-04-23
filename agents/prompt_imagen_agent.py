import requests
import os
import random

def generar_copy_experto(tipo="resiliencia"):
    """
    Agente avanzado de copywriting emocional/viral.
    Optimizado para evitar monotonía y aumentar engagement.
    """

    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # -------------------------------
    # MODOS DINÁMICOS (ANTI-MONOTONÍA)
    # -------------------------------
    modos = [
        "directo y frío (como una verdad absoluta)",
        "reflexivo y profundo",
        "confrontativo (como si fuera una verdad que duele)",
        "espiritual (enfocado en Dios y propósito)",
        "desapegado (sin emoción, casi indiferente)",
        "tipo advertencia (como consejo fuerte de vida)",
    ]

    modo = random.choice(modos)

    # -------------------------------
    # TEMAS BASE
    # -------------------------------
    temas = {
        "resiliencia": "Irse de donde no te valoran y proteger tu energía.",
        "fe": "Confiar en Dios cuando todo parece salir mal.",
        "autoestima": "Elegirse a uno mismo sin competir por atención.",
        "leccion": "Aceptar que las personas no cambian y aprender a soltar."
    }

    # -------------------------------
    # SYSTEM PROMPT (OPTIMIZADO)
    # -------------------------------
    system_prompt = (
        "Eres un autor de élite en Instagram especializado en 'Minimalismo Emocional'. "
        "Tu contenido es altamente viral, profundo y genera identificación inmediata.\n\n"
        
        "DIRECTRICES:\n"
        "1. IMPACTO: Empieza con una verdad incómoda, pregunta o afirmación fuerte.\n"
        "2. FILOSOFÍA: Mezcla estoicismo con fe en Dios.\n"
        "3. RITMO: Usa frases cortas. Cada línea debe sentirse como un golpe.\n"
        "4. LENGUAJE: Usa verbos fuertes. Evita palabras de relleno.\n"
        "5. VARIACIÓN: No repitas estructuras. Cambia inicio, ritmo y cierre.\n"
        "6. EMOCIÓN: Puede ser frío, confrontativo, reflexivo o espiritual.\n"
        "7. IMPACTO PSICOLÓGICO: Genera duda, incomodidad o revelación.\n"
        "8. RESTRICCIÓN: Máximo 40 palabras. Sin hashtags. Máximo 1 emoji neutro.\n"
    )

    # -------------------------------
    # EJEMPLOS MEJORADOS (FEW-SHOT)
    # -------------------------------
    ejemplos_guia = (
        "\nEJEMPLOS DEL TONO DESEADO:\n"
        "- No te perdí. Me liberé.\n"
        "- Dios no te quitó nada, te mostró quién no era para ti.\n"
        "- Te dolió porque esperabas más de alguien que daba lo mínimo.\n"
        "- No cierres ciclos. Aprende a no volver.\n"
        "- A veces irse tarde también es fallarte.\n"
        "- No era amor. Era costumbre.\n"
    )

    # -------------------------------
    # PROMPT USUARIO (DINÁMICO)
    # -------------------------------
    prompt_usuario = (
        f"Tema: {temas.get(tipo, temas['resiliencia'])}.\n"
        f"Tono: {modo}.\n"
        "Debe parecer una frase que la gente guardaría o compartiría por WhatsApp.\n"
        "Evita repetir estructuras comunes.\n"
        "Hazlo potente y diferente."
    )

    # -------------------------------
    # REQUEST
    # -------------------------------
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": system_prompt + ejemplos_guia},
            {"role": "user", "content": prompt_usuario}
        ],
        "temperature": 0.75,
        "top_p": 0.9
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise RuntimeError(f"Error en la API de Groq: {response.text}")

    # -------------------------------
    # LIMPIEZA FINAL
    # -------------------------------
    resultado = response.json()["choices"][0]["message"]["content"].strip()

    resultado = (
        resultado.replace('"', '')
        .replace('“', '')
        .replace('”', '')
        .strip()
    )

    return resultado
