import os
import datetime
import textwrap
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

def crear_imagen_pro(texto, nombre_empresa="@TuCliente"):
    W, H = (1080, 1350)
    img = Image.new('RGB', (W, H), color='black')
    draw = ImageDraw.Draw(img)
    
    try:
        font_principal = ImageFont.truetype("Montserrat-Bold.ttf", 90)
        font_marca = ImageFont.truetype("Montserrat-Bold.ttf", 40)
    except:
        font_principal = ImageFont.load_default()
        font_marca = ImageFont.load_default()

    lineas = textwrap.wrap(texto, width=22) 
    
    # --- CAMBIO AQUÍ PARA EVITAR EL ERROR 'textsize' ---
    # Calculamos el alto total del bloque de texto
    line_heights = [draw.textbbox((0, 0), line, font=font_principal)[3] for line in lineas]
    total_text_height = sum(line_heights) + (20 * (len(lineas) - 1))
    
    y_text = (H - total_text_height) / 2
    
    for line in lineas:
        # Usamos textbbox para centrar horizontalmente
        bbox = draw.textbbox((0, 0), line, font=font_principal)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        draw.text(((W - w) / 2, y_text), line, font=font_principal, fill="white")
        y_text += h + 25 # Espaciado entre líneas

    # Marca de agua corregida también
    bbox_m = draw.textbbox((0, 0), nombre_empresa, font=font_marca)
    w_m = bbox_m[2] - bbox_m[0]
    draw.text(((W - w_m) / 2, H - 150), nombre_empresa, font=font_marca, fill="gray")
    # ---------------------------------------------------

    if not os.path.exists('galeria_maqueta'): os.makedirs('galeria_maqueta')
    ruta = f"galeria_maqueta/post_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.jpg"
    img.save(ruta, quality=95)
    return ruta

def tarea_diaria():
    log("--- 🤖 AGENTE DE CONTENIDO INICIANDO ---")
    try:
        frase = generar_copy_experto("resiliencia")
        log(f"📝 Frase generada: {frase}")
        
        ruta_archivo = crear_imagen_pro(frase)
        log(f"✅ Imagen creada con éxito en: {ruta_archivo}")
    except Exception as e:
        log(f"❌ ERROR: {e}")

if __name__ == "__main__":
    tarea_diaria()
