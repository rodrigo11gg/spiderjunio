# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 15:09:20 2025

@author: Rodrigo
"""

import pandas as pd
import numpy as np

datos = {
    'Nombre': ['Leonardo', 'Darik', 'Julio', 'Alex'],
    'Calificaciones': ['60', '70', '70', '80'],
    'Deportes': ['Natación', 'Basquet', 'Fútbol', 'Fútbol'],
    'Materias': ['Química', 'Matemática', 'Historia', 'vida']
}

df = pd.DataFrame(datos)

print(df)
print('\n') 
print(df)
print('\n')

datos2 = {
    'Nombre': ['Darik', 'Julio', 'Alex', 'N/A'],
    'Calificaciones': ['60', '70', '70', np.nan],
    'Deportes': ['Natación', 'Basquet', 'Fútbol', 'Fútbol'],
    'Materias': ['Química', 'Matemática', 'Historia', 'vida']
}
df2 = pd.DataFrame(datos2)

print(df2)
print(df2.info())
print(df2.describe())

# Reemplazar NaN con "0"
nuevo = df2.replace(np.nan, "0")
nuevo['Calificaciones']= nuevo.Calificaciones.astype(int)
print(nuevo.describe())
print(nuevo.info())
print(nuevo)






