#---------|---------|---------|---------|---------|---------|---------/========<
"""
Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros
En el programa costo_camion.py, el nombre del archivo de entrada 
'../Data/camion.csv' fue escrito en el código.

# costo_camion.py
import csv

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
Esto está bien para ejercitar, pero en un programa real probablemente no 
harías eso ya que querrías una mayor flexibilidad. Una posibilidad es pasarle 
al programa el nombre del archivo que querés procesar como un parámetro 
cuando lo llamás desde la línea de comandos.

Copiá el contenido de costo_camion.py a un nuevo archivo llamado 
camion_commandline.py que incorpore la lectura de parámetros por línea de 
comando según la sugerencia del siguiente ejemplo:

# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
sys.argv es una lista que contiene los argumentos que le pasamos al script 
al momento de llamarlo desde la línea de comandos (si es que le pasamos alguno). 
Por ejemplo, desde una terminal de Unix (en Windows es similar), para correr 
nuestro programa y que procese el mismo archivo podríamos escribir:

bash $ python3 camion_commandline.py ../Data/camion.csv
Costo total: 47671.15
bash $
O con el archivo missing.csv:

bash $ python3 camion_commandline.py ../Data/missing.csv
...
Costo total: 30381.15
bash $

Si no le pasamos ningún archivo, va a mostrar el resultado para camion.csv 
porque lo indicamos con la línea nombre_archivo = '../Data/camion.csv'.

Guardá tu programa en el archivo camion_commandline.py para entregar al final 
de la clase.
"""

#Ejercicio 2.10
# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
	f = open(nombre_archivo)
	rows = csv.reader(f)
	costo_total = 0
	encabezado = next(rows)
	for i,linea in enumerate(rows):
		try:
			cajones = int(linea[1])
			# en la segunda columna estan los cajones, tomo su valor 
			# como entero
			precio = float(linea[2].replace('\n',''))
			# el valor tiene un salto de linea que debe ser removido, como es 
			# un precio lo tomo como punto flotante
		except ValueError:
			print("Un valor es incorrecto en la linea", i)
			cajones = 0
			precio = 0
			#si encuentra un ValueError, imprime la advertencia y el numero de linea
			#donde salto el error.
		costo_total += cajones * precio
	f.close()
	return(costo_total)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)