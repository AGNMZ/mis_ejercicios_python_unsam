

# Ejercicio 3.13: Recolectar datos
import csv

# Esta funcion lee el archivo y retorna una lista de diccionarios con los nombres
# ,cajones y precios de la fruta.


def leer_camion(nombre_archivo):
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)
    camion = []
    for n_fila, fila in enumerate(filas, start=1):
        dcamion = dict(zip(encabezados, fila))
        camion.append(dcamion)
    f.close()
    return camion

# Esta funcion devuelve  una lista de diccionario con cada fruta y su precio de
# venta


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

# Esta funcion toma las lista de precios y camion y devuelve una lista de tuplas
# de cada fruta con sus datos


def hacer_informe(precios, camion):
    informe = []
    for fila in camion:
        r = ()
        r = (fila['nombre'], int(fila['cajones']), float(fila['precio']),
             float(precios[fila['nombre']]))
        informe.append(r)
    return informe


# precios = leer_precio('../Data/precios.csv')
# camion = leer_camion('../Data/fecha_camion.csv')
# inf = hacer_informe(precios, camion)
# # enc es la tupla para el encabezado y sep del separador
# enc = (' Nombre', 'Cajones', 'Precio', 'Cambio')
# sep = ('', '', '', '')
# print(f'{enc[0]:<10s} {enc[1]:^10s} {enc[2]:^10s} {enc[3]:^10s}')
# print(f'{sep[0]:-^10s} {sep[1]:-^10s} {sep[2]:-^10s} {sep[3]:-^10s}')
# for nombre, cajones, precio, cambio in inf:
#     precioS = '$' + str(round(precio, 2))
#     print(f'{nombre:>10s} {cajones:>10d} {precioS:>10s} {cambio:>10.2f}')
