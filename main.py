import os
import datetime
import textwrap
import random
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

# CONFIG
NOMBRE_PAGINA = "Sentir sin Culpa"
USUARIO_IG = "@sentirsingulpa"

# ==============================
# CARGA SEGURA DE FUENTES
# ==============================
def cargar_fuente(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception as e:
        log(f"⚠️ Fuente no encontrada ({path}): {e}")
        return ImageFont.load_default()

# ==============================
# CREAR POST
# ==============================
def crear_post_sentir_sin_culpa_premium(frase):
    
    # Protección por si el texto es muy largo
    if len(frase) > 280:
        frase = frase[:280] + "..."
        log("⚠️ Frase recortada por longitud")

    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)

    # Fuentes
    font_header_bold = cargar_fuente("Montserrat-Bold.ttf", 45)
    font_header_regular = cargar_fuente("Montserrat-Regular.ttf", 38)
    font_cuerpo = cargar_fuente("Montserrat-Regular.ttf", 52)
    font_footer = cargar_fuente("Montserrat-Regular.ttf", 32)

    # Márgenes
    m_left = int(W * 0.12)
    m_top = int(H * 0.12)
    m_bottom = int(H * 0.88)

    # ==============================
    # HEADER (LOGO)
    # ==============================
    try:
        logo = Image.open("logo.png").convert("RGBA")
        logo = logo.resize((125, 125))
        img.paste(logo, (m_left, m_top), logo)
        log("✅ logo cargado")
    except Exception as e:
        log(f"⚠️ Logo no encontrado: {e}")
        draw.ellipse([m_left, m_top, m_left+125, m_top+125], fill=(245,230,220))

    draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
    draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")

    # ==============================
    # CUERPO TEXTO
    # ==============================
    lineas = textwrap.wrap(frase, width=32)

    bbox = draw.textbbox((0, 0), "Ag", font=font_cuerpo)
    line_height = bbox[3] - bbox[1]
    spacing = int(line_height * 0.45)

    total_text_height = (line_height * len(lineas)) + (spacing * (len(lineas) - 1))

    top_text_area = m_top + 280
    bottom_text_area = m_bottom - 150

    available_height = bottom_text_area - top_text_area

    y_text = top_text_area + ((available_height - total_text_height) / 2)

    for line in lineas:
        draw.text((m_left, y_text), line, font=font_cuerpo, fill=(45,45,45))
        y_text += line_height + spacing

    # ==============================
    # FOOTER
    # ==============================
    draw.line([(m_left, 940), (W - m_left, 940)], fill="lightgray", width=2)

    footer_txt = f"Permítete ser humano en {USUARIO_IG}"
    w_f = draw.textlength(footer_txt, font=font_footer)

    draw.text(((W - w_f)/2, 970), footer_txt, font=font_footer, fill="gray")

    # ==============================
    # GUARDAR
    # ==============================
    carpeta = "galeria_posts"
    os.makedirs(carpeta, exist_ok=True)

    nombre = f"post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    ruta = os.path.join(carpeta, nombre)

    img.save(ruta, quality=95)
    return ruta

# ==============================
# TAREA AUTOMÁTICA
# ==============================
def tarea_diaria():
    log("🤖 Iniciando agente...")

    try:
        temas = [
            "culpabilidad por descansar",
            "miedo a decir que no",
            "priorizarse",
            "validación emocional"
        ]

        tema = random.choice(temas)
        log(f"🧠 Tema: {tema}")

        frase = generar_copy_experto(tema)
        log(f"📝 Frase: {frase}")

        ruta = crear_post_sentir_sin_culpa_premium(frase)
        log(f"✅ Post creado: {ruta}")

    except Exception as e:
        log(f"❌ ERROR: {e}")

if __name__ == "__main__":
    tarea_diaria()
