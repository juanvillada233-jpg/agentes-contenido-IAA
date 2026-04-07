import os
import datetime
import textwrap
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

# =========================
# CONFIG
# =========================
NOMBRE_PAGINA = "Sentir sin Culpa"
USUARIO_IG = "@sentirsingulpa"

# =========================
# FUENTES
# =========================
def cargar_fuente(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        log(f"⚠️ No se encontró {path}")
        return ImageFont.load_default()

# =========================
# POST PREMIUM BIEN ESCALADO
# =========================
def crear_post(frase):

    W, H = 1080, 1080
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)

    # =========================
    # FUENTES (AUMENTADAS)
    # =========================
    font_header_bold = cargar_fuente("Montserrat-SemiBold.ttf", 52)
    font_header_regular = cargar_fuente("Montserrat-Regular.ttf", 40)
    font_cuerpo = cargar_fuente("Montserrat-Light.ttf", 58)
    font_footer = cargar_fuente("Montserrat-Regular.ttf", 36)

    # =========================
    # MÁRGENES
    # =========================
    m_left = int(W * 0.12)
    m_top = int(H * 0.12)

    # =========================
    # HEADER
    # =========================
    draw.ellipse([m_left, m_top, m_left+130, m_top+130], fill=(255, 0, 120))

    draw.text((m_left + 160, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill=(0,0,0))
    draw.text((m_left + 160, m_top + 70), USUARIO_IG, font=font_header_regular, fill=(120,120,120))

    # =========================
    # TEXTO (CORREGIDO)
    # =========================
    lineas = textwrap.wrap(frase, width=32)  # 🔥 clave para tamaño correcto

    bbox = draw.textbbox((0,0), "Ag", font=font_cuerpo)
    line_height = bbox[3] - bbox[1]

    spacing = int(line_height * 0.40)

    # MÁS ARRIBA PERO BIEN DISTRIBUIDO
    y_text = m_top + 320

    for line in lineas:
        draw.text(
            (m_left, y_text),
            line,
            font=font_cuerpo,
            fill=(80, 80, 80)  # gris premium
        )
        y_text += line_height + spacing

    # =========================
    # FOOTER
    # =========================
    y_line = 900
    draw.line([(m_left, y_line), (W - m_left, y_line)], fill=(200,200,200), width=2)

    footer_txt = f"Permítete ser humano en {USUARIO_IG}"
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
    log("Generando post premium...")

    frase = generar_copy_experto("reflexión emocional")
    log(frase)

    ruta = crear_post(frase)
    log(f"Post creado: {ruta}")

if __name__ == "__main__":
    tarea()
