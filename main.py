import os
import datetime
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from agents.copy_agent import generar_copy_experto

def subir_a_drive(nombre_archivo, contenido_texto):
    try:
        info = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT"))
        creds = service_account.Credentials.from_service_account_info(info)
        drive_service = build('drive', 'v3', credentials=creds)

        if not os.path.exists('output'): os.makedirs('output')
        ruta_temp = f"output/{nombre_archivo}"
        with open(ruta_temp, "w", encoding="utf-8") as f:
            f.write(contenido_texto)

        folder_id = os.getenv("DRIVE_FOLDER_ID")
        
        file_metadata = {
            'name': nombre_archivo,
            'parents': [folder_id]
        }
        media = MediaFileUpload(ruta_temp, mimetype='text/plain')

        # CAMBIO CLAVE: Usamos fields='id' y forzamos el uso de la carpeta compartida
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id',
            supportsAllDrives=True,
            # Esta línea le dice a Google que no use la cuota del robot
            ignoreDefaultVisibility=True 
        ).execute()

        print(f"🚀 EXITAZO: Archivo subido a Drive con ID: {file.get('id')}")
        
    except Exception as e:
        print(f"❌ ERROR EN DRIVE (Aunque la frase se creó): {e}")

def tarea_diaria():
    tema_de_hoy = "resiliencia" 
    print(f"--- Iniciando Agente Contenido IA: {tema_de_hoy} ---")
    
    try:
        # 1. Generar la frase
        frase_final = generar_copy_experto(tema_de_hoy)
        
        # 2. MOSTRAR LA FRASE INMEDIATAMENTE (Para que no se pierda)
        print("-" * 30)
        print(f"📝 FRASE GENERADA:\n{frase_final}")
        print("-" * 30)
        
        # 3. Intentar subirla
        fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        nombre_f = f"frase_{fecha}.txt"
        subir_a_drive(nombre_f, frase_final)
        
    except Exception as e:
        print(f"❌ ERROR GENERAL: {e}")

if __name__ == "__main__":
    tarea_diaria()
