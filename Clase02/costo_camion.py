#---------|---------|---------|---------|---------|---------|---------/========<
"""
  Ejercicio 2.2: Lectura de un archivo de datos
Ahora que sabés leer un archivo, escribamos un programa que haga un cálculo
simple con los datos leídos.
Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad 
de cajones cargados en el camión, y un precio de compra por cada cajón de 
ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, 
lea las líneas, y calcule el precio pagado por los cajones cargados en el 
camión.

Ayuda: para interpretar un string s como un número entero, usá int(s). 
Para leerlo como punto flotante, usá float(s).

Tu programa debería imprimir una salida como la siguiente:

Costo total 47671.15
Acordate de guardar tu archivo en el directorio Clase02; vamos a volver 
a trabajar sobre él.
"""

"""
#Este es el  ejercicio 2.2
with open('../Data/camion.csv', 'rt') as arch_camion:
	encabezado = next(arch_camion).split()
	for linea in arch_camion:
		lis_linea = linea.split(',')
		cajones = int(lis_linea[1])
		# en la segunda columna estan los cajones, tomo su valor 
		# como entero
		precio = float(lis_linea[2].replace('\n',''))
		# el valor tiene un salto de linea que debe ser removido, como es 
		# un precio lo tomo como punto flotante
		costo_total += cajones * precio

print('Costo total',costo_total)
"""

#---------|---------|---------|---------|---------|---------|---------/========<
"""
Ejercicio 2.6: Transformar un script en una función
Transformá el programa costo_camion.py (que escribiste en el Ejercicio 2.2 
de la sección anterior) en una función costo_camion(nombre_archivo). Esta 
función recibe un nombre de archivo como entrada, lee la información sobre 
los cajones que cargó el camión y devuelve el costo de la carga de frutas 
como una variable de punto flotante.

Para usar tu función, cambiá el programa de forma que se parezca a esto:

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
Cuando ejecutás tu programa, deberías ver la misma salida impresa que antes. 
Una vez que lo hayas corrido, podés llamar interactivamente a la función 
escribiendo esto:

bash $ python3 -i costo_camion.py

Esto va a ejecutar el código en el programa y dejar abierto el intérprete 
interactivo.

>>> costo_camion('Data/camion.csv')
47671.15
>>>

Es útil para testear y debuguear poder interactuar interactivamente con 
tu código.
"""

"""
#este es el ejercicio 2.6
def costo_camion(nombre_archivo):
	with open(nombre_archivo, 'rt') as arch_camion:
		costo_total = 0
		encabezado = next(arch_camion).split()
		for linea in arch_camion:
			lis_linea = linea.split(',')
			cajones = int(lis_linea[1])
			# en la segunda columna estan los cajones, tomo su valor 
			# como entero
			precio = float(lis_linea[2].replace('\n',''))
			# el valor tiene un salto de linea que debe ser removido, como es 
			# un precio lo tomo como punto flotante
		costo_total += cajones * precio
	return(costo_total)


costo = costo_camion('../Data/camion.csv')
print('Costo total',costo)

"""
#---------|---------|---------|---------|---------|---------|---------/========<
"""
Ejercicio 2.8: Administración de errores
Probá correr la siguiente función ingresando tu edad real, una edad escrita 
con letras (como "ocho") y una edad negativa (-3):

def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad
Ahora probá este ejemplo que atrapa la excepción generada con raise y continúa 
la ejecución con la siguiente persona.

for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')
Vamos a usar estas ideas aplicadas al procesamiento de un archivo CSV. 
¿Qué pasa si intentás usar la función costo_camion() con un archivo que 
tiene datos faltantes?

>>> costo_camion('Data/missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <módulo>
    File "costo_camion.py", line 11, in costo_camion
    ncajones = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
El programa termina con un error. A esta altura tenés que tomar una 
decisión. Para que el programa funcione podés editar el archivo CSV de 
entrada de manera de corregirlo (borrando líneas o adecuando la información) 
o podés modificar el código para que maneje las líneas incorrectas de alguna 
manera.

Modificá el programa costo_camion.py para que atrape la excepción con un bloque 
try - except, imprima un mensaje de aviso (warning) y continúe procesando 
el resto del archivo.

Vamos a profundizar en la administración de errores en las próximas clases.
"""

"""
#este es el ejercicio 2.8
def costo_camion(nombre_archivo):
	with open(nombre_archivo, 'rt') as arch_camion:
		costo_total = 0
		encabezado = next(arch_camion).split()
		for i,linea in enumerate(arch_camion):
			try:
				lis_linea = linea.split(',')
				cajones = int(lis_linea[1])
				# en la segunda columna estan los cajones, tomo su valor 
				# como entero
				precio = float(lis_linea[2].replace('\n',''))
				# el valor tiene un salto de linea que debe ser removido, como es 
				# un precio lo tomo como punto flotante
			except ValueError:
				print("Un valor es incorrecto en la linea", i)
				cajones = 0
			precio = 0
				#si encuentra un ValueError, imprime la advertencia y el numero de linea
				#donde salto el error.
			costo_total += cajones * precio
	return(costo_total)

costo = costo_camion('../Data/missing.csv')
print('Costo total',costo)
"""
#---------|---------|---------|---------|---------|---------|---------/========<

"""
Ejercicio 2.9: Funciones de la biblioteca
Python viene con una gran biblioteca estándar de funciones útiles. En este 
caso el módulo csv podría venirnos muy bien. Podés usarlo cada vez que tengas 
que leer archivos CSV. Acá va un ejemplo de cómo funciona.

>>> import csv
>>> f = open('Data/camion.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['nombre', 'cajones', 'precio']
>>> for row in rows:
        print(row)

['Lima', '100', '32.2']
['Naranja', '50', '91.1']
['Caqui', '150', '103.44']
['Mandarina', '200', '51.23']
['Durazno', '95', '40.37']
['Mandarina', '50', '65.1']
['Naranja', '100', '70.44']
>>> f.close()
>>>
Una cosa buena que tiene el módulo csv es que maneja solo una gran variedad 
de detalles de bajo nivel como el problema de las comillas, o la separación 
con comas de los datos. En la salida del último ejemplo podés ver que el lector 
ya sacó las comillas dobles de los nombres de las frutas de la primera columna.

Modificá tu programa costo_camion.py para que use el módulo csv para leer 
los archivos CSV y probalo en un par de los ejemplos anteriores.
"""
#Ejercicio 2.9
import csv

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

costo = costo_camion('../Data/missing.csv')
print('Costo total',costo)