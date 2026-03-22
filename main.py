import os
import datetime
import textwrap
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

# ==========================================
# CONFIGURACIÓN DE TU MARCA (Monetización)
NOMBRE_PAGINA = "Mente Autónoma"
USUARIO_IG = "@menteautonoma_ai"
# ==========================================

def crear_post_916_premium(frase):
    # Formato vertical 9:16 (Reels/Stories) - 1080x1920
    W, H = (1080, 1920)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    # 1. CARGAR FUENTES (Mismo nombre, diferente grosor)
    try:
        # Bold para títulos y Regular para el cuerpo (toque fino)
        font_header_bold = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 38)
        font_cuerpo_regular = ImageFont.truetype("Montserrat-Regular.ttf", 55) # <--- FUENTE FINA
    except Exception as e:
        log(f"⚠️ Error cargando fuentes (.ttf). Asegúrate de subir Montserrat-Regular.ttf y Montserrat-Bold.ttf. Error: {e}")
        font_header_bold = font_header_regular = font_cuerpo_regular = ImageFont.load_default()

    # MÁRGENES DE SEGURIDAD PROFESIONALES (12% de cada borde)
    m_left = int(W * 0.12)
    m_right = int(W * 0.88)
    m_top = int(H * 0.10) # Un poco más de aire arriba
    m_bottom = int(H * 0.90)

    # 2. CABECERA (Logo y Nombre de Marca)
    try:
        # Cargamos tu archivo 'logo.png'
        logo = Image.open("logo.png").convert("RGBA")
        # Redimensionamos el logo (ejemplo: 140x140px)
        logo = logo.resize((140, 140))
        # Lo pegamos
        img.paste(logo, (m_left, m_top), logo)
        
        # Texto del nombre (Bold) y usuario (Regular) - ¡CORREGIDO ABAJO!
        draw.text((m_left + 170, m_top + 15), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 170, m_top + 75), USUARIO_IG, font=font_header_regular, fill="gray")
        
    except Exception as e:
        log(f"⚠️ No se encontró 'logo.png' o hubo un error. Usando respaldo básico. Error: {e}")
        draw.text((m_left, m_top), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left, m_top + 60), USUARIO_IG, font=font_header_regular, fill="gray")

    # 3. CUERPO DE TEXTO (Frase con fuente fina)
    # textwrap ajusta para que no se corte el texto
    # width=35 es un buen ancho para Montserrat-Regular a 55px
    lineas = textwrap.wrap(frase, width=35)
    
    # Posicionamiento vertical (empezamos más abajo del header)
    # y_text = m_top + 350
    # Obtenemos la altura promedio de la fuente para centrar verticalmente
    bbox_avg = draw.textbbox((0, 0), "Abg", font=font_cuerpo_regular)
    single_line_height = bbox_avg[3] - bbox_avg[1]
    
    # Calcular alto total del bloque de texto
    total_h = (single_line_height * len(lineas)) + (30 * (len(lineas) - 1)) # pad=30px
    
    # Centramos verticalmente en el área disponible (bajo el header hasta el footer)
    area_h = m_bottom - (m_top + 350) # Espacio disponible
    y_text = m_top + 350 + ((area_h - total_h) / 2) # Centrado vertical dinámico
    
    for line in lineas:
        # draw.text((X_izq, Y_texto), ...)
        draw.text((m_left, y_text), line, font=font_cuerpo_regular, fill=(40, 40, 40))
        y_text += single_line_height + 30 # Espaciado entre líneas

    # 4. PIE DE PÁGINA (Footer Minimalista)
    log("🎨 Diseñando footer sin desborde...")
    
    # Línea divisoria suave
    draw.line([(m_left, m_bottom - 100), (m_right, m_bottom - 100)], fill="lightgray", width=2)
    
    # Texto del footer (más pequeño y centrado para que no se corte)
    try:
        font_footer = ImageFont.truetype("Montserrat-Regular.ttf", 35)
    except:
        font_footer = ImageFont.load_default()
        
    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente autónoma"
    
    # Calcular ancho para centrar
    bbox_f = draw.textbbox((0, 0), footer_txt, font=font_footer)
    w_f = bbox_f[2] - bbox_f[0]
    
    # draw.text(((W-w_f)/2, H_footer), ...)
    draw.text(((W-w_f)/2, m_bottom - 70), footer_txt, font=font_footer, fill="gray")

    # Guardar localmente
    if not os.path.exists('galeria_maqueta'): os.makedirs('galeria_maqueta')
    ruta = f"galeria_maqueta/post_916_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.jpg"
    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    log("--- 🚀 INICIANDO MODO MONETIZACIÓN 9:16 ---")
    try:
        # Aquí puedes cambiar el tema constantemente después
        frase = generar_copy_experto("resiliencia")
        log(f"📝 Frase Groq: {frase}")
        
        ruta_archivo = crear_post_916_premium(frase)
        log(f"✅ Post 9:16 Profesional creado: {ruta_archivo}")
    except Exception as e:
        log(f"❌ ERROR CRÍTICO: {e}")

if __name__ == "__main__":
    tarea_diaria()
