#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

#%% ejercicio 7.7
import fileparse
import lote 
import formato_tabla

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo) as f:
        camion_dic = fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)
    camion = [lote.Lote(d["nombre"], d["cajones"], d["precio"]) for d in camion_dic]
    return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(camion, precios):
    lista = []
    for fruta in camion:
        cambio = precios[fruta.nombre] - fruta.precio
        t = (fruta.nombre, fruta.cajones, fruta.precio, cambio)
        lista.append(t)
    return lista

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    # print('    Nombre    Cajones     Precio     Cambio')
    # print('---------- ---------- ---------- ----------')
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    
    for nombre, cajones, precio, cambio in data_informe:
        # precio = f'${precio}'
        # print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt="txt"):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))
    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)
    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    
#%%
def f_principal(argumentos):
    informe_camion(argumentos[1], argumentos[2], argumentos[3])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    






