#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 16:45:55 2021

@author: amene
"""

import os
import sys
import datetime

def procesar_nombre(fname):
    """
    Toma el nombre de un archivo y devuelva la fecha y el nombre corregido.

    Parameters
    ----------
    fname : str
        el nombre del archivo a analizar debe ser del formato "archivo.png"
        debe tener su extension.
        
    Returns
    -------
    nombre_corregido : str
        El nombre que debe tener el archivo

    fecha : fecha
        la fecha que tiene etiquetada el archivo
  
    """
    try:
        year = int(fname[-12:-8])
        month = int(fname[-8:-6])
        day =  int(fname[-6:-4])
    except ValueError or IndexError:
        raise RuntimeError("El archivo debe tener el nombre con el formato correcto.")
    file_date = datetime.datetime(year, month, day)
    nombre_corregido = fname.replace(fname[-13:-5],"")
    return nombre_corregido , file_date



# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'dir_a_leer dir_destino')
#     dir_destino = sys.argv[2]
#     dir_a_leer = sys.argv[1]
#     os.mkdir(dir_destino)
    
    
    