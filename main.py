from agents.copy_agent import generar_copy
from agents.prompt_imagen_agent import generar_prompt_imagen
from drive.drive_uploader import subir_a_drive
from datetime import datetime
import json
import os


def run_agents():
    contenidos = []

    tipos = [
        "inspiracional",
        "disciplina",
        "cta"
    ]

    for tipo in tipos:
        copy = generar_copy(tipo)
        prompt_imagen = generar_prompt_imagen(copy)

        contenidos.append({
            "tipo": tipo,
            "copy": copy,
            "prompt_imagen": prompt_imagen
        })

    data = {
        "fecha": datetime.now().isoformat(),
        "contenidos": contenidos
    }

    # Crear carpeta output si no existe
    os.makedirs("output", exist_ok=True)

    nombre_archivo = f"contenido_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    ruta_archivo = os.path.join("output", nombre_archivo)

    # Guardar JSON local
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Subir archivo a Google Drive
    subir_a_drive(ruta_archivo, nombre_archivo)


if __name__ == "__main__":
    run_agents()
