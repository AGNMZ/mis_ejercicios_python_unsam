# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 22:28:21 2021

@author: amene
"""

import pandas as pd
import os

directorio = '../Data'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
fname_veredas = os.path.join(directorio, archivo_veredas)
fname_parques = os.path.join(directorio, archivo_parques)
df_v = pd.read_csv(fname_veredas)
df_p = pd.read_csv(fname_parques)
# hago esto para que sea mas sencillo en el caso de querer meter el codigo en
# una funcion
especie_v = 'Tipuana tipu'
especie_p = 'Tipuana Tipu'
nombre_col_v = 'nombre_cientifico'
nombre_col_p = 'nombre_cie'
# El copy() al final estas para no modificar el dataframe original
df_tipas_veredas = df_v[df_v[nombre_col_v] == especie_v].copy()
df_tipas_parques = df_p[df_p[nombre_col_p] == especie_p].copy()
col_v = ['altura_arbol',  'diametro_altura_pecho']
col_p = ['altura_tot', 'diametro']
#Cuando renombre de esta manera lo hacia pensando en si tenia que pasarlo a 
# una funcion. en retrospectiva necesitaria bocha de parametros.
df_tipas_parques =  df_tipas_parques.rename({col_p[0]: col_v[0], col_p[1]: col_v[1]}, axis='columns')
df_tipas_veredas['ambiente'] = 'vereda'
df_tipas_parques['ambiente'] = 'parque'
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
df_tipas.boxplot('altura_arbol',by = 'ambiente')

# Para hacer el analisis de otras especies seria necesario cambiar los valores
# de especies_v y especies_p seria mejor usar una funcion y pasarle esos paremetros,mk_: