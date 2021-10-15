# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:11:58 2021

@author: amene
"""

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        cost = self.cajones * self.precio
        return cost
    
    def vender(self, vendido):
        self.cajones -= vendido
        
    def __repr__(self):
        return f"Lote({self.nombre}, {self.cajones}, {self.precio})"