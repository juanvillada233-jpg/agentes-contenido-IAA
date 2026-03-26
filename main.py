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

def crear_post_cuadrado_ premium(frase):
    # Formato cuadrado 1:1 para Feed (FB/IG)
    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    # 1. CARGAR FUENTES (Asegúrate de tener estos archivos .ttf)
    try:
        # Bold para título de marca, Regular/Light para el cuerpo
        font_header_bold = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 38)
        
        # --- AJUSTE DE JERARQUÍA 1: TAMAÑO DE FUENTE ---
        # Reducimos de 55/60px a 52px para un look más fino
        font_cuerpo_ligero = ImageFont.truetype("Montserrat-Regular.ttf", 52) 
        
    except Exception as e:
        log(f"⚠️ Error cargando fuentes (.ttf): {e}. Asegúrate de subirlas al repo.")
        font_header_bold = font_header_regular = font_cuerpo_ligero = ImageFont.load_default()

    # MÁRGENES DE SEGURIDAD (12% para un look de marca caro)
    m_left = int(W * 0.12)
    m_right = int(W * 0.88)
    m_top = int(H * 0.12)
    m_bottom = int(H * 0.88)

    # 2. CABECERA (Header Institucional)
    try:
        # Cargamos el logo
        logo = Image.open("logo.png").convert("RGBA")
        logo = logo.resize((125, 125)) # Tamaño sutil
        img.paste(logo, (m_left, m_top), logo)
        
        # Texto del nombre y usuario a la derecha del logo
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")
    except:
        # Círculo de respaldo fucsia
        COLOR_FUCSIA = (255, 0, 127)
        draw.ellipse([m_left, m_top, m_left+125, m_top+125], fill=COLOR_FUCSIA)
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")

    # 3. CUERPO DE TEXTO (Frase alineada a la izquierda)
    # textwrap ajusta para que no se corte el texto. 
    # Un ancho de 35 es bueno para que no sean líneas muy largas.
    lineas = textwrap.wrap(frase, width=35)
    
    # --- AJUSTE DE JERARQUÍA 2: INTERLINEADO ---
    # Obtenemos la altura promedio de la fuente
    bbox_avg = draw.textbbox((0, 0), "Abg", font=font_cuerpo_ligero)
    single_line_height = bbox_avg[3] - bbox_avg[1]
    
    # Calculamos el interlineado (aire entre líneas).
    # Un 45% del alto de línea es un valor profesional.
    pad_interlineado = int(single_line_height * 0.45) # 45% de espacio extra
    
    # Calculamos el alto total para centrarlo
    total_h = (single_line_height * len(lineas)) + (pad_interlineado * (len(lineas) - 1))
    
    # Posicionar texto (centrado verticalmente en el área útil bajo el header)
    # y_text_start = Área útil bajo el header (aprox m_top + 250)
    # y_text_end = m_bottom - 150 (aire arriba del footer)
    
    area_h = (m_bottom - 150) - (m_top + 250) # Espacio disponible
    y_text = m_top + 250 + ((area_h - total_h) / 2) # Centrado vertical dinámico
    
    # Dibujar líneas con aire
    for line in lineas:
        draw.text((m_left, y_text), line, font=font_cuerpo_ligero, fill=(40, 40, 40))
        y_text += single_line_height + pad_interlineado # SUMAMOS EL INTERLINEADO AQUÍ

    # 4. PIE DE PÁGINA (Footer Minimalista)
    # Línea divisoria suave
    draw.line([(m_left, 940), (m_right, 940)], fill="lightgray", width=2)
    
    # Texto del footer centrado
    try:
        font_footer = ImageFont.truetype("Montserrat-Regular.ttf", 32) # Letra más pequeña
    except:
        font_footer = ImageFont.load_default()
        
    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente autónoma"
    
    # Calcular ancho para centrar
    bbox_f = draw.textbbox((0, 0), footer_txt, font=font_footer)
    w_f = bbox_f[2] - bbox_f[0]
    
    # draw.text(((W-w_f)/2, Y_footer), ...)
    draw.text(((W-w_f)/2, 970), footer_txt, font=font_footer, fill="gray")

    # Guardar localmente
    if not os.path.exists('galeria_maqueta'): os.makedirs('galeria_maqueta')
    ruta = f"galeria_maqueta/post_prem_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.jpg"
    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    log("--- 🚀 INICIANDO GENERACIÓN PREMIUM CON JERARQUÍA ---")
    try:
        from agents.copy_agent import generar_copy_experto
        frase = generar_copy_experto("estoicismo") # Ejemplo de tema
        log(f"📝 Frase Groq: {frase}")
        
        ruta_archivo = crear_post_cuadrado_premium(frase)
        log(f"✅ ¡Post con Jerarquía Creado!: {ruta_archivo}")
    except Exception as e:
        log(f"❌ ERROR: {e}")

if __name__ == "__main__":
    tarea_diaria()
