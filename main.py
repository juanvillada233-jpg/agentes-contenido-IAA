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
NOMBRE_PAGINA = "Mente Autónoma"
USUARIO_IG = "@menteautonoma_ai"
# ==========================================

def crear_post_cuadrado_premium(frase):
    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    # FUENTES
    try:
        font_header_bold = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 36)
        
        nombre_fuente = "OpenSans-VariableFont_wdth,wght.ttf"
        font_cuerpo = ImageFont.truetype(nombre_fuente, 36)  # 🔥 más pequeño
        
    except Exception as e:
        log(f"⚠️ Error fuentes: {e}")
        font_header_bold = font_header_regular = font_cuerpo = ImageFont.load_default()

    # MÁRGENES
    m_left = int(W * 0.12)
    m_right = int(W * 0.88)
    m_top = int(H * 0.12)
    m_bottom = int(H * 0.88)

    # CABECERA
    try:
        logo = Image.open("logo.png").convert("RGBA").resize((110, 110))
        img.paste(logo, (m_left, m_top), logo)
    except:
        draw.ellipse([m_left, m_top, m_left+110, m_top+110], fill=(255, 0, 127))

    draw.text((m_left + 140, m_top + 5), NOMBRE_PAGINA, font=font_header_bold, fill="black")
    draw.text((m_left + 140, m_top + 55), USUARIO_IG, font=font_header_regular, fill=(120,120,120))

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

    # Área de texto
    area_top = m_top + 200
    area_bottom = m_bottom - 220
    area_height = area_bottom - area_top

    y_text = area_top + (area_height - total_h) / 2

    # 🔥 Alineado a la izquierda (CLAVE)
    for line in lineas:
        draw.text((m_left, y_text), line, font=font_cuerpo, fill=(90, 90, 90))
        y_text += line_h + pad

    # FOOTER
    draw.line([(m_left, 920), (m_right, 920)], fill=(220,220,220), width=2)
    
    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente"
    try:
        font_footer = ImageFont.truetype(nombre_fuente, 28)
    except:
        font_footer = ImageFont.load_default()

    w_f = draw.textlength(footer_txt, font=font_footer)
    draw.text(((W - w_f) / 2, 950), footer_txt, font=font_footer, fill=(140,140,140))

    # GUARDADO
    if not os.path.exists('galeria_maqueta'):
        os.makedirs('galeria_maqueta')

    nombre_archivo = f"post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    ruta = os.path.join('galeria_maqueta', nombre_archivo)

    img.save(ruta, quality=95)
    return ruta

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