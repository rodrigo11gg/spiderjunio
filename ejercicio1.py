# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 15:09:20 2025

@author: Rodrigo
"""

import pandas as pd
import numpy as np
datos={'Nombre':['Leonardo','Darik','Julio','Alex'], 'Calificaciones':[
    '60','70','70', '80'], 'Deportes':['Natación','Basquet', 'Fútbol', 'Fútbol'],
    'Materias':['Química','Matemática', 'Historia', 'vida']
       }
df= pd.DataFrame(datos)
print(df)
