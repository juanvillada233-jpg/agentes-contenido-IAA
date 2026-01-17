from agents.copy_agent import generar_copy
from agents.prompt_imagen_agent import generar_prompt_imagen
from datetime import datetime
import json
import os

def run_agents():
    ahora = datetime.now()
    hora = ahora.hour

    # Definir tipo según la hora
    if hora < 12:
        tipo = "inspiracion"
    elif hora < 18:
        tipo = "reflexion"
    else:
        tipo = "cta"

    os.makedirs("output", exist_ok=True)

    copy = generar_copy(tipo)
    prompt_imagen = generar_prompt_imagen()

    contenido = {
        "fecha": ahora.strftime("%Y-%m-%d"),
        "hora": ahora.strftime("%H:%M"),
        "tipo": tipo,
        "copy": copy,
        "prompt_imagen": prompt_imagen
    }

    nombre_archivo = f"output/{ahora.strftime('%H-%M')}_{tipo}.json"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(contenido, f, ensure_ascii=False, indent=2)

    print(f"Contenido generado: {tipo}")

if __name__ == "__main__":
    run_agents()
