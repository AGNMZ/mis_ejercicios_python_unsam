# -*- coding: utf-8 -*-

import os
import pandas as pd

directorio = '../Data' # Carpeta donde se encuentran los archivos

#----------

# ARBOLES CRECIDOS EN PARQUES
archivo_parques = 'arbolado-en-espacios-verdes.csv' # Nombre del archivo 

fname_parques = os.path.join(directorio,archivo_parques) # Se crea la ruta del archivo de arboles crecidos en parques

df_parques = pd.read_csv(fname_parques) # Dataframe de arboles crecidos en parques

cols_sel_parques = ['diametro' ,'altura_tot'] # Seleccion de columnas

df_tipas_parques = df_parques[df_parques['nombre_cie']=='Tipuana Tipu'][cols_sel_parques].copy() # Se seleccionan las columnas deseadas de la especie elegida

#----------

# ARBOLES CRECIDOS EN VEREDAS
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv' # Nombre del archivo

fname_veredas = os.path.join(directorio,archivo_veredas) # Se crea la ruta del archivo de arboles crecidos en veredas

df_veredas = pd.read_csv(fname_veredas) # Dataframe de arboles crecidos en veredas

cols_sel_veredas = ['diametro_altura_pecho', 'altura_arbol'] # Seleccion de columnas

df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico']=='Tipuana tipu'][cols_sel_veredas].copy() # Se seleccionan las columnas deseadas de la especie elegida

#----------

# Se renombran las columnas de diametro y altura de df_tipas_parques
df_tipas_parques.rename(columns={'diametro':'diametro_altura_pecho','altura_tot':'altura_arbol'},inplace=True)

#----------

# Agregar columnas 'ambiente' a ambos Dataframes con sus valores correspondientes
df_tipas_parques = df_tipas_parques.assign(ambiente = 'parque') # Se asigna 'parque'
df_tipas_veredas = df_tipas_veredas.assign(ambiente = 'vereda') # Se asigna 'veredas'

#----------

# Concatenacion de ambos Dataframes
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques]) # Se concatenan ambos dataframes

#----------

# Boxplots de diametros y alturas por ambientes
df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
df_tipas.boxplot('altura_arbol',by = 'ambiente')
