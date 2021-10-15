#ejercicio 2.17
import csv

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


