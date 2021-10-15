# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:39:24 2021

@author: amene
"""
import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def estimacion_pi(N):
    M = 0
    for _ in range(N):
        punto = generar_punto()
        dentro = (punto[0]**2 + punto[1]**2 < 1)
        if dentro:
            M += 1
    est = 4 * M/N
    return est 

def main():
    N = 100000
    est = estimacion_pi(N)
    print(f'Utilizando {N} puntos:')
    print(f'Se obtuvo una estimacion de pi de {est}')