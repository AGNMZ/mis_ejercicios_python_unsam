#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 15:45:31 2021

@author: amene
"""
import os
import sys

def archivos_png(directorio):
    """
    Arma una lista de todos los archivos .png que se encuentren 
    en algún subdirectorio directorio dado.

    Parameters
    ----------
    directorio : STR
        direccion del directorio a analizar.

    Returns
    -------
    lista_archivos_png : LIST
        lista de cada png encontrado.

    """
    #    
    lista_archivos_png = []
    # Queria usar interpretacion de listas para hacer el ejercicio pero
    # no se me ocurrio como hacerlo.
    for root, dirs, files in os.walk(directorio):
        for name in files:
           if name[-3:] == "png":
               lista_archivos_png.append(name)
    return lista_archivos_png

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio')
    print(archivos_png(sys.argv[1]))