import os
import sys

print("--- 🤖 PROBANDO UBICACIÓN CORRECTA ---", flush=True)

if __name__ == "__main__":
    print("✅ ¡ÉXITO! Ahora sí estoy en el lugar correcto.", flush=True)
    print(f"Carpeta actual: {os.getcwd()}", flush=True)
    print(f"Archivos aquí: {os.listdir('.')}", flush=True)
