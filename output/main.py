import os
import sys
import json
import datetime

# CONFIGURACIÓN DE IMPRESIÓN FORZADA
def log(texto):
    print(f"DEBUG_LOG: {texto}", flush=True)

log("Iniciando motor del Agente...")

try:
    from agents.copy_agent import generar_copy_experto
    log("✅ Carpeta 'agents' detectada correctamente")
except Exception as e:
    log(f"❌ ERROR: No se encuentra la carpeta 'agents' o el archivo 'copy_agent.py': {e}")
    sys.exit(1)

def tarea_diaria():
    try:
        log("Solicitando frase a Groq...")
        frase = generar_copy_experto("resiliencia")
        
        print("\n" + "="*50)
        print(f"📝 RESULTADO FINAL:\n{frase}")
        print("="*50 + "\n", flush=True)
        
        # Aquí es donde el código se detiene si el Drive falla, 
        # pero al menos ya viste la frase arriba.
        log("Intentando guardar en Drive (Paso crítico)...")
        # (Aquí iría tu función de subida que ya tenemos)
        
    except Exception as e:
        log(f"❌ FALLO EN LA TAREA: {e}")

if __name__ == "__main__":
    tarea_diaria()
