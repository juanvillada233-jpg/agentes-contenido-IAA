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
    # Formato cuadrado 1:1 (1080x1080)
    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    # 1. CARGAR FUENTES (Asegúrate de tener OpenSans-VariableFont_wdth,wght.ttf)
    try:
        font_header_bold = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 38)
        
        # Fuente Open Sans para el cuerpo (Jerarquía Fina)
        nombre_fuente = "OpenSans-VariableFont_wdth,wght.ttf"
        font_cuerpo_fino = ImageFont.truetype(nombre_fuente, 52) 
        
    except Exception as e:
        log(f"⚠️ Error fuentes: {e}. Usando fuente de sistema.")
        font_header_bold = font_header_regular = font_cuerpo_fino = ImageFont.load_default()

    # MÁRGENES (12%)
    m_left = int(W * 0.12)
    m_right = int(W * 0.88)
    m_top = int(H * 0.12)
    m_bottom = int(H * 0.88)

    # 2. CABECERA (Logo y Nombre)
    try:
        logo = Image.open("logo.png").convert("RGBA").resize((125, 125))
        img.paste(logo, (m_left, m_top), logo)
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")
    except:
        draw.ellipse([m_left, m_top, m_left+125, m_top+125], fill=(255, 0, 127))
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")

    # 3. CUERPO DE TEXTO (Con Interlineado Pro)
    lineas = textwrap.wrap(frase, width=32)
    
    bbox_avg = draw.textbbox((0, 0), "Abg", font=font_cuerpo_fino)
    line_h = bbox_avg[3] - bbox_avg[1]
    
    # Ajuste de AIRE (Interlineado del 45%)
    pad = int(line_h * 0.45)
    total_h = (line_h * len(lineas)) + (pad * (len(lineas) - 1))
    
    # Centrado vertical dinámico
    y_text = m_top + 280 + (( (m_bottom - 150) - (m_top + 250) - total_h) / 2)
    
    for line in lineas:
        draw.text((m_left, y_text), line, font=font_cuerpo_fino, fill=(45, 45, 45))
        y_text += line_h + pad

    # 4. PIE DE PÁGINA (Sin desborde)
    draw.line([(m_left, 940), (m_right, 940)], fill="lightgray", width=2)
    
    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente"
    try:
        font_footer = ImageFont.truetype(nombre_fuente, 32)
    except:
        font_footer = ImageFont.load_default()

    w_f = draw.textlength(footer_txt, font=font_footer)
    draw.text(((W-w_f)/2, 970), footer_txt, font=font_footer, fill="gray")

    # 5. GUARDADO CON NOMBRE ÚNICO (Evita el error de Git)
    if not os.path.exists('galeria_maqueta'): os.makedirs('galeria_maqueta')
    # Añadimos segundos (%S) para que cada archivo sea diferente
    nombre_archivo = f"post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    ruta = os.path.join('galeria_maqueta', nombre_archivo)
    
    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    log("--- 🚀 INICIANDO AGENTE AUTÓNOMO PREMIUM ---")
    try:
        # Temas variados para los 50 posts
        temas = ["estoicismo", "disciplina", "mentalidad alfa", "hábitos", "psicología"]
        tema = random.choice(temas)
        
        frase = generar_copy_experto(tema)
        log(f"📝 Frase: {frase}")
        
        ruta = crear_post_cuadrado_premium(frase)
        log(f"✅ Archivo generado: {ruta}")
    except Exception as e:
        log(f"❌ ERROR: {e}")

if __name__ == "__main__":
    tarea_diaria()
