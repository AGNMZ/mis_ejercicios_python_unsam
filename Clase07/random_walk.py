# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:06:22 2021

@author: amene
"""

#Devolvi el ejercico porque en la revision de pares me hicieron notar que 
# no estaba correctamente resuelto.

import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


def maximo_absoluto(serie):
    """
    La funcion devuelve el maximo de los valores absolutos de la funcion.

    Parameters
    ----------
    serie : lista
        la serie a analizar

    Returns
    -------
    maximo : float
        el valor maximo en valor absoluto

    """
    maximo = max([abs(dato) for dato in serie])
    return maximo


N = 100000
series = [randomwalk(N) for _ in range(12)]
# antes habia intentado usar la varianza, pero me funciona de manera extraña
# al querer ponerle la media cero a la medicion, por lo que prefiero usar
# el metodo de fijarme cual tiene
maximos = [maximo_absoluto(serie) for serie in series]
minimo = min([dato for dato in maximos])
maximo = max([dato for dato in maximos])
imin = 0
imax = 0

# Aca quiero sacar el indice de la serie con el maximo mas grande y el mas pequeño
for i, dato in enumerate(maximos):
    if dato == maximo:
        imax = i
    if dato == minimo:
        imin = i

plt.subplot(2, 1, 1)
for serie in series:
    plt.plot(serie)
plt.ylim(-550, 550)
plt.title('12 Caminatas al azar')
plt.xticks([]), plt.yticks([-500, 0, +500], [r'$-500$', r'$0$', r'$500$'])

plt.subplot(2, 2, 3)
plt.plot(series[imax])
plt.xticks([]), plt.yticks([-500, 0, +500], [r'$-500$', r'$0$', r'$500$'])
plt.ylim(-550, 550)
plt.title('La caminata que mas se aleja.')

plt.subplot(2, 2, 4)
plt.plot(series[imin])
plt.xticks([]), plt.yticks([-500, 0, +500], [r'$-500$', r'$0$', r'$500$'])
plt.ylim(-550, 550)
plt.title('La caminata que menos se aleja.')

plt.show()
