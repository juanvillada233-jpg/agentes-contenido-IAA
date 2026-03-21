import os
import sys
from agents.copy_agent import generar_copy_experto

def log(msg):
    # El flush=True es vital para que lo veas en tiempo real en GitHub
    print(f"DEBUG: {msg}", flush=True)

def tarea_diaria():
    log("--- 🤖 INICIANDO AGENTE DE TEXTO (MODO LOG) ---")
    try:
        # 1. Generar la frase
        # Usamos 'resiliencia' como ejemplo, puedes cambiar el tema aquí
        frase = generar_copy_experto("resiliencia")
        
        log("✅ FRASE GENERADA CON ÉXITO:")
        print("\n" + "="*60)
        print(f"{frase}")
        print("="*60 + "\n", flush=True)

    except Exception as e:
        log(f"❌ ERROR EN LA GENERACIÓN: {e}")

if __name__ == "__main__":
    tarea_diaria()
    log("--- 🏁 PROCESO FINALIZADO ---")
