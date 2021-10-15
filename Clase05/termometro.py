# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:58:31 2021

@author: amene
"""
import random
import numpy as np

# Me dusta que las funciones tengan todos los parametros para que sean mas flexibles
# Aunque eso las hace mas dificiles de leer.
# valor es lo que voy a medir. la media del error seria el sesgo, cero en este caso
# y el desvio. Hice que se redondee al primer decimal porque el termometro te
# va a dar un valor con esa precicion.
def medir_temp(N, valor=37.5, media_error=0, desvio_error=0.2):
    mediciones = [round(random.normalvariate(
        valor + media_error, desvio_error), 1) for _ in range(N)]
    vector = np.empty(N)
    vector = mediciones
    try:
        np.save('../Data/temperaturas.npy', vector)
    except OSError:
        print("No puedo guardar en la poscicion solicitada.")
    return mediciones


def calc_mediana(lista):
    lista.sort()
    # aca la condicion es si el tamaño de la lista es par o impar. haciendo las
    # cuentas en cada caso.
    if len(lista) % 2 != 0:
        el_medio = round(len(lista) / 2)
        mediana = lista[el_medio]
    else:
        la_mitad = int(len(lista) / 2)
        mediana = (lista[la_mitad] + lista[la_mitad+1])/2
    return mediana


def resumen_temp(N):
    # Esto lo hice para probar como funcionaba levantar una exepcion.
    if N <= 0:
        raise ValueError("Lo siento, solamente numeros mayores que cero.")
    temp = medir_temp(N)
    maximo = max(temp)
    minimo = min(temp)
    promedio = sum(temp) / N
    promedio = round(promedio, 1)
    # Como sacar la mediana era el proceso mas complejo por eso lo hice en una
    # funcion aparte para que se entienda mas facil.
    mediana = calc_mediana(temp)
    # Para obtener los cuartiles
    """
    cuartil1 = calc_mediana(temp[0, int(N/2))]
    cuartil2 = calc_mediana(temp)
    cuartil3 = calc_mediana(temp[round(N/2), N)]
    """
    return (maximo, minimo, promedio, mediana)

def main():
    N = 999
    res = resumen_temp(N)
    print(f'De una muestra de {N} mediciones se obtuvieron los siguientes datos:')
    print(f'Maximo: {res[0]}')
    print(f'Minimo: {res[1]}')
    print(f'Promedio: {res[2]}')
    print(f'Mediana: {res[3]}')