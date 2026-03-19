import os
import datetime
from agents.copy_agent import generar_copy_experto

def tarea_diaria():
    # Temas basados en el entrenamiento de 500k seguidores
    # Puedes cambiar "resiliencia" por "fe" o "autoestima"
    tema_de_hoy = "resiliencia" 
    
    print(f"--- Iniciando generación de: {tema_de_hoy} ---")
    
    try:
        # 1. El agente genera la frase con técnica de ingeniería inversa
        frase_final = generar_copy_experto(tema_de_hoy)
        
        # 2. Creamos la carpeta output si no existe
        if not os.path.exists('output'):
            os.makedirs('output')
        
        # 3. Guardamos la frase en un archivo con la fecha
        fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        ruta_archivo = f"output/frase_{fecha}.txt"
        
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write(frase_final)
            
        print(f"✅ ÉXITO: Frase guardada en {ruta_archivo}")
        print(f"Contenido: {frase_final}")

        # --- AQUÍ SIGUE TU LÓGICA DE GOOGLE DRIVE ---
        # Asegúrate de pasar 'frase_final' a tu función de subida a Drive
        
    except Exception as e:
        print(f"❌ ERROR en el flujo: {e}")

if __name__ == "__main__":
    tarea_diaria()
