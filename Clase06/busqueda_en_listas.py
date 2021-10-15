# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:06:40 2021

@author: amene
"""

def busqueda_lineal_lordenada(lista,e):
    '''Si e está en la lista devuelve su posición, de lo
        contrario devuelve -1.
        la función para cuando encuentre un elemento mayor a e
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        if z > e:    #La funcion sale en cuanto encuentra un elemento mayoa a e
            break
    return pos

