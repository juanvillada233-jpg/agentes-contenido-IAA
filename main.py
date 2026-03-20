def subir_a_drive(nombre_archivo, ruta_fisica, tipo_mimo):
    try:
        log(f"Intentando subir {nombre_archivo}...")
        info = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT"))
        creds = service_account.Credentials.from_service_account_info(info)
        drive_service = build('drive', 'v3', credentials=creds)

        folder_id = os.getenv("DRIVE_FOLDER_ID")
        
        file_metadata = {
            'name': nombre_archivo,
            'parents': [folder_id]
        }
        
        media = MediaFileUpload(ruta_fisica, mimetype=tipo_mimo, resumable=True)

        # EL TRUCO: Usamos 'fields' para confirmar que se creó y 'supportsAllDrives'
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id',
            supportsAllDrives=True
        ).execute()

        log(f"🚀 ¡LOGRADO! Archivo guardado con ID: {file.get('id')}")

    except Exception as e:
        if "storageQuotaExceeded" in str(e):
            log("❌ ERROR DE CUOTA: El robot no puede usar tu espacio.")
            log("👉 SOLUCIÓN: Ve a la carpeta en Drive, selecciona al robot y asegúrate de que sea EDITOR.")
        else:
            log(f"❌ ERROR DE DRIVE: {e}")
