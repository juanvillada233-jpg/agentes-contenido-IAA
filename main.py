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
    # Formato cuadrado 1:1 para Facebook e Instagram Feed
    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    # 1. CARGAR FUENTES (Asegúrate de tener Montserrat-Regular.ttf en el repo)
    try:
        font_header_bold = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 38)
        # Usamos Regular aquí para que se vea fino como el ejemplo que te gustó
        font_cuerpo_regular = ImageFont.truetype("Montserrat-Regular.ttf", 55) 
    except Exception as e:
        log(f"⚠️ Error fuentes: {e}")
        font_header_bold = font_header_regular = font_cuerpo_regular = ImageFont.load_default()

    # MÁRGENES DE SEGURIDAD (12% de cada borde)
    m_left = int(W * 0.12)
    m_right = int(W * 0.88)
    m_top = int(H * 0.12)
    m_bottom = int(H * 0.88)

    # 2. CABECERA (Logo y Nombres apilados)
    try:
        logo = Image.open("logo.png").convert("RGBA")
        logo = logo.resize((125, 125))
        img.paste(logo, (m_left, m_top), logo)
        
        # Nombre en negrita y usuario justo debajo en gris
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")
    except:
        # Círculo fucsia si no hay logo.png
        draw.ellipse([m_left, m_top, m_left+125, m_top+125], fill=(255, 0, 127))
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")

    # 3. CUERPO DE TEXTO (Frase fina a la izquierda)
    # Ajustamos el ancho para Montserrat-Regular
    lineas = textwrap.wrap(frase, width=32)
    
    # Calculamos altura para centrar verticalmente en el área disponible
    bbox_avg = draw.textbbox((0, 0), "Abg", font=font_cuerpo_regular)
    single_line_height = bbox_avg[3] - bbox_avg[1]
    total_h = (single_line_height * len(lineas)) + (30 * (len(lineas) - 1))
    
    # Posicionamos el texto
    y_text = m_top + 250 + (( (m_bottom - 150) - (m_top + 250) - total_h) / 2)
    
    for line in lineas:
        draw.text((m_left, y_text), line, font=font_cuerpo_regular, fill=(40, 40, 40))
        y_text += single_line_height + 30

    # 4. PIE DE PÁGINA (Footer sin desborde)
    draw.line([(m_left, 940), (m_right, 940)], fill="lightgray", width=2)
    
    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente"
    # Usamos una fuente más pequeña para el footer
    try:
        font_footer = ImageFont.truetype("Montserrat-Regular.ttf", 32)
    except:
        font_footer = ImageFont.load_default()

    bbox_f = draw.textbbox((0, 0), footer_txt, font=font_footer)
    w_f = bbox_f[2] - bbox_f[0]
    
    # Centrado horizontal en el pie
    draw.text(((W-w_f)/2, 970), footer_txt, font=font_footer, fill="gray")

    # Guardar
    if not os.path.exists('galeria_maqueta'): os.makedirs('galeria_maqueta')
    ruta = f"galeria_maqueta/post_fb_ig_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.jpg"
    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    log("--- 🚀 GENERANDO CONTENIDO CUADRADO PREMIUM ---")
    try:
        # Aquí es donde el prompt hará su magia
        frase = generar_copy_experto("resiliencia")
        ruta_archivo = crear_post_cuadrado_fino(frase)
        log(f"✅ Post Finalizado: {ruta_archivo}")
    except Exception as e:
        log(f"❌ ERROR: {e}")

if __name__ == "__main__":
    tarea_diaria()
