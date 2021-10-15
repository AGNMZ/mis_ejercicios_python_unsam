# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:23:51 2021

@author: amene
"""

import datetime 

def vida_en_segundos(fecha_nac):
    fecha_nac_dt = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
    ahora_dt = datetime.datetime.now()
    delta_tiempo = ahora_dt - fecha_nac_dt
    segundos_vividos = delta_tiempo.total_seconds()
    return segundos_vividos
