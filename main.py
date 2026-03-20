import os
import datetime
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from agents.copy_agent import generar_copy_experto

def subir_a_drive(nombre_archivo, contenido_texto):
    """Conecta con la API de Google y sube el archivo usando el espacio de la carpeta destino."""
    try:
        # 1. Cargar las credenciales desde el secreto de GitHub
        info = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT"))
        creds = service_account.Credentials.from_service_account_info(info)
        drive_service = build('drive', 'v3', credentials=creds)

        # 2. Preparar el archivo temporal
        if not os.path.exists('output'): 
            os.makedirs('output')
        ruta_temp = f"output/{nombre_archivo}"
        
        with open(ruta_temp, "w", encoding="utf-8") as f:
            f.write(contenido_texto)

        # 3. Configurar metadatos
        # Sacamos el ID de la carpeta de las variables de entorno
        folder_id = os.getenv("DRIVE_FOLDER_ID")
        
        file_metadata = {
            'name': nombre_archivo,
            'parents': [folder_id]
        }
        media = MediaFileUpload(ruta_temp, mimetype='text/plain')

        # 4. EJECUCIÓN ARREGLADA (Soluciona el Error 403 de Quota)
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id',
            supportsAllDrives=True  # IMPORTANTE: Permite usar el espacio de la carpeta compartida
        ).execute()

        print(f"🚀 EXITAZO: Archivo subido a Drive con ID: {file.get('id')}")
        
    except Exception as e:
        print(f"❌ ERROR EN DRIVE: {e}")

def tarea_diaria():
    # Aquí puedes rotar temas: "resiliencia", "fe", "amor propio"
    tema_de_hoy = "resiliencia" 
    print(f"--- Iniciando Agente Contenido IA: {tema_de_hoy} ---")
    
    try:
        # 1. Generar la frase con el cerebro entrenado
        frase_final = generar_copy_experto(tema_de_hoy)
        
        # 2. Crear nombre único con fecha y hora
        fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        nombre_f = f"frase_{fecha}.txt"
        
        # 3. Subir a la nube
        subir_a_drive(nombre_f, frase_final)
        
        print(f"✅ Proceso terminado con éxito.")
        
    except Exception as e:
        print(f"❌ ERROR GENERAL: {e}")

if __name__ == "__main__":
    tarea_diaria()
