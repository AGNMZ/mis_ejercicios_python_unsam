#---------|---------|---------|---------|---------|---------|---------/========<
"""
Ejercicio 2.3: Precio de la naranja
El archivo Data/precios.csv contiene una serie de líneas con precios de 
venta de cajones en el mercado al que va el camión. El archivo se ve así:

"Lima",40.22
"Uva",24.85
"Ciruela",44.85
"Cereza",11.27
"Frutilla",53.72
...
Escribí un código que abra el archivo Data/precios.csv, busque el precio 
de la naranja y lo imprima en pantalla.

>>> f = open('../Data/precios.csv', 'rt')
...
>>> f.close()

El precio de la naranja es:  106.28
"""
fruta = "Naranja"

f = open('../Data/precios.csv', 'rt')
for line in f:
	row = line.split(',')
	if fruta in line:
		print("El precio de:",fruta,", es de $",row[1])

f.close()
