"""
Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo
Queremos hacer un traductor que cambie las palabras masculinas de una frase 
por su versión neutra. Como primera aproximación, completá el siguiente código 
para reemplazar todas las letras 'o' que figuren en el último o anteúltimo 
caracter de cada palabra por una 'e'. Por ejemplo 'todos somos programadores' 
pasaría a ser 'todes somes programadores'.
 Guardá tu código en el archivo inclusive.py
"""
#---------|---------|---------|---------|---------|---------|---------/========<
frase = 'Todos, tu también'
palabras = frase.split()
for palabra in palabras:
	i = palabras.index(palabra)
	if len(palabra)>2:
		if palabra[-1]=='o':
			palabra_inc = palabra[0:-1] + 'e'
			palabras.remove(palabra)
			palabras.insert(i,palabra_inc)
		elif palabra[-2]=='o':
			palabra_inc = palabra[0:-2] + 'e' + palabra[-1]
			palabras.remove(palabra)
			palabras.insert(i,palabra_inc)
frase_t = ' '.join(palabras)
print(frase_t)

#palabras.remove(palabra)
#palabras.insert(i,palabra_inc)
