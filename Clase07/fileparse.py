# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 23:43:59 2021

@author: amene
"""

import csv


def parse_csv(lista, select=None, types=None, has_headers=False, silence_errors=False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, 
    determinando el parámetro select, que debe ser una lista de
    nombres de las columnas a considerar.
    '''
    filas = csv.reader(lista)
    if has_headers:
        encabezados = next(filas)
    if select:
        indices = [encabezados.index(nombre_columna)
                   for nombre_columna in select]
        encabezados = select
    else:
        indices = []
    registros = []
    for fila in filas:
        if not fila:    # Saltear filas vacías
            continue
        if has_headers:
            if indices:
                fila = [fila[index] for index in indices]
            try:
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
            except ValueError:
                if not silence_errors:
                    print(f'No pude convertir {fila}')
                continue
            registro = dict(zip(encabezados, fila))
        else:
            registro = tuple(fila)
        registros.append(registro)
    return registros
