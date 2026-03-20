import os
import sys
import datetime
import json

# Forzamos que los prints salgan SIEMPRE
def log(msg):
    print(f"DEBUG: {msg}", flush=True)

log("--- 🤖 INICIANDO AGENTE ---")

try:
    import requests
    import io
    from PIL import Image, ImageDraw, ImageFont
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from agents.copy_agent import generar_copy_experto
    log("✅ Librerías cargadas correctamente")
except Exception as e:
    log(f"❌ ERROR AL CARGAR LIBRERÍAS: {e}")
    sys.exit(1)

def subir_a_drive(nombre_archivo, ruta_fisica, tipo_mimo):
    try:
        log(f"Conectando a Drive para subir: {nombre_archivo}")
        info = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT"))
        creds = service_account.Credentials.from_service_account_info(info)
        drive_service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': nombre_archivo,
            'parents': [os.getenv("DRIVE_FOLDER_ID")]
        }
        media = MediaFileUpload(ruta_fisica, mimetype=tipo_mimo)

        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id',
            supportsAllDrives=True
        ).execute()
        log(f"🚀 SUBIDO A DRIVE CON ID: {file.get('id')}")
    except Exception as e:
        log(f"❌ ERROR DRIVE: {e}")

def tarea_diaria():
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    if not hf_token:
        log("⚠️ ADVERTENCIA: No se encontró HUGGINGFACE_TOKEN")

    try:
        log("Generando frase con Groq...")
        frase = generar_copy_experto("resiliencia")
        log(f"📝 Frase generada: {frase}")

        # Crear carpeta output si no existe
        if not os.path.exists('output'): os.makedirs('output')

        # --- GENERACIÓN DE IMAGEN ---
        log("Llamando a Hugging Face...")
        headers = {"Authorization": f"Bearer {hf_token}"}
        payload = {"inputs": "minimalist deep black solid background, 4k"}
        
        # Usamos un modelo más rápido y estable
        url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            log("✅ Imagen recibida de Hugging Face")
            img = Image.open(io.BytesIO(response.content))
            draw = ImageDraw.Draw(img)
            # Dibujamos algo simple por ahora para testear
            draw.text((50, 50), frase[:30] + "...", fill="white")
            
            ruta_post = "output/test_post.jpg"
            img.save(ruta_post)
            
            fecha = datetime.datetime.now().strftime("%Y-%m-%d")
            subir_a_drive(f"post_{fecha}.jpg", ruta_post, "image/jpeg")
        else:
            log(f"❌ Error en Hugging Face: {response.status_code} - {response.text}")

    except Exception as e:
        log(f"❌ ERROR EN TAREA DIARIA: {e}")

if __name__ == "__main__":
    tarea_diaria()
    log("--- 🏁 FIN DEL PROCESO ---")
