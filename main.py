import os
import datetime
import textwrap
from PIL import Image, ImageDraw, ImageFont
from agents.copy_agent import generar_copy_experto

def log(msg):
    print(f"DEBUG: {msg}", flush=True)

def crear_imagen_pro(texto, nombre_empresa="@TuCliente"):
    W, H = (1080, 1350) # Formato Portrait Instagram
    img = Image.new('RGB', (W, H), color='black')
    draw = ImageDraw.Draw(img)
    
    # Intentar cargar la fuente elegante
    try:
        font_principal = ImageFont.truetype("Montserrat-Bold.ttf", 90)
        font_marca = ImageFont.truetype("Montserrat-Bold.ttf", 40)
    except:
        font_principal = ImageFont.load_default()
        font_marca = ImageFont.load_default()

    # Ajustar el texto para que no se salga de la imagen
    lineas = textwrap.wrap(texto, width=22) 
    
    # Dibujar la frase centrada
    y_text = (H / 2) - (50 * len(lineas))
    for line in lineas:
        w, h = draw.textsize(line, font=font_principal)
        draw.text(((W - w) / 2, y_text), line, font=font_principal, fill="white")
        y_text += h + 20

    # Dibujar la marca de agua abajo (El toque profesional)
    w_m, h_m = draw.textsize(nombre_empresa, font=font_marca)
    draw.text(((W - w_m) / 2, H - 150), nombre_empresa, font=font_marca, fill="gray")

    # Guardar localmente
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
