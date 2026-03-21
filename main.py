import os
import datetime
import textwrap
import random
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

# CONFIGURACIÓN DE TU MARCA (Monetización)
NOMBRE_PAGINA = "Mente Autónoma"
USUARIO_IG = "@menteautonoma_ai"
COLOR_PRINCIPAL = (255, 0, 127) # Un fucsia vibrante como el de tu ejemplo

def crear_post_premium(frase):
    W, H = (1080, 1080) # Formato cuadrado 1:1 (Muy efectivo en el feed)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        font_bold = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_regular = ImageFont.truetype("Montserrat-Bold.ttf", 40) # Usa la misma si no tienes Regular
        font_texto = ImageFont.truetype("Montserrat-Bold.ttf", 55)
    except:
        font_bold = font_regular = font_texto = ImageFont.load_default()

    # 1. CABECERA (Header)
    # Dibujamos el círculo del logo
    margin = 80
    draw.ellipse([margin, margin, margin+120, margin+120], fill=COLOR_PRINCIPAL)
    # Texto del nombre y usuario
    draw.text((margin+150, margin+15), NOMBRE_PAGINA, font=font_bold, fill="black")
    draw.text((margin+150, margin+70), USUARIO_IG, font=font_regular, fill="gray")

    # 2. CUERPO DE TEXTO (Alineado a la izquierda)
    # Ajustamos el texto para que deje aire a los lados
    lineas = textwrap.wrap(frase, width=35)
    y_text = 350 # Empezamos más arriba para dejar espacio
    
    for line in lineas:
        draw.text((margin, y_text), line, font=font_texto, fill=(40, 40, 40))
        y_text += 80 # Espaciado entre líneas

    # 3. PIE DE PÁGINA (Footer)
    draw.line([(margin, 950), (W-margin, 950)], fill="lightgray", width=2)
    draw.text((margin, 970), f"Sigue a {USUARIO_IG} para más valor", font=font_regular, fill="gray")

    # Guardar
    if not os.path.exists('galeria_maqueta'): os.makedirs('galeria_maqueta')
    ruta = f"galeria_maqueta/post_premium_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.jpg"
    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    log("--- 🚀 INICIANDO MODO MONETIZACIÓN ---")
    try:
        temas = ["psicología del éxito", "hábitos atómicos", "finanzas autónomas"]
        frase = generar_copy_experto(random.choice(temas))
        
        ruta = crear_post_premium(frase)
        log(f"✅ Post Premium creado: {ruta}")
    except Exception as e:
        log(f"❌ ERROR: {e}")

if __name__ == "__main__":
    tarea_diaria()
