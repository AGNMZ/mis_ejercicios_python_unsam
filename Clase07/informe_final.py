#!/usr/bin/env python3
# Ejercicio 3.13: Recolectar datos

import fileparse
import sys


def leer_camion(nombre_archivo, seleccion=['nombre', 'cajones', 'precio']):
    with open(nombre_archivo, 'rt') as lista:
        camion = fileparse.parse_csv(lista, select=seleccion, types=[
            str, int, float], has_headers=True)
    return camion

# Esta funcion devuelve  una lista de diccionario con cada fruta y su precio de
# venta


def leer_precio(nombre_archivo):
    with open(nombre_archivo, 'rt') as lista:
        precios = fileparse.parse_csv(
            lista, types=[str, float], has_headers=False)
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


def f_principal(parametros):
    informe_camion(parametros[1], parametros[2])


# if __name__ == '__main__':
#     f_principal(sys.argv)
