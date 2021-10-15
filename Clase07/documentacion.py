# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:24:59 2021

@author: amene
"""

def valor_absoluto(n):
    """
    Esta funcion devuelve el valor absoluto de un numero dado.

    Parameters
    ----------
    n : float
        Debe recibir un valor numerico.

    Returns
    -------
    TYPE float
        Devuelve numeros positivos

    """
    if n >= 0:
        return n
    else:
        return -n
    #el invariable justamente es |n|
    
def suma_pares(l):
    """
    Esta funcion toma un iterable que contenga numeros y devuelve la
    suma de aquellos que sean pares..

    Parameters
    ----------
    l : tipo iterable
        Debe ser un iterable que contenga datos numericos.

    Returns
    -------
    res : tipo entero
        Res va a ser un numero entero mayor que cero.

    """
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    return res
    #res - (sumatoria de e)=inv
    
def veces(a, b):
    """
    Esta funcion devuelve el valor de a tantas veces por b

    Parameters
    ----------
    a : TYPE floar
        Puede ser cualquier valor real.
    b : TYPE int
        Debe ser un valor entero mayor que cero.

    Returns
    -------
    res : TYPE float
        Devuelve un valor real

    """
    res = 0
    nb = b
    while nb != 0:
        # print(nb * a + res)
        res += a
        nb -= 1
    return res
    # inv = nb * a +res
    
    

    