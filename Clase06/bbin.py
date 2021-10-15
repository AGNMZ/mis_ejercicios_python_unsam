# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:21:16 2021

@author: amene
"""
import random #para probar si funciona.
#%%
#dejo la funcion original para  comparar
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, comps
#%%
def donde_insertar(lista, x, verbose = False):
    '''
    Recibe una lista ordenada y un elemento y devuelva la posición 
    de ese elemento en la lista (si se encuentra en la lista) 
    o la posición donde se podría insertar el elemento para que la 
    lista permanezca ordenada (si no está en la lista).
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    medio = 0
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    """
    al final me volvi loco intentando buscar las condiciones correctas para
    que funcione, no me quedo muy elegante pero funciona
    """
    if pos == -1:
        if (medio == len(lista) - 1):
            if x > lista[medio]:
                pos = len(lista)
            else:
                pos = medio
        else:        
            if der < 0 or x > lista[der]:                                 
                pos = izq
            else:
                pos = der                               
    return pos

def insertar(lista, x, verbose = False):
    '''
    Recibe una lista ordenada y un elemento. Si el elemento 
    se encuentra en la lista solamente devuelve su posición;
    si no se encuentra en la lista, lo inserta en la posición 
    correcta para mantener el orden. 
    En este segundo caso, también devuelve su posición.
    '''
    pos = busqueda_binaria(lista, x)[0]
    if pos == -1:
        pos = donde_insertar(lista, x,verbose)
        lista.insert(pos, x)
    return pos
#para probar usamos una funcion que tira un dado y vamos si los devuelve ordenados.




