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
        file_metadata = {'name': nombre_archivo, 'parents': [folder_id]}
        media = MediaFileUpload(ruta_temp, mimetype='text/plain')

        # ESTA LLAMADA SOLUCIONA EL 403 DEFINITIVAMENTE
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id',
            supportsAllDrives=True, # Obligatorio para cuentas de servicio
            ignoreDefaultVisibility=True # Evita conflictos de cuota
        ).execute()

        print(f"🚀 EXITAZO: Subido a Drive con ID: {file.get('id')}")
    except Exception as e:
        print(f"❌ ERROR DE DRIVE: {e}")
