# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:44:40 2021

@author: amene
"""
# Ejercicio 3.18: Lectura de los árboles de un parque
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
# Esta funcion asigna el tipo correcto a cada dato


def leer_parque(nombre_archivo, parque):
    parque = parque.upper()
    parque_l = []
    with open(nombre_archivo, encoding="utf8") as f:
        filas = csv.reader(f)
        enc = next(f).split(',')
        for n_fila, fila in enumerate(filas, start=1):
            fila_tip = tipo_de_dato(fila)
            if parque in fila_tip:
                record = {}
                record = dict(zip(enc, fila_tip))
                parque_l.append(record)
    return parque_l

# %%

# Ejercicio 3.19: Determinar las especies en un parque


def especies(lista_arboles):
    esp = set()
    for linea in lista_arboles:
        esp.add(linea['nombre_com'])
    return esp


# %%

# Ejercicio 3.20: Contar ejemplares por especie
def contar_ejemplares(lista_arboles):
    from collections import Counter
    ej = Counter()
    for l in lista_arboles:
        ej[l['nombre_com']] += 1
    return ej

# hice esta funcion para tomar los datos de  las listas de ejemplares e \
# imprimirlas en formato table


def hacer_tabla3(lis1, lis2, lis3, hasta, tit):
    print(f'{tit[0]:^26s}{tit[1]:^26s}{tit[2]:^26s}')
    for i in range(hasta):
        val1 = f'{lis1[i][0]}:{lis1[i][1]}'
        val2 = f'{lis2[i][0]}:{lis2[i][1]}'
        val3 = f'{lis3[i][0]}:{lis3[i][1]}'
        print(f'{val1:<26s}{val2:<26s}{val3:<26s}')

# %%

# Ejercicio 3.21: Alturas de una especie en una lista


def obtener_alturas(lista_arboles, especie):
    alturas = []
    for l in lista_arboles:
        if especie in l['nombre_com']:
            alturas.append(l['altura_tot'])
    return alturas


def hacer_tabla4(lis1, lis2, lis3, tit):
    import statistics
    md = 'Medida'
    mp = ('max', 'prom')
    print(f'{md:<7s}{tit[0]:<12s}{tit[1]:<10s}{tit[2]:<11s}')
    val1 = f'{round(max(lis1),2)}'
    val2 = f'{round(max(lis2),2)}'
    val3 = f'{round(max(lis3),2)}'
    print(f'{mp[0]:<7s}{val1:<12s}{val2:<10s}{val3:<11s}')
    val1 = f'{round(statistics.mean(lis1),2)}'
    val2 = f'{round(statistics.mean(lis2),2)}'
    val3 = f'{round(statistics.mean(lis3),2)}'
    print(f'{mp[1]:<7s}{val1:<12s}{val2:<10s}{val3:<11s}')

# %%


def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for i, l in enumerate(lista_arboles):
        if especie in l['nombre_com']:
            inclinaciones.append(l['inclinacio'])
    return inclinaciones

# %%


def especimen_mas_inclinado(lista_arboles):
    todas_esp = especies(lista_arboles)
    maximos = []
    for especie in todas_esp:
        max_esp = (max(obtener_inclinaciones(lista_arboles, especie)), especie)
        maximos.append(max_esp)
    return max(maximos)

# %%
# Ejercicio 3.24: Especie más inclinada en promedio


def especie_promedio_mas_inclinado(lista_arboles):
    import statistics
    todas_esp = especies(lista_arboles)
    promedios = []
    for especie in todas_esp:
        pro_esp = (statistics.mean(obtener_inclinaciones(
            lista_arboles, especie)), especie)
        promedios.append(pro_esp)
    return max(promedios)


def tipo_de_dato(fil):
    a0 = float(fil[0])
    a1 = float(fil[1])
    a2 = int(fil[2])
    a3 = int(fil[3])
    a4 = int(fil[4])
    a5 = int(fil[5])
    a6 = int(fil[6])
    a7 = str(fil[7])
    a8 = str(fil[8])
    a9 = str(fil[9])
    a10 = str(fil[10])
    a11 = str(fil[11])
    a12 = str(fil[12])
    a13 = str(fil[13])
    a14 = str(fil[14])
    a15 = float(fil[15])
    a16 = float(fil[16])
    fila_tipo = (a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13,
                 a14, a15, a16)
    return fila_tipo

# %%
# Ejercicio 4.15: Lectura de todos los árboles
#Esta parte es la de la seccion 4

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo, encoding="utf8") as f:
        filas = csv.reader(f)
        enc = next(f).split(',')
        tipos = [float, float, int, int, int, int, int, str,
                 str, str, str, str, str, str, str, float, float]
        for fila in filas:
            fila_tip = [func(val) for func, val in zip(tipos, fila)]
            record = {}
            record = dict(zip(enc, fila_tip))
            arboleda.append(record)
    return arboleda

#Esta funcion devuelve una lista de tuplas con la altura y diametro.
def lista_alt_diam(arboleda, nombre):
    HD = [(arbol['altura_tot'], arbol['diametro'])
          for arbol in arboleda if arbol['nombre_com'] == nombre]
    return HD

#Para formar el diccionario itere sobre especies y use la funcion anterior .
def medidas_de_especies(especies, arboleda):
    diccionario = {arbol: lista_alt_diam(
        arboleda, arbol) for arbol in especies}
    return diccionario

#%%

#Ejercicio 5.25: Histograma de altos de Jacarandás

def histograma():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    plt.hist(altos,bins=50)

# Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás

def scatter_hd(lista_de_pares, color='b', size=25):
    array = np.array(lista_de_pares)
    h = array[:,1]
    d = array[:,0]
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto")
    plt.scatter(d,h, s=size, c=color ,alpha=0.10)
    
def scatter_varios():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    plt.xlim(0,40) 
    plt.ylim(0,150) 
    scatter_hd(medidas['Jacarandá'], color='r', size=30)
    scatter_hd(medidas['Palo borracho rosado'],color='g', size=30)
    scatter_hd(medidas['Jacarandá'],color='b', size=30)
    
def main():
    # from pprint import pprint
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    # H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    # # print(H)
    # HD=[(arbol['altura_tot'],arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    # pprint(HD)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    dicc = medidas_de_especies(especies, arboleda)
    print(len(dicc['Eucalipto']))
    print(len(dicc['Palo borracho rosado']))
    print(len(dicc['Jacarandá']))
