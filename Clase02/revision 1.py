##2.18 Balances
from pprint import pprint
import csv
#Funcion 1- Retorna una lista (camion) donde cada elemento es un diccionario que 
#contiene las claves: valor para nombre,cajones y precio de costo
#se debe utilizar el archivo camion.csv
def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo, 'rt') as f:
       rows = csv.reader(f)
       headers = next(rows)
       for row in rows:
           lote={'nombre':row[0],
                 'cajones':int(row[1]),
                 'precio':float(row[2])}
           camion.append(lote)
    return camion
#Funcion 2 - Retorna un diccionario (precios) con claves:valor para frutas/verduras y el precio venta
#Se debe utilizar el archivo precios.csv
def leer_precios(nombre_archivo):
    with open(nombre_archivo,'rt',encoding='utf8') as f:
        precios={}
        rows=csv.reader(f)
        for row in rows:
            try:
               precios[row[0]]=float(row[1])
            except IndexError:
               break 
        return precios

#Funcion 3 - Para obtener una tupla con las ventas y costos totales y el resultado(Ventas-costos)
def balance(archivo_costo,archivo_venta):
      dcosto=leer_camion(archivo_costo)#llamado Funcion 1
      dventa=leer_precios(archivo_venta)#llamado Funcion 2
      for row in dcosto:
            row['precio_vta']=float(dventa[row['nombre']])#agrego clave:valor para precio de venta en el diccionario que contiene datos de costos(camion.csv)
      resultado=0.0
      ventas_totales=0.0
      costos_totales=0.0     
      for b in dcosto:#Obtenemos la informacion (ventas totales, costos totales y la diferencia)
           resultado=resultado + ((b['precio_vta']-b['precio'])*b['cajones'])
           ventas_totales=ventas_totales+ (b['precio_vta']*b['cajones'])
           costos_totales=costos_totales+ (b['precio']*b['cajones'])
      return (ventas_totales,costos_totales,resultado)

#Funcion 4 - Para Mostrar Informe con los resultados obtenidos en la funcion 3
def Informe(ventas,costos,resultado):
    if resultado>0:
       mensaje=f'''Informe: Ventas total:$ {ventas},
         Costo total:$ {costos},
         Resultado bruto positivo(ganancia):$ {resultado}'''
    elif resultado<0:
       mensaje=f'''Informe: Ventas total:$ {ventas},
         Costo total:$ {costos},
         Resultado bruto negativo(perdida):$ {resultado}'''
    else:
       mensaje=f'''Informe: Ventas total:$ {ventas},
         Costo total:$ {costos},
         Resultado neutro:$ {resultado}'''          
    return mensaje

archivo_camion='../Data/camion.csv'
archivo_precios='../Data/precios.csv'  
ingresos,costos,resultado=balance(archivo_camion,archivo_precios)
informe=Informe(ingresos,costos,resultado)
print(informe)
#se utiliza la funcion balance y desempaquetamos la tupla que se obtiene
# de la funcion balance en 3 variables(ingresos,costos,resultado)
#utilizamos la funcion informe con las variables que obtuvimos de la tupla de la funcion balance
#Salida Ej-2.18
#Informe: Ventas total:$ 62986.1,
#         Costo total:$ 47671.15,
#         Resultado bruto positivo(ganancia):$ 15314.95