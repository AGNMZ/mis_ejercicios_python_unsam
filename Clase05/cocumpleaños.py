# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:12:06 2021

@author: amene
"""
import random
from collections import Counter

def tirar(num = 30):
    tirada = [random.randint(1,365) for _ in range(num)]
    return tirada

def prob_cocum(N, personas = 30):
    cont_cocum = 0
    for i in range(N):
        contar_valores = Counter()
        tirada = tirar(personas)
        for i in tirada:
            contar_valores[i] += 1
        moda = contar_valores.most_common(1)[0]
        if moda[1] > 1:
            cont_cocum += 1
    probabilidad = cont_cocum / N
    return probabilidad


def main():
    personas = 1
    N = 10000
    prob = 0
    while prob < 0.5:
        prob = prob_cocum(N, personas)
        personas += 1
    print(personas) 