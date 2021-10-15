#---------|---------|---------|---------|---------|---------|---------/========<
"""
#Ejercicio 2.15
import csv

def leer_camion(nombre_archivo):
	camion = []
	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			lote = (row[0], int(row[1]), float(row[2]))
			camion.append(lote)
	return camion
"""

#Ejercicio 2.16 y 2.18
import csv

def leer_camion(nombre_archivo):
	dcamion = {}
	camion = []
	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		h = next(rows)
		for row in rows:
			r = [(h[0], row[0]), (h[1], int(row[1])), (h[2], float(row[2]))]
			dcamion = dict(r)
			camion.append(dcamion)
	return camion

def leer_precio(nombre_archivo):
	lis_pre = []
	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		for row in rows:
			try:
				t = (row[0], float(row[1]))
				lis_pre.append(t)
			except IndexError:
				pass
		dict_pre = dict(lis_pre)
	return dict_pre

precios = leer_precio('../Data/precios.csv')
camion = leer_camion('../Data/camion.csv')
costo_total = 0
ventas_total = 0

for i in camion:
	costo_total += i['cajones'] * i['precio']
	if i['nombre'] in precios:
		ventas_total += i['cajones'] * precios[i['nombre']]

balance = ventas_total - costo_total

print("El costo del camion fue de: $",round(costo_total,2))
print("El valor de las ventas realizadas fue de: $",round(ventas_total,2))
print("El balance fue de: $",round(balance,2))

if balance>0:
	print("Hubo ganancia.")
else:
	print("Hubo perdida.")