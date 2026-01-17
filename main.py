from agents.copy_agent import generar_copy
from agents.prompt_imagen_agent import generar_prompt_imagen
from drive.drive_uploader import subir_a_drive
from datetime import datetime
import json
import os

def run_agents():
    os.makedirs("output", exist_ok=True)

    copy = generar_copy()
    prompt_imagen = generar_prompt_imagen()

    contenido = {
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "hora": datetime.now().strftime("%H:%M"),
        "copy": copy,
        "prompt_imagen": prompt_imagen
    }

    nombre_archivo = f"{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    ruta = f"output/{nombre_archivo}"

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(contenido, f, ensure_ascii=False, indent=2)

    # SUBIR A DRIVE
    subir_a_drive(ruta, nombre_archivo)

    print("Contenido generado y subido a Google Drive")

if __name__ == "__main__":
    run_agents()
