#---------|---------|---------|---------|---------|---------|---------/========<
"""
Ejercicio 2.7: Buscar precios
A partir de lo que hiciste en el Ejercicio 2.3, escribí una función 
buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio 
de determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no 
figura en el listado de precios, debe imprimir un mensaje que lo indique.

>>> buscar_precio('Frambuesa')
El precio de un cajón de Frambuesa es: 34.35
>>> buscar_precio('Kale')
Kale no figura en el listado de precios.

Guardá este código en un archivo buscar_precios.py para entregar al final 
de la clase.
"""

def buscar_precios(fruta):
	f = open('../Data/precios.csv', 'rt')
	esta = False
	#la variable esta es por defecto falsa hasta que se encuentre la fruta
	#en el archivo
	for line in f:
		row = line.split(',')
		if fruta in line:
			esta = True
			precio = row[1]
			#si alguna vez se entra en el condicional, la variable de control
			#pasa a verdadero y se uarda el preci
	f.close()
	if esta:
		print("El precio de un cajon de", fruta,"es:",precio)
	else:
		print(fruta,"no figura en el listado de precios.")

fruta = input("Ingrese el nombre de la fruta  cuyo precio desea conocer:")
buscar_precios(fruta)