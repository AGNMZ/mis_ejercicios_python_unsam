# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:09:33 2021

@author: amene
"""

from datetime import date


fecha_actual = date.today()
año = fecha_actual.year
primavera_este_año = date(año, 9, 21)
primavera_prox_año = date(año+1, 9, 21)
delta_este_año = primavera_este_año - fecha_actual
delta_prox_año = primavera_prox_año - fecha_actual
dias = delta_este_año.days
if dias < 0:
    dias = delta_prox_año.days
    
print(f"Faltan {dias:d} dias para la primavera.")