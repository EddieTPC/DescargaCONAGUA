from libreria import *
import pandas as pd

CarpetaDatos = 'C:/Users/edivi/Documents/PROGRAMACION2/CONAGUA/Catalogo/Diario/Salida/'
crearCarpeta(CarpetaDatos)

Emision = []
Estacion = []
Nombre = []
Estado = []
Municipio = []
Situacion = []
CveOMM = []
Latitud = []
Longitud = []
Altitud = []
Fecha_Ini = []
Fecha_Fin = []
Anno_Inicio = []
Anno_Fin = []
######################################3
FechaDatos=[]
Precipitacion=[]
Evaporacion=[]
TemperaturaMax=[]
TemperaturaMin=[]
def extraerInformacion(nombresArchivos, rutaCarpeta):
    for archi in nombresArchivos:
        mi_archivo = open(rutaCarpeta + '\\' + archi, "r", encoding= 'utf-8', errors= None)
        #En la variable Archivo lineas vamos a recuperar el mi archivo por líneas
        Archivo_lineas=mi_archivo.readlines ()
        # Número de líneas del archivo
        Numero_Lineas = len (Archivo_lineas) 
        for i in range(0, 40):
            Conv=Archivo_lineas[i].split()
            #Validar que la lista sea mayor a cero para poder leerla
            if len (Conv) > 0:
                #  Identificar los nombres que deseamos para recuperarlos en una variable
                if Conv [0] == 'EMISIÓN' or Conv [0] == 'EMISION':
                    Emision.append (Conv [2])
                if Conv [0]=='ESTACIÓN' or Conv[0] == 'ESTACION':
                    Estacion.append(int (Conv [2]))
                if Conv [0] == 'NOMBRE':
                    Nombre.append (cadena_Nombre (Conv))
                if Conv [0] == 'ESTADO':
                    Estado.append (cadena_Nombre (Conv))
                if Conv [0] =='MUNICIPIO':
                    Municipio.append (cadena_Nombre (Conv))
                if Conv[0] == 'SITUACIÓN' or Conv [0]== 'SITUACION':
                    Situacion.append (Conv [2])
                if Conv [0] =='CVE-OMM':
                    CveOMM.append(cadena_Nombre (Conv))
                if Conv [0] =='LATITUD': 
                    Latitud.append(float (Conv[2].strip('\n ° \t :')))
                if Conv [0] == 'LONGITUD':
                    Longitud.append(float (Conv [2].strip('\n ° \t :')))
                if Conv [0] == 'ALTITUD':
                    Altitud.append (float (Conv [2]))
                if Conv [0]=='FECHA':
                    registro1=i+2 #El registro de fecha inicia dos registros después de la palabra fecha
                    dato1=Archivo_lineas[registro1].split()[0] #Extraemos la fecha de la lista
                    Fecha_Ini.append (dato1)
                    #Validar si el mes y el día son iguales a 1, es decir 1 de enero
                    if int(dato1[5:7])==1 and int(dato1[8:10])==1:
                        Anno_Inicio.append(int(dato1[0:4])) #Extraemos el año de la lista y lo guardamos en Anno_Inicio, el [0:4] es para extraer los primeros 4 caracteres
                    else:
                        Anno_Inicio.append(int((Archivo_lineas[registro1].split()[0])[0:4])+1)
        
        dato2=Archivo_lineas[-1].split()[0] #Extraemos de la lista de todas las líneas la última fecha
        Fecha_Fin.append (dato2)
        mi_archivo.close()
        #Validar año de fin de la lista, si el mes es 12 y el dia es 31
        if int(dato2[5:7])==12 and int(dato2[8:10])==31:
            Anno_Fin.append(int(dato2[0:4]))
        else:
            Anno_Fin.append(int(dato2[0:4])-1)

        for i in range(registro1, Numero_Lineas):
            FechaDatos.append(Archivo_lineas[i].split()[0])
            if Archivo_lineas[i].split()[1]=="NULO" or Archivo_lineas[i].split()[1]=="Nulo" or Archivo_lineas[i].split()[1]=="nulo":
                Precipitacion.append('NAN')
            else:
                Precipitacion.append((Archivo_lineas[i].split()[1]))
            
            if Archivo_lineas[i].split()[2]=="NULO" or Archivo_lineas[i].split()[2]=="Nulo" or Archivo_lineas[i].split()[2]=="nulo":
                Evaporacion.append('NAN')
            else:
                Evaporacion.append(Archivo_lineas[i].split()[2])

            if Archivo_lineas[i].split()[3]=="NULO" or Archivo_lineas[i].split()[3]=="Nulo" or Archivo_lineas[i].split()[3]=="nulo":
                TemperaturaMax.append('NAN')
            else:
                TemperaturaMax.append(Archivo_lineas[i].split()[3])

            if Archivo_lineas[i].split()[4]=="NULO" or Archivo_lineas[i].split()[4]=="Nulo" or Archivo_lineas[i].split()[4]=="nulo":
                TemperaturaMin.append('NAN')
            else:
                TemperaturaMin.append(Archivo_lineas[i].split()[4])
#Crear un DataFrame con los datos obtenidos
        datos=pd.DataFrame()
        datos['Fecha']=FechaDatos
        datos['Precipitación']=Precipitacion
        datos['Evaporación']=Evaporacion
        datos['Temperatura Máxima']=TemperaturaMax
        datos['Temperatura Mínima']=TemperaturaMin
        datos.to_csv(CarpetaDatos + archi[0:-4], index=None)
        
#AQUI RECORREMOS TODA LA LISTA DE ARCHIVOS PARA LEERLOS
##Definimos la rutas separadas por carpetas
DiaOperando=r'C:\Users\edivi\Documents\PROGRAMACION2\CONAGUA\Catalogo\Diario/Operando1'
Mensual=r'C:\Users\edivi\Documents\PROGRAMACION2\CONAGUA\Catalogo\Mensuales/Operando1' ##MODIFICAR
extension='.txt'
extraerInformacion(leerArchivo(DiaOperando, extension), DiaOperando)
#extraerInformacion(leerArchivo(Mensual, extension), Mensual)

datFr= pd.DataFrame()
datFr['Estación']=Estacion
datFr['Nombre']= Nombre
datFr['Estado']=Estado
datFr['Municipio']=Municipio
datFr['Situacion']=Situacion
datFr['CVE_OMM']=CveOMM
datFr['Latitud']=Latitud
datFr['Longitud']=Longitud
datFr['Altitud']=Altitud
datFr['Emision']=Emision
datFr['Fecha Inicio']=Fecha_Ini
datFr['Fecha Fin']=Fecha_Fin
datFr['Año Inicio']=Anno_Inicio
datFr['Año Fin']=Anno_Fin

datFr.to_excel(CarpetaDatos + 'catalogo1.xlsx', index=0)
print(datFr)

print(Estacion)
##print (Emision, Estacion, Nombre, Estado, Municipio, Situacion, CveOMM, Latitud, Longitud, Altitud, Fecha_Ini, Fecha_Fin)