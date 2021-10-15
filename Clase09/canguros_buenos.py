# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:18:06 2021

@author: amene
"""

class Canguro:
    def __init__(self, nombre, contenido_marsupio=[]):
        self.nombre = nombre
        self.contenido_marsupio = [] + contenido_marsupio
        
        
    def meter_en_marsupio(self, objeto_cualquiera):
        self.contenido_marsupio.append(objeto_cualquiera)
        
    def __str__(self):
        imprimir = f"{self.nombre} es un canguro y en su marsupio tiene {self.contenido_marsupio}"
        return imprimir
    
    def __repr__(self):
        imprimir = f"Canguro({self.nombre}, {self.contenido_marsupio}"
        return imprimir


"""
# canguro_malo.py


class Canguro:
    
    
    def __init__(self, nombre, contenido=[]):

        self.nombre = nombre
        # para arreglar el problema, en esta linea debemos agregar un .copy()
        self.contenido_marsupio = contenido

    def __str__(self):
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')

madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.
"""
# Bueno, lo que veo que ocurre es que al agregar coasas a la madre canguro, se 
# se agregan an hijo, por lo que para evitarlo, hice que contenido_marsupio sea
# una copia.
