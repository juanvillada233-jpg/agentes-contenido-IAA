import os
import datetime
import textwrap
import random
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

# ==========================================
# CONFIGURACIÓN DE TU MARCA
NOMBRE_PAGINA = "Mente Autónoma"
USUARIO_IG = "@menteautonoma_ai"
# ==========================================

def crear_post_final_con_emojis(frase):
    W, H = (1080, 1080)
    img = Image.new('RGB', (W, H), color='white')
    draw = ImageDraw.Draw(img)
    
    # 1. CARGAR FUENTES
    try:
        font_header = ImageFont.truetype("Montserrat-Bold.ttf", 45)
        font_cuerpo = ImageFont.truetype("Montserrat-Regular.ttf", 55)
        # ESTA ES LA CLAVE: Fuente de sistema de GitHub que SÍ tiene emojis
        font_emoji = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
    except:
        font_header = font_cuerpo = font_emoji = ImageFont.load_default()

    margin = int(W * 0.12)

    # 2. CABECERA (Logo y Nombre)
    try:
        logo = Image.open("logo.png").convert("RGBA").resize((120, 120))
        img.paste(logo, (margin, margin), logo)
        draw.text((margin + 150, margin + 15), NOMBRE_PAGINA, font=font_header, fill="black")
        draw.text((margin + 150, margin + 70), USUARIO_IG, font=font_header, fill="gray")
    except:
        # Círculo de respaldo si no hay logo.png
        draw.ellipse([margin, margin, margin+120, margin+120], fill=(255, 0, 127))
        draw.text((margin + 150, margin + 15), NOMBRE_PAGINA, font=font_header, fill="black")

    # 3. CUERPO DE TEXTO (Alineado a la izquierda)
    lineas = textwrap.wrap(frase, width=32)
    y_text = margin + 220
    
    for line in lineas:
        # Dibujamos la línea de texto normal
        draw.text((margin, y_text), line, font=font_cuerpo, fill=(40, 40, 40))
        y_text += 80

    # 4. FOOTER
    draw.line([(margin, 950), (W-margin, 950)], fill="lightgray", width=2)
    footer_txt = f"Sigue a {USUARIO_IG} para potenciar tu mente"
    w_f = draw.textlength(footer_txt, font=font_header) # Ajuste para Pillow moderno
    draw.text(((W-w_f)/2, 970), footer_txt, font=font_header, fill="gray")

    # Guardar
    if not os.path.exists('galeria_maqueta'): os.makedirs('galeria_maqueta')
    ruta = f"galeria_maqueta/post_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.jpg"
    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    print("DEBUG: --- 🤖 INICIANDO MODO PRO ---")
    try:
        frase = generar_copy_experto("estoicismo")
        ruta = crear_post_final_con_emojis(frase)
        print(f"DEBUG: ✅ Post con soporte de emoji creado: {ruta}")
    except Exception as e:
        print(f"DEBUG: ❌ ERROR: {e}")

if __name__ == "__main__":
    tarea_diaria()
