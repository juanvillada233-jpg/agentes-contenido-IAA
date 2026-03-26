import os
import datetime
import textwrap
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

# ==========================================
# CONFIGURACIÓN DE TU MARCA
NOMBRE_PAGINA = "Mente Autónoma"
USUARIO_IG = "@menteautonoma_ai"
# ==========================================

def crear_post_cuadrado_fino(frase):
    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    # 1. CARGAR FUENTES (Asegúrate de tener estos archivos en la raíz de tu GitHub)
    try:
        # Header en Montserrat-Bold para que se vea institucional
        font_header_bold = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 38)
        
        # --- CAMBIO A OPEN SANS ---
        # Usamos el nombre exacto de tu archivo subido
        nombre_fuente_nueva = "OpenSans-VariableFont_wdth,wght.ttf"
        font_cuerpo_fino = ImageFont.truetype(nombre_fuente_nueva, 55) 
        
    except Exception as e:
        log(f"⚠️ Error cargando fuentes: {e}. Revisa que el nombre del archivo sea idéntico.")
        font_header_bold = font_header_regular = font_cuerpo_fino = ImageFont.load_default()

    # MÁRGENES (12%)
    m_left = int(W * 0.12)
    m_right = int(W * 0.88)
    m_top = int(H * 0.12)
    m_bottom = int(H * 0.88)

    # 2. CABECERA (Logo y Texto)
    try:
        logo = Image.open("logo.png").convert("RGBA").resize((125, 125))
        img.paste(logo, (m_left, m_top), logo)
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")
    except:
        draw.ellipse([m_left, m_top, m_left+125, m_top+125], fill=(255, 0, 127))
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")

    # 3. CUERPO DE TEXTO (Ahora con Open Sans)
    # Open Sans es un poco más ancha que Montserrat, bajamos el width a 30 para seguridad
    lineas = textwrap.wrap(frase, width=30)
    
    bbox_avg = draw.textbbox((0, 0), "Abg", font=font_cuerpo_fino)
    single_line_height = bbox_avg[3] - bbox_avg[1]
    total_h = (single_line_height * len(lineas)) + (35 * (len(lineas) - 1))
    
    # Posicionamiento centrado en el área blanca
    y_text = m_top + 280 + (( (m_bottom - 150) - (m_top + 250) - total_h) / 2)
    
    for line in lineas:
        draw.text((m_left, y_text), line, font=font_cuerpo_fino, fill=(45, 45, 45))
        y_text += single_line_height + 35

    # 4. PIE DE PÁGINA (Footer)
    draw.line([(m_left, 940), (m_right, 940)], fill="lightgray", width=2)
    
    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente"
    try:
        font_footer = ImageFont.truetype(nombre_fuente_nueva, 32)
    except:
        font_footer = ImageFont.load_default()

    w_f = draw.textlength(footer_txt, font=font_footer)
    draw.text(((W-w_f)/2, 970), footer_txt, font=font_footer, fill="gray")

    # Guardar
    if not os.path.exists('galeria_maqueta'): os.makedirs('galeria_maqueta')
    ruta = f"galeria_maqueta/post_opensans_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.jpg"
    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    log("--- 🚀 INICIANDO GENERACIÓN CON OPEN SANS ---")
    try:
        frase = generar_copy_experto("mentalidad de acero")
        ruta_archivo = crear_post_cuadrado_fino(frase)
        log(f"✅ ¡Post con Open Sans Creado!: {ruta_archivo}")
    except Exception as e:
        log(f"❌ ERROR: {e}")

if __name__ == "__main__":
    tarea_diaria()
