def crear_post_cuadrado_premium(frase):
    # Formato cuadrado 1:1 (1080x1080)
    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)

    # 1. CARGAR FUENTES
    # FUENTES
    try:
        font_header_bold = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 38)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 36)

        nombre_fuente = "OpenSans-VariableFont_wdth,wght.ttf"
        font_cuerpo_fino = ImageFont.truetype(nombre_fuente, 48)  # ↓ un poco más pequeño
        font_cuerpo = ImageFont.truetype(nombre_fuente, 36)  # 🔥 más pequeño

    except Exception as e:
        log(f"⚠️ Error fuentes: {e}. Usando fuente de sistema.")
        font_header_bold = font_header_regular = font_cuerpo_fino = ImageFont.load_default()
        log(f"⚠️ Error fuentes: {e}")
        font_header_bold = font_header_regular = font_cuerpo = ImageFont.load_default()

    # MÁRGENES
    m_left = int(W * 0.12)
    m_right = int(W * 0.88)
    m_top = int(H * 0.12)
    m_bottom = int(H * 0.88)

    # 2. CABECERA
    # CABECERA
    try:
        logo = Image.open("logo.png").convert("RGBA").resize((125, 125))
        logo = Image.open("logo.png").convert("RGBA").resize((110, 110))
        img.paste(logo, (m_left, m_top), logo)
    except:
        draw.ellipse([m_left, m_top, m_left+125, m_top+125], fill=(255, 0, 127))
        draw.ellipse([m_left, m_top, m_left+110, m_top+110], fill=(255, 0, 127))

    draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
    draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")
    draw.text((m_left + 140, m_top + 5), NOMBRE_PAGINA, font=font_header_bold, fill="black")
    draw.text((m_left + 140, m_top + 55), USUARIO_IG, font=font_header_regular, fill=(120,120,120))

    # 3. CUERPO DE TEXTO (VERSIÓN PRO)
    
    # 🔥 Líneas más cortas (clave visual)
    lineas = textwrap.wrap(frase, width=26)
    
    # Altura base de línea
    bbox_avg = draw.textbbox((0, 0), "Ag", font=font_cuerpo_fino)
    line_h = bbox_avg[3] - bbox_avg[1]
    
    # 🔥 Interlineado PRO
    pad = int(line_h * 0.65)
    # ==========================================
    # 🔥 CUERPO TEXTO (ESTILO EDITORIAL)
    # ==========================================

    # Líneas más largas (tipo párrafo)
    lineas = textwrap.wrap(frase, width=38)

    # Altura de línea
    bbox = draw.textbbox((0, 0), "Ag", font=font_cuerpo)
    line_h = bbox[3] - bbox[1]

    # 🔥 Interlineado más cerrado (como referencia)
    pad = int(line_h * 0.35)

    total_h = (line_h * len(lineas)) + (pad * (len(lineas) - 1))
    
    # 🔥 Área limpia para centrar
    area_top = m_top + 260
    area_bottom = m_bottom - 180

    # Área de texto
    area_top = m_top + 200
    area_bottom = m_bottom - 220
    area_height = area_bottom - area_top

    y_text = area_top + (area_height - total_h) / 2

    # 🔥 Dibujo centrado línea por línea
    # 🔥 Alineado a la izquierda (CLAVE)
    for line in lineas:
        w_line = draw.textlength(line, font=font_cuerpo_fino)
        x_text = m_left + ((m_right - m_left) - w_line) / 2

        draw.text((x_text, y_text), line, font=font_cuerpo_fino, fill=(45, 45, 45))
        draw.text((m_left, y_text), line, font=font_cuerpo, fill=(90, 90, 90))
        y_text += line_h + pad

    # 4. FOOTER
    draw.line([(m_left, 940), (m_right, 940)], fill="lightgray", width=2)
    # FOOTER
    draw.line([(m_left, 920), (m_right, 920)], fill=(220,220,220), width=2)

    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente"
    try:
        font_footer = ImageFont.truetype(nombre_fuente, 32)
        font_footer = ImageFont.truetype(nombre_fuente, 28)
    except:
        font_footer = ImageFont.load_default()

    w_f = draw.textlength(footer_txt, font=font_footer)
    draw.text(((W - w_f) / 2, 970), footer_txt, font=font_footer, fill="gray")
    draw.text(((W - w_f) / 2, 950), footer_txt, font=font_footer, fill=(140,140,140))

    # 5. GUARDADO
    # GUARDADO
    if not os.path.exists('galeria_maqueta'):
        os.makedirs('galeria_maqueta')

    nombre_archivo = f"post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    ruta = os.path.join('galeria_maqueta', nombre_archivo)
    

    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    log("--- 🚀 INICIANDO AGENTE AUTÓNOMO PREMIUM ---")
    log("--- 🚀 INICIANDO AGENTE AUTÓNOMO ---")
    try:
        temas = ["estoicismo", "disciplina", "mentalidad alfa", "hábitos", "psicología"]
        temas = ["estoicismo", "disciplina", "mentalidad", "hábitos", "psicología"]
        tema = random.choice(temas)

        frase = generar_copy_experto(tema)
