import pandas as pd
import wget
from libreria import *

##Creamos carpetas para clasificar los archivos descargados.
DiaOperando=r'C:\Users\edivi\Documents\PROGRAMACION2\CONAGUA\Catalogo\Diario/Operando1'
crearCarpeta(DiaOperando)
DiaSuspendido=r'C:\Users\edivi\Documents\PROGRAMACION2\CONAGUA\Catalogo\Diario/Suspendido1'
crearCarpeta(DiaSuspendido)
Mensual=r'C:\Users\edivi\Documents\PROGRAMACION2\CONAGUA\Catalogo\Mensual'
crearCarpeta(Mensual)

rutaArchivo1=r'C:\Users\edivi\Documents\PROGRAMACION2\CONAGUA\Catalogo'
extension1='.xlsx'
archivosExcel=leerArchivo(rutaArchivo1, extension1)
print(archivosExcel)

for excel in archivosExcel:
    print(rutaArchivo1 + '\\' + excel)
    estacion=pd.read_excel(rutaArchivo1 +'\\'+ excel)

    urlLista=[]

    ##print(estacion["ABREV."]) ##Solo imprime la columna con dicha clave
    urlBase='https://smn.conagua.gob.mx/tools/RESOURCES/Normales_Climatologicas/Diarios'

    ##def descargar(estacion):
    for i in range(0,len(estacion)):
        nombreArchivo= 'dia'+ str(estacion.Clave[i]).zfill(5) +'.txt' ##Guardabos en una variable el nombre del archivo
        urlBuscar=urlBase+'/'+ estacion.ABREV[i] + '/' + nombreArchivo
        print(estacion.Clave[i], estacion.ABREV[i]) ## Imprime todas las claves de la columna ABRV.
        urlLista.append(urlBuscar)
        print(urlBuscar)
        try:
            if estacion.Situación[i]=="Operando":
                wget.download(urlBuscar, out=DiaOperando)
                ##Abrimos el archivo y lo leemos para extraer la fecha
            else:
                wget.download(urlBuscar, out=DiaSuspendido)
        except Exception as e:
            print("No se pudo descargar el archivo: ", str(e))

##descargar(estacion)
