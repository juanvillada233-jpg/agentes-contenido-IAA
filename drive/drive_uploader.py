from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def subir_a_drive(ruta_archivo, nombre_archivo):
    creds_info = os.getenv("GOOGLE_SERVICE_ACCOUNT")

    credentials = service_account.Credentials.from_service_account_info(
        eval(creds_info),
        scopes=SCOPES
    )

    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': nombre_archivo,
        'parents': [os.getenv("DRIVE_FOLDER_ID")]
    }

    media = MediaFileUpload(
        ruta_archivo,
        mimetype='application/json'
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    return file.get('id')
