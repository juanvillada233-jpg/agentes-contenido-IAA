import os
import datetime
import textwrap
import random
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

# ==========================================
# CONFIGURACIÓN DE TU NUEVA MARCA (¡ÉXITO!)
# Cámbialo si decides otro nombre final
NOMBRE_PAGINA = "Sentir sin Culpa"
USUARIO_IG = "@sentirsingulpa" # Revisa disponibilidad en FB/IG
# ==========================================

def crear_post_sentir_sin_culpa_premium(frase):
    # Formato cuadrado 1:1 (1080x1080)
    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    # 1. CARGAR FUENTES (Asegúrate de tener estos archivos .ttf)
    try:
        # Bold para título de marca, Regular para el cuerpo
        font_header_bold = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_header_regular = ImageFont.truetype("Montserrat-Regular.ttf", 38)
        
        # --- AJUSTE DE JERARQUÍA FINA ---
        # Usamos Open Sans Regular para un look más fino y legible
        font_cuerpo_ligero = ImageFont.truetype("OpenSans-Regular.ttf", 52) 
        
    except Exception as e:
        log(f"⚠️ Error fuentes: {e}. Asegúrate de subirlas al repo.")
        font_header_bold = font_header_regular = font_cuerpo_ligero = ImageFont.load_default()

    # MÁRGENES DE SEGURIDAD (12% para elegancia premium)
    m_left = int(W * 0.12)
    m_right = int(W * 0.88)
    m_top = int(H * 0.12)
    m_bottom = int(H * 0.88)

    # 2. CABECERA (Header Institucional con Nuevo Logo)
    try:
        # Cargamos el logo de "Abrazo Minimalista" (subido como logo.png transparente)
        # El tamaño 125x125 es sutil y mantiene la jerarquía
        logo = Image.open("logo.png").convert("RGBA").resize((125, 125)) 
        img.paste(logo, (m_left, m_top), logo)
        
        # Texto del nombre y usuario a la derecha del logo
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")
    except Exception as e:
        log(f"⚠️ No se pudo cargar logo.png: {e}. Usando respaldo.")
        # Círculo de respaldo beige suave si no hay logo.png
        COLOR_BEIGE_PASTEL = (245, 230, 220) 
        draw.ellipse([m_left, m_top, m_left+125, m_top+125], fill=COLOR_BEIGE_PASTEL)
        draw.text((m_left + 155, m_top + 10), NOMBRE_PAGINA, font=font_header_bold, fill="black")
        draw.text((m_left + 155, m_top + 70), USUARIO_IG, font=font_header_regular, fill="gray")

    # 3. CUERPO DE TEXTO (Frase alineada a la izquierda con Interlineado)
    lineas = textwrap.wrap(frase, width=32)
    
    bbox_avg = draw.textbbox((0, 0), "Abg", font=font_cuerpo_ligero)
    single_line_height = bbox_avg[3] - bbox_avg[1]
    
    # Interlineado profesional (45% de espacio extra)
    pad_interlineado = int(single_line_height * 0.45) 
    
    # Calculamos el alto total
    total_h = (single_line_height * len(lineas)) + (pad_interlineado * (len(lineas) - 1))
    
    # Posicionar texto (centrado verticalmente bajo el header)
    area_h = (m_bottom - 150) - (m_top + 280) # Dejamos espacio para el header
    y_text = m_top + 280 + ((area_h - total_h) / 2) # Centrado vertical dinámico
    
    for line in lineas:
        # Color gris oscuro para no competir con el header negro
        draw.text((m_left, y_text), line, font=font_cuerpo_ligero, fill=(45, 45, 45))
        y_text += single_line_height + pad_interlineado

    # 4. PIE DE PÁGINA (Footer Minimalista)
    draw.line([(m_left, 940), (m_right, 940)], fill="lightgray", width=2)
    
    try:
        # Fuente más pequeña para el footer
        font_footer = ImageFont.truetype("OpenSans-Regular.ttf", 32)
    except:
        font_footer = ImageFont.load_default()
        
    footer_txt = f"Permítete ser humano en {USUARIO_IG}"
    
    # Calcular ancho para centrar
    w_f = draw.textlength(footer_txt, font=font_footer)
    draw.text(((W-w_f)/2, 970), footer_txt, font=font_footer, fill="gray")

    # 5. GUARDADO CON NOMBRE ÚNICO (Anti-Errores de Git)
    if not os.path.exists('galeria_posts'): os.makedirs('galeria_posts')
    # Añadimos segundos (%S) para asegurar unicidad
    nombre_archivo = f"post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    ruta = os.path.join('galeria_posts', nombre_archivo)
    
    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    log("--- 🤖 INICIANDO AGENTE DE SENTIR SIN CULPA ---")
    try:
        from agents.copy_agent import generar_copy_experto
        # Groq elegirá un tema relacionado con la culpa y validación
        temas = ["culpabilidad por descansar", "miedo a decir que no", "priorizarse", "validación emocional"]
        tema_elegido = random.choice(temas)
        log(f"🧠 Tema elegido: {tema_elegido}")
        
        frase = generar_copy_experto(tema_elegido)
        log(f"📝 Frase Groq: {frase}")
        
        ruta_archivo = crear_post_sentir_sin_culpa_premium(frase)
        log(f"✅ ¡Post con Identidad Creado!: {ruta_archivo}")
    except Exception as e:
        log(f"❌ ERROR CRÍTICO: {e}")

if __name__ == "__main__":
    tarea_diaria()
