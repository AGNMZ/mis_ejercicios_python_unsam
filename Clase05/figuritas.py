# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 12:24:56 2021

@author: amene
"""
import random
import numpy as np
import matplotlib.pyplot as plt

# crear el album vacio


def crear_album(figus_total=670):
    return np.zeros(figus_total)

# genera una figurita aleatoria como agrega el cero reste uno al maximo


def comprar_figu(figus_total=670):
    return random.randint(0, figus_total-1)

# chequea si hay ceros en el album


def album_incompleto(A):
    return (0 in A)


# la funcion anterior tira un booleano, mientras sea falsa se continua el bucle
# asi cuento las figuritas que debo comprar.
def cuantas_figus(figus_total=670):
    album = crear_album(figus_total)
    cuantas = 0
    while album_incompleto(album):
        nueva = comprar_figu(figus_total)
        cuantas += 1
        album[nueva] += 1
    return cuantas


# Este calcula el promedio de fiuritas que se deben comprar, agreue el histograma
def experimento_figus(n_repeticiones=100, figus_total=670):
    pruebas = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    promedio = np.mean(pruebas)
    plt.hist(pruebas, bins=30)
    plt.show()
    return promedio

# aca se devuelve una lista de figuritas segun pida el paquete.


def comprar_paquete(figus_total=670, figus_paquete=5):
    paquete = [comprar_figu(figus_total) for _ in range(figus_paquete)]
    return paquete

# analogo al de cuantas figus, pero hace un bucle al final para agregar todo el paquete


def cuantos_paquetes(figus_total=670, figus_paquete=5):
    album = crear_album(figus_total)
    cuantos = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        cuantos += 1
        for figu in paquete:
            album[figu] += 1
    return cuantos

# igual que el experimento con las figuritas.


def experimento_paquetes(n_repeticiones=100, figus_total=670, figus_paquete=5):
    pruebas = [cuantos_paquetes(figus_total, figus_paquete)
               for _ in range(n_repeticiones)]
    promedio = np.mean(pruebas)
    plt.hist(pruebas, bins=25)
    plt.show()
    return promedio

# esta funcion esta copiada de la consigna, abajo esta comentado los comandos para usarla


def calcular_historia_figus_pegadas(figus_total=670, figus_paquete=5):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album > 0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas

# Ejercicio 5.20
# Esta funcion calcula la probabilidad de llenar el albun con una cierta cantidad de paquetes


def chance_llenar(figus_total=670, figus_paquete=5, paquetes_comprados=850, N=100):
    # Esto es lo que hice en un principio
    # pruebas = [cuantos_paquetes(figus_total, figus_paquete) < paquetes_comprados for _ in range(N)]
    # probabilidad = np.mean(pruebas)
    lista = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(N)]
    n_paquetes_hasta_llenar = np.array(lista)
    probabilidad = (n_paquetes_hasta_llenar <= paquetes_comprados).sum() / N
    return probabilidad

# Ejercicio 5.22
# aca se calcula cuantos paquetes hay que comprar para alcanzar alguna chance


def cuantos_paquetes_chance(figus_total=670, figus_paquete=5, chance=0.9, N=100):
    lista = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(N)]
    n_paquetes_hasta_llenar = np.array(lista)
    prob = 0
    paquetes_comprados = round(figus_total / figus_paquete)
    while (prob <= chance):
        prob = (n_paquetes_hasta_llenar <= paquetes_comprados).sum() / N
        paquetes_comprados += 1
    return paquetes_comprados

# Ejercicio 5.23:
# Esta funcion genera un paquete "premium" osea un paquete que no repite figuritas.


def comprar_paquete_premium(figus_total=670, figus_paquete=5):
    valores = np.arange(figus_total)
    valores = list(valores)
    paquete = random.sample(valores, k=figus_paquete)
    return paquete

# como la funcion cuantos_paquetes pero con paquetes premium


def cuantos_paquetes_premium(figus_total=670, figus_paquete=5):
    album = crear_album(figus_total)
    cuantos = 0
    while album_incompleto(album):
        paquete = comprar_paquete_premium(figus_total, figus_paquete)
        cuantos += 1
        for figu in paquete:
            album[figu] += 1
    return cuantos
# version premium de chance_llenar


def chance_llenar_premium(figus_total=670, figus_paquete=5, paquetes_comprados=850, N=100):
    # Esto es lo que hice en un principio
    # pruebas = [cuantos_paquetes(figus_total, figus_paquete) < paquetes_comprados for _ in range(N)]
    # probabilidad = np.mean(pruebas)
    lista = [cuantos_paquetes_premium(
        figus_total, figus_paquete) for _ in range(N)]
    n_paquetes_hasta_llenar = np.array(lista)
    probabilidad = (n_paquetes_hasta_llenar <= paquetes_comprados).sum() / N
    return probabilidad
# %%
# Ejercicio 5.24: Cooperar vs competir
# Cuanta cuantos paquetes deben comprar una cierta cantidad de amigos para completar
# cada uno su album cooperando,


def cuantos_paquetes_coop(figus_total=670, figus_paquete=5, amigos=5):
    album = crear_album(figus_total)
    cuantos = 0
    # Aca lo que hago es verificar que haya cinco copias de cada figurita.
    # creo que si se modifica album tambien se modifica album5 no?
    albumC = (album > amigos)
    while album_incompleto(albumC):
        paquete = comprar_paquete(figus_total, figus_paquete)
        cuantos += 1
        for figu in paquete:
            album[figu] += 1
        albumC = (album > amigos)
    return cuantos
# una funcion para mostrar la diferencia entre cooperar y competir, no devuelve nada
# solo imprime los resultados.


def cooperar_vs_competir(figus_total=670, figus_paquete=5, N=100, amigos=5):
    comp_acumulado = 0
    coop_acumulado = 0
    for _ in range(N):
        competir = [cuantos_paquetes(figus_total, figus_paquete)
                    for _ in range(amigos)]
        comp_acumulado += sum(competir)
        coop_acumulado += cuantos_paquetes_coop(
            figus_total, figus_paquete, amigos)
    comp = comp_acumulado / N
    coop = coop_acumulado / N
    print(
        f'Si los amigos compiten deberan comprar en promedio {comp} paquetes.')
    print(
        f'Si los amigos cooperan deberan comprar en promedio {coop} paquetes.')


# %%
# se debe descomentar esto para usar la funcion calcular_historia_figus_pegadas
"""
figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
"""
