#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:49:19 2021

@author: cris
"""

import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def hacer_curvas(n_curvas, N):
    ''' Recibe un n natural, genera n cantidad de curvas y las guarda 
    en una lista'''
    lista_curvas = []
    for i in range(n_curvas):
        curva = randomwalk(N)
        lista_curvas.append(curva)
    return lista_curvas


def curva_cercana(lista_curvas):
    '''Recibe una lista de arrays y devuelve la posición de la lista 
    que contiene al menor de los mayores de cada lista''' 
    posicion_cercana = 0
    menor_max = max(abs(lista_curvas[0]))
    for i, curva in enumerate(lista_curvas):
        maximo_actual = max(abs(lista_curvas[i]))
        if maximo_actual < menor_max:
            menor_max = maximo_actual
            posicion_cercana = i
    return posicion_cercana
            
def curva_lejana(lista_curvas):
    '''Recibe una lista de arrays y devuelve la posición de la lista 
    que contiene al mayor de los mayores de cada lista''' 
    posicion_lejana = 0
    mayor_max = max(abs(lista_curvas[0]))
    for i, curva in enumerate(lista_curvas):
        maximo_actual = max(abs(lista_curvas[i]))
        if maximo_actual > mayor_max:
            mayor_max = maximo_actual
            posicion_lejana = i
    return posicion_lejana
    

def dibujar_curvas(curvas, pasos):
    '''Recibe cantidad de curvas deseadas y pasos por curva.Devuelve un 
    subploteo con 3 gráficos, uno en la parte superior con todas las curvas
    y dos en la parte inferior con las curvas de mayor y menor desviación'''
    curvas = hacer_curvas(curvas, pasos)
    plt.subplot(2,1,1)
    for curva in curvas:
        plt.plot(curva)
    plt.title('Random Walk (12 caminatas al azar)')
    plt.ylabel('Distancia al origen')
    plt.xticks([]) 
    plt.subplot(2, 2, 3)
    plt.title('Caminata que mas se aleja')
    plt.plot(curvas[curva_lejana(curvas)])
    plt.xticks([]) 
    plt.subplot(2, 2, 4)
    plt.title('Caminata que menos se aleja')
    plt.plot(curvas[curva_cercana(curvas)])
    plt.xticks([]) 
    plt.show()

dibujar_curvas(12, 100000)