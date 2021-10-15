# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:34:17 2021

@author: amene
"""
import random
from collections import Counter


def barajar(tam=3):
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor, palo) for valor in valores for palo in palos]
    mano = random.sample(naipes, tam)
    return mano


def hay_tanto(mano):
    # valores va a ser la lista con cada carta y el valor para el envido, 
    # el 10 11 y 12 no tienen valor para el envido.
    valores = [(valor, palo) for valor, palo in mano if valor < 10]
    valores += [(0, palo) for valor, palo in mano if valor >= 10]
    #con contador cuento cuantas cartas hay de cada palo
    contador = Counter()
    for valor, palo in mano:
        contador[palo] += 1
    #con el comando most common puedo guardar cual es el palo para el tanto y
    #cuantas cartas tienen el mismo palo.
    palo_tanto = contador.most_common(1)[0][0]
    cartas_tanto = contador.most_common(1)[0][1]
    # segun cuantas cartas tiene el tanto cuento los puntos, si solo es una carta
    #simplemente tomo la mas grande, sino tengo que sumar las dos mas altas
    #como es una mano de tres cartas, en el caso de flor, simplemente le reste
    #el minimo
    if cartas_tanto == 1:
        tanto = max([valor for valor, palo in valores])
    elif cartas_tanto == 2:
        tanto = sum(
            [valor for valor, palo in valores if palo == palo_tanto]) + 20
    else:
        tanto = sum([valor for valor, palo in valores]) - \
            min([valor for valor, palo in valores]) + 20
    return tanto


# Al final la funcion me quedo cortita
# el parametro N es la cantidad de manos y c_puntos es la cantidad de puntos que quiero averiguar que salen
def prob_envido(N, c_puntos):
    cont_envido = 0
    for i in range(N):
        mano = barajar()
        if hay_tanto(mano) == c_puntos:
            cont_envido += 1
    prob = cont_envido / N
    return prob

def main():
    semilla = 10
    random.seed(semilla)
    N = 100000
    c31 = prob_envido(N,31)
    c32 = prob_envido(N,32)
    c33 = prob_envido(N,33)
    print(f'De una muestra de {N} tiradas con una semilla de valor {semilla}:')
    print(f'Una proporcion de {c31} tuvo puntuacion de 31.')  
    print(f'Una proporcion de {c32} tuvo puntuacion de 32.')    
    print(f'Una proporcion de {c33} tuvo puntuacion de 33.')    