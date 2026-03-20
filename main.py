import os
import datetime
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from agents.copy_agent import generar_copy_experto

def subir_a_drive(nombre_archivo, contenido_texto):
    """Función que conecta con la API de Google para subir el archivo."""
    try:
        # 1. Cargar las credenciales desde el secreto de GitHub
        info = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT"))
        creds = service_account.Credentials.from_service_account_info(info)
        drive_service = build('drive', 'v3', credentials=creds)

        # 2. Crear un archivo temporal físico para poder subirlo
        ruta_temp = f"output/{nombre_archivo}"
        if not os.path.exists('output'): os.makedirs('output')
        
        with open(ruta_temp, "w", encoding="utf-8") as f:
            f.write(contenido_texto)

        # 3. Configurar dónde se sube (ID de carpeta)
        file_metadata = {
            'name': nombre_archivo,
            'parents': [os.getenv("DRIVE_FOLDER_ID")]
        }
        media = MediaFileUpload(ruta_temp, mimetype='text/plain')

        # 4. Ejecutar la subida
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"🚀 EXITAZO: Archivo subido a Drive con ID: {file.get('id')}")
        
    except Exception as e:
        print(f"❌ ERROR EN DRIVE: {e}")

def tarea_diaria():
    tema_de_hoy = "resiliencia" 
    print(f"--- Iniciando Agente Contenido IA: {tema_de_hoy} ---")
    
    try:
        # 1. Generar la frase con el entrenamiento de 500k
        frase_final = generar_copy_experto(tema_de_hoy)
        
        # 2. Nombre del archivo con fecha
        fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        nombre_f = f"frase_{fecha}.txt"
        
        # 3. LLAMAR A LA FUNCIÓN DE SUBIDA (Esto era lo que faltaba)
        subir_a_drive(nombre_f, frase_final)
        
        print(f"✅ Proceso terminado. Frase: {frase_final}")
        
    except Exception as e:
        print(f"❌ ERROR GENERAL: {e}")

if __name__ == "__main__":
    tarea_diaria()
