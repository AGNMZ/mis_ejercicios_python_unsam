

# Ejercicio 3.13: Recolectar datos

import fileparse


def leer_camion(nombre_archivo, seleccion=['nombre', 'cajones', 'precio']):
    camion = fileparse.parse_csv(nombre_archivo, select=seleccion, types=[
                                 str, int, float], has_headers=True)
    return camion

# Esta funcion devuelve  una lista de diccionario con cada fruta y su precio de
# venta


def leer_precio(nombre_archivo):
    precios = fileparse.parse_csv(
        '../Data/precios.csv', types=[str, float], has_headers=False)
    dict_pre = dict(precios)
    return dict_pre

# Esta funcion toma las lista de precios y camion y devuelve una lista de tuplas
# de cada fruta con sus datos


def hacer_informe(precios, camion):
    informe = []
    for fila in camion:
        r = ()
        r = (fila['nombre'], int(fila['cajones']), float(fila['precio']),
             float(precios[fila['nombre']]) - float(fila['precio']))
        informe.append(r)
    return informe


def imprimir_informe(informe):
    # enc es la tupla para el encabezado y sep del separador
    enc = (' Nombre', 'Cajones', 'Precio', 'Cambio')
    sep = ('', '', '', '')
    print(f'{enc[0]:^10s} {enc[1]:^10s} {enc[2]:^10s} {enc[3]:^10s}')
    print(f'{sep[0]:-^10s} {sep[1]:-^10s} {sep[2]:-^10s} {sep[3]:-^10s}')
    for nombre, cajones, precio, cambio in informe:
        precioS = '$' + str(round(precio, 2))
        print(f'{nombre:>10s} {cajones:>10d} {precioS:>10s} {cambio:>10.2f}')


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    precios = leer_precio(nombre_archivo_precios)
    camion = leer_camion(nombre_archivo_camion)
    informe = hacer_informe(precios, camion)
    imprimir_informe(informe)


# informe_camion('../Data/camion2.csv', '../Data/precios.csv')
