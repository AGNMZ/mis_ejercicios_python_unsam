# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:26:53 2021

@author: amene
"""

import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
dh = df['12-25-2014':].copy()
# saque el valor de delta_h viendo las diferencias entre dos picos.
# el valor de delta_t lo saque con prueba y error.
delta_t = -1
delta_h = 163.475 - 144.9125
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()