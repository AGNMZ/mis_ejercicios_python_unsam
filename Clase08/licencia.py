# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:01:37 2021

@author: amene
"""

from datetime import date, timedelta

licencia = date(2020,9,26)
dias = timedelta(days=200)
final = licencia + dias
print(final)