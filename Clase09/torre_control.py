# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:25:40 2021

@author: amene
"""

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    

class TorreDeControl:
    """Funciona como una torre de control de un aeropuerto
    """
    
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()
        
    def nuevo_arribo(self, vuelo):
        self.arribos.encolar(vuelo)
        
    def nueva_partida(self, vuelo):
        self.partidas.encolar(vuelo)
        
    def ver_estado(self):
        if self.arribos.esta_vacia():
            print("No hay vuelos esperando a aterrizar.")
        else:
            lista = getattr(self.arribos, "items")
            linea1 = "Vuelos esperando a aterrizar:" + ','.join(lista)
            print(linea1)
        if self.partidas.esta_vacia():
            print("No hay vuelos esperando a despegar.")
        else:
            lista = getattr(self.partidas, "items")
            linea2 = "Vuelos esperando a despegar:" + ','.join(lista)
            print(linea2)
            
    def asignar_pista(self):
        if self.arribos.esta_vacia() and self.partidas.esta_vacia():
            print("No hay vuelos en espera.")
        else:
            if self.arribos.esta_vacia():
                despega = self.partidas.desencolar()
                print(f"El vuelo {despega} despegó con éxito.")
            else:
                aterriza = self.arribos.desencolar()
                print(f"El vuelo {aterriza} aterrizó con éxito.")
                
                