import os
import json
import datetime
import requests
import io
from PIL import Image, ImageDraw, ImageFont
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

def subir_a_drive(nombre_archivo, ruta_fisica):
    try:
        log(f"Conectando a Drive para subir {nombre_archivo}...")
        # Cargar credenciales desde GitHub Secrets
        info = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT"))
        creds = service_account.Credentials.from_service_account_info(info)
        drive_service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': nombre_archivo,
            'parents': [os.getenv("DRIVE_FOLDER_ID")]
        }
        media = MediaFileUpload(ruta_fisica, mimetype='image/jpeg')

        # Subida forzada para evitar errores de cuota en cuentas gratis
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id',
            supportsAllDrives=True
        ).execute()
        log(f"✅ ¡ÉXITO TOTAL! Archivo en Drive con ID: {file.get('id')}")
    except Exception as e:
        log(f"❌ ERROR EN DRIVE: {e}")

def tarea_diaria():
    log("--- 🤖 INICIANDO PROCESO DE CONTENIDO ---")
    try:
        # 1. Generar la frase con Groq
        frase = generar_copy_experto("resiliencia")
        log(f"📝 Frase generada: {frase}")

        # 2. Crear Imagen Minimalista (1080x1350 - Formato Instagram)
        log("🎨 Creando diseño visual...")
        img = Image.new('RGB', (1080, 1350), color='black')
        draw = ImageDraw.Draw(img)
        
        # Escribir frase (Blanco, centrada)
        # Nota: Usamos la fuente por defecto si no hay una .ttf en el servidor
        draw.text((540, 675), frase, fill="white", anchor="mm", align="center")
        
        if not os.path.exists('output'): os.makedirs('output')
        ruta_post = "output/post_final.jpg"
        img.save(ruta_post, quality=95)

        # 3. Subir el archivo final a la carpeta compartida de Drive
        fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        subir_a_drive(f"Post_IA_{fecha}.jpg", ruta_post)

    except Exception as e:
        log(f"❌ ERROR GENERAL: {e}")

if __name__ == "__main__":
    tarea_diaria()
    log("--- 🏁 AGENTE FINALIZÓ SU TURNO ---")
