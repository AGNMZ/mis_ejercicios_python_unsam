# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:22:50 2021

@author: amene
"""


"""
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    #Version con ciclo
    resultado = 0
    if hasta >= desde:
        for i in range(desde, hasta):
            resultado += i
    return resultado
"""
def trian(numero):
    '''
    Esta funcion devuelve el numero triangular del valor absoluto del parametro

    Parameters
    ----------
    numero : integer
        El parametro puede ser un numero entero positivo o negativo

    Returns
    -------
        Devuelve el numero triangular.

    '''
    n = abs(numero)
    t = n*(n+1)/2
    return t
    
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    #version con numero trianular.
    resultado = 0
    if hasta >= desde:
        resultado = trian(hasta) - trian(desde)
    return resultado
        
    