# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 23:29:05 2021

@author: amene
"""

# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            # tuve que agregar esta linea porque me tiraba error.
            d = str(d)
            print(f'{d:>10s}', end=' ')
        print()
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        string = "<tr>"
        for header in headers:
            string += f"<th>{header}</th>"
        string += "</tr>"
        print(string)
    
    def fila(self, data_fila):
        string = "<tr>"
        for data in data_fila:
            string += f"<th>{data}</th>"
        string += "</tr>"
        print(string)
        
def crear_formateador(fmt):
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formateador
    
def imprimir_tabla(lotes, atrs, formateador):
    formateador.encabezado(atrs)
    filas = []
    for lot in lotes:    
        data = [getattr(lot, atr) for atr in atrs]
        filas.append(data)      
    for linea in filas:
        formateador.fila(linea)
