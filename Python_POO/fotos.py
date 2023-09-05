import os

# Ruta al directorio donde se encuentran los archivos JPG
directorio = "/home/dac/Desktop/Road to Spain/Holliday/for_me"

# Recorre los archivos en el directorio
for nombre_archivo in os.listdir(directorio):
    if nombre_archivo.endswith(".jpg") and nombre_archivo.startswith("IMG-"):
        # Obtiene el año del nombre del archivo
        ano = nombre_archivo[4:19]
        
        # Nuevo nombre del archivo
        nuevo_nombre = ano + ".jpg"
        
        # Ruta completa del archivo original y nuevo
        ruta_original = os.path.join(directorio, nombre_archivo)
        ruta_nuevo = os.path.join(directorio, nuevo_nombre)
        
        # Renombra el archivo
        os.rename(ruta_original, ruta_nuevo)
        print(f"Archivo renombrado: {ruta_original} -> {ruta_nuevo}")
        print("hello world")