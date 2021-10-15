#---------|---------|---------|---------|---------|---------|---------/========<
"""
Ejercicio 2.14: Diccionario geringoso.
Construí una función que, a partir de una lista de palabras, devuelva un 
diccionario geringoso. Las claves del diccionario deben ser las palabras 
de la lista y los valores deben ser sus traducciones al geringoso (como 
en el Ejercicio 1.18). Probá tu función para la lista 
['banana', 'manzana', 'mandarina']. 
Guardá este ejercicio en un archivo diccionario_geringoso.py para entregar 
al final de la clase.

"""

#Ejercicio 2.14

#esta funcion es el ejercicio del geringoso que devuelve la palabra 
#transformada.
def geringosear(cadena):
	cadena = cadena.lower()
	capadepenapa = ''
	for c in cadena:
		if c in 'aeiou':
			capadepenapa = capadepenapa + c + 'p' + c
		else:
			capadepenapa = capadepenapa + c
	return capadepenapa

def dir_gen(lista):
	d = {}
	for palabra in lista:
		d[palabra] = geringosear(palabra)
	return d

prueba = ['banana', 'manzana', 'mandarina']
print(dir_gen(prueba))