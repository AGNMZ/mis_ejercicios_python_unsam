# rebotes.py
# Archivo de ejemplo
# Ejercicio

#---------|---------|---------|---------|---------|---------|---------/========<
"""Ejercicio 1.5: La pelota que rebota
Este es el primer conjunto de ejercicios en el que vas a tener que crear un
archivo de Python y correrlo. A partir de aca, vamos a asumir que estás 
trabajando en el subdirectorio ejercicios_python/. Para ayudarte a organizar 
los archivos de diferentes clases y a ubicar el lugar correcto ya creamos 
algunos subdirectorios y un par de archivos en el directorio correpondiente 
a esta clase. Buscá en tu terminal el archivo 
ejercicios_python/Clase01/rebotes.py (cambiando de directorio como vimos recién).
 Lo vamos a usar en este ejercicio.

Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que 
toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa 
rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada 
uno de sus primeros diez rebotes.

Tu programa debería generar una tabla que se parezca a esta:

1 60.0
2 36.0
3 21.599999999999998
4 12.959999999999999
5 7.775999999999999
6 4.6655999999999995
7 2.7993599999999996
8 1.6796159999999998
9 1.0077695999999998
10 0.6046617599999998

Nota: Podés limpiar un toque la salida si usás la función round() de la 
que miraste el help hace un rato. Tratá de usarla para redondear a cuatro 
dígitos.

1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
"""
#---------|---------|---------|---------|---------|---------|---------/========<
mul_rebote = 3/5
altura = 100
rebotes = 10
cont = 1


while cont<=rebotes:
    altura = altura * mul_rebote
    print(cont, round(altura, 4))
    cont = cont + 1