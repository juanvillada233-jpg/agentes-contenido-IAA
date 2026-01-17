from agents.copy_agent import generar_copy
from agents.prompt_imagen_agent import generar_prompt_imagen
from drive.drive_uploader import subir_json_drive
from datetime import datetime


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

    subir_json_drive(data)


if __name__ == "__main__":
    run_agents()
