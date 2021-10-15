# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 18:40:57 2021

@author: amene
"""
import random
from collections import Counter

#Le agregue a la funcion un parametro para poder elegir cuantos dados tiro.1 
def tirar(num = 5):
    tirada = [random.randint(1,6) for _ in range(num)]
    return tirada

def es_generala(tirada):
    return max(tirada)==min(tirada)

def prob_generala(N):
    cont_generalas = 0
    for i in range(N):
        contar_valores = Counter()
        tirada = tirar()
        #Si saca generala termina la iteracion y pasa a la siguiente.
        if es_generala(tirada):
            cont_generalas += 1
            continue
        #Aca cuento cuantos valores salieron y uso el most common para 
        #hacer una tupla que me dice el valor modal(un termino de la estadistica) y su frecuencia.
        for i in tirada:
            contar_valores[i] += 1
        moda = contar_valores.most_common(1)[0]
        #moda[1] me dice cuantas veces salio el mas frecuente asi que solo tiro los demas dados
        #podria restarselo a cinco directamente pero me guardo el valor para asi me es mas facil
        #hacer el punto extra.
        me_guardo = moda[1]
        #Para el punto extra agregaria el condicional
        """
        if me_guardo == 1:
            me_guardo = 0
        """
        tirada = tirar(5-me_guardo)
        #vuelvo a agregarle los dados que me guarde. moda es un tupla que me dice
        #  en 0 dice el valor de los dados y en 1 cuantos dados tenes.
        tirada += [moda[0] for _ in range(moda[1])]
        if es_generala(tirada):
            cont_generalas += 1
            continue
        #Repito los pasos anteriores para el tercer intento, no uso bucles para no enloquecer el continue.
        for i in tirada:
            contar_valores[i] += 1
        moda = contar_valores.most_common(1)[0]
        me_guardo = moda[1]
        #Para el punto extra agregaria el condicional
        """
        if me_guardo == 1:
            me_guardo = 0
        """
        tirada = tirar(5-me_guardo)
        tirada += [moda[0] for _ in range(moda[1])]
        if es_generala(tirada):
            cont_generalas += 1
    probabilidad = cont_generalas / N
    return probabilidad

def main():
    CM = 100000
    MI = 1000000
    G1 = sum([es_generala(tirar()) for i in range(CM)])
    G2 = sum([es_generala(tirar()) for i in range(MI)])
    prob1 = G1/CM
    prob2 = G2/MI
    print(f'Tiré {CM} veces, de las cuales {G1} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob1:.6f}.')
    print(f'Tiré {MI} veces, de las cuales {G2} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob2:.6f}.')
    N = 100000
    prob3 = prob_generala(N)
    print(f'Jugue {N} veces, salio generala con una probababilidad de {prob3:.6f}')
    # probando el punto extra la probabilidad me dio ligeramente superior utilizando el 
    #m metodo de no dejar un dado.

    