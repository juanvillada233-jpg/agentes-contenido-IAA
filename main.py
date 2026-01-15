from agents.copy_agent import generar_copy
from agents.prompt_imagen_agent import generar_prompt_imagen
from datetime import datetime
import json
import os

def run_agents():
    # Crear carpeta output si no existe
    os.makedirs("output", exist_ok=True)

    # Ejecutar agentes
    copy = generar_copy()
    prompt_imagen = generar_prompt_imagen(copy)

    # Armar resultado
    contenido = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "copy": copy,
        "prompt_imagen": prompt_imagen
    }

    # Guardar archivo
    nombre_archivo = f"output/{datetime.now().strftime('%Y%m%d_%H%M')}.json"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(contenido, f, ensure_ascii=False, indent=2)

    print("Contenido generado correctamente")

if __name__ == "__main__":
    run_agents()
