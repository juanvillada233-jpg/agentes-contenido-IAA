import os
import datetime
import textwrap
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

# =========================
# CONFIGURACIÓN
# =========================
NOMBRE_PAGINA = "Mente Autónoma"
USUARIO_IG = "@menteautonoma_ai"

# =========================
# CARGA SEGURA DE FUENTES
# =========================
def cargar_fuente(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        log(f"⚠️ No se encontró {path}, usando default")
        return ImageFont.load_default()

# =========================
# CREAR POST ESTILO PREMIUM
# =========================
def crear_post(frase):

    W, H = 1080, 1080
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)

    # =========================
    # FUENTES (CLAVE DEL ESTILO)
    # =========================
    font_header_bold = cargar_fuente("Montserrat-SemiBold.ttf", 42)
    font_header_regular = cargar_fuente("Montserrat-Regular.ttf", 34)
    font_cuerpo = cargar_fuente("Montserrat-Light.ttf", 46)
    font_footer = cargar_fuente("Montserrat-Regular.ttf", 30)

    # =========================
    # MÁRGENES
    # =========================
    m_left = int(W * 0.12)
    m_top = int(H * 0.12)

    # =========================
    # HEADER (CÍRCULO + TEXTO)
    # =========================
    # Círculo fucsia
    draw.ellipse([m_left, m_top, m_left+110, m_top+110], fill=(255, 0, 120))

    # Textos header
    draw.text((m_left + 140, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill=(0,0,0))
    draw.text((m_left + 140, m_top + 60), USUARIO_IG, font=font_header_regular, fill=(120,120,120))

    # =========================
    # CUERPO TEXTO (ESTILO EDITORIAL)
    # =========================
    # IMPORTANTE: líneas más largas (look editorial)
    lineas = textwrap.wrap(frase, width=38)

    # Métricas
    bbox = draw.textbbox((0,0), "Ag", font=font_cuerpo)
    line_height = bbox[3] - bbox[1]

    # Interlineado sutil
    spacing = int(line_height * 0.35)

    # Posición más arriba (clave visual)
    y_text = m_top + 240

    for line in lineas:
        draw.text(
            (m_left, y_text),
            line,
            font=font_cuerpo,
            fill=(90, 90, 90)  # gris elegante
        )
        y_text += line_height + spacing

    # =========================
    # FOOTER
    # =========================
    y_line = 900
    draw.line([(m_left, y_line), (W - m_left, y_line)], fill=(200,200,200), width=2)

    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente"
    w_f = draw.textlength(footer_txt, font=font_footer)

    draw.text(
        ((W - w_f)/2, y_line + 25),
        footer_txt,
        font=font_footer,
        fill=(150,150,150)
    )

    # =========================
    # GUARDAR
    # =========================
    carpeta = "galeria_posts"
    os.makedirs(carpeta, exist_ok=True)

    nombre = f"post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    ruta = os.path.join(carpeta, nombre)

    img.save(ruta, quality=95)
    return ruta

# =========================
# EJECUCIÓN
# =========================
def tarea():
    log("Generando post estilo premium...")

    frase = generar_copy_experto("reflexión emocional")
    log(f"Frase: {frase}")

    ruta = crear_post(frase)
    log(f"Post creado en: {ruta}")

if __name__ == "__main__":
    tarea()
