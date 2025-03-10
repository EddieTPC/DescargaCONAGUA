import os

##Variables globales
##Crea carpetas
def crearCarpeta(carpeta):
    try:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"Carpeta '{carpeta}' creada exitosamente")
    except Exception as e:
      print(f"Error: {str(e)}")

def leerArchivo(rutaArchivo, extension):
    with os.scandir(rutaArchivo) as archivos:
        archivos=[archivo.name for archivo in archivos
            if archivo.is_file() and archivo.name.endswith(extension)]
    return archivos

""" def archivoExiste(rutaArchivo):
    if os.path.isfile(rutaArchivo):
        return True """