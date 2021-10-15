# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:51:29 2021

@author: amene
"""

def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

def listar_secuencias(n):
    lista = []
    num = [0  for _ in range(n)]
    lista.append(tuple(num))
    while sum(num) < len(num):
        num = incrementar(num)
        lista.append(tuple(num))
    return lista
            
def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos