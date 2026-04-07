import os
import datetime
import textwrap
import random
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

# ==========================================
# CONFIGURACIÓN DE TU MARCA
NOMBRE_PAGINA = "Sentir sin Culpa"
USUARIO_IG = "@sentirsinulpa"
# ==========================================

def crear_post_cuadrado_premium(frase):
    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    # ==========================
    # FUENTES (CLAVE)
    # ==========================
    try:
        font_header_bold = ImageFont.truetype("Montserrat-Bold.ttf", 48)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 34)
        font_cuerpo = ImageFont.truetype("Montserrat-Regular.ttf", 34)
        font_footer = ImageFont.truetype("Montserrat-Regular.ttf", 28)
    except Exception as e:
        log(f"⚠️ Error fuentes: {e}")
        font_header_bold = font_header_regular = font_cuerpo = font_footer = ImageFont.load_default()

    # ==========================
    # MÁRGENES
    # ==========================
    m_left = int(W * 0.12)
    m_right = int(W * 0.88)
    m_top = int(H * 0.12)
    m_bottom = int(H * 0.88)

    # ==========================
    # LOGO (MISMO TAMAÑO QUE REFERENCIA)
    # ==========================
    try:
        logo = Image.open("logo.png").convert("RGBA").resize((130, 130))
        img.paste(logo, (m_left, m_top), logo)
    except:
        draw.ellipse([m_left, m_top, m_left+130, m_top+130], fill=(255, 0, 127))

    # ==========================
    # HEADER
    # ==========================
    draw.text((m_left + 150, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
    draw.text((m_left + 150, m_top + 65), USUARIO_IG, font=font_header_regular, fill=(130,130,130))

    # ==========================
    # CUERPO TEXTO (ESTILO EDITORIAL EXACTO)
    # ==========================
    lineas = textwrap.wrap(frase, width=42)

    bbox = draw.textbbox((0, 0), "Ag", font=font_cuerpo)
    line_h = bbox[3] - bbox[1]

    pad = int(line_h * 0.25)

    total_h = (line_h * len(lineas)) + (pad * (len(lineas) - 1))

    # POSICIÓN CORRECTA (más arriba como referencia)
    area_top = m_top + 180
    area_bottom = m_bottom - 260
    area_height = area_bottom - area_top

    y_text = area_top + (area_height - total_h) / 2

    for line in lineas:
        draw.text((m_left, y_text), line, font=font_cuerpo, fill=(85, 85, 85))
        y_text += line_h + pad

    # ==========================
    # FOOTER
    # ==========================
    draw.line([(m_left, 920), (m_right, 920)], fill=(220,220,220), width=2)

    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente"
    w_f = draw.textlength(footer_txt, font=font_footer)
    draw.text(((W - w_f) / 2, 950), footer_txt, font=font_footer, fill=(140,140,140))

    # ==========================
    # GUARDADO
    # ==========================
    if not os.path.exists('galeria_maqueta'):
        os.makedirs('galeria_maqueta')

    nombre_archivo = f"post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    ruta = os.path.join('galeria_maqueta', nombre_archivo)

    img.save(ruta, quality=95)
    return ruta

# ==========================
# AGENTE AUTOMÁTICO
# ==========================
def tarea_diaria():
    log("--- 🚀 INICIANDO AGENTE AUTÓNOMO ---")
    try:
        temas = ["estoicismo", "disciplina", "mentalidad", "hábitos", "psicología"]
        tema = random.choice(temas)
        
        frase = generar_copy_experto(tema)
        log(f"📝 Frase: {frase}")
        
        ruta = crear_post_cuadrado_premium(frase)
        log(f"✅ Archivo generado: {ruta}")
    except Exception as e:
        log(f"❌ ERROR: {e}")

if __name__ == "__main__":
    tarea_diaria()
