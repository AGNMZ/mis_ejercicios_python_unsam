# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:21:36 2021

@author: amene
"""

import math

def buscar_u_elemento(l,e):
    pos = -1
    for i,item in enumerate(l):
        if e == item:
            pos = i
    return pos

def buscar_n_elemento(l,e):
    con = 0
    for i,item in enumerate(l):
        if e == item:
            con += 1
    return con

def maximo(lista):
    '''Devuelve el máximo de una lista
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = -math.inf #inicializo en menos infinito
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def minimo(lista):
    '''Devuelve el minimo de una lista
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = math.inf #inicializo en menos infinito
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m



def main(): 
    print(buscar_u_elemento([1,2,3,2,3,4],1))
    print(maximo([1,2,7,2,3,4]))
    print(maximo([-5,-4]))

