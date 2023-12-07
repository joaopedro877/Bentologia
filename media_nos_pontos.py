#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:34:04 2023

@author: joao
"""

import pandas as pd
import matplotlib.pyplot as plt

'''abrindo o  primeiro arquivo'''
achando_csv ='/home/joao/bentologia/annotations.csv'
df = pd.read_csv(achando_csv,sep = ',')
df=df.drop(['Aux3','Aux4','Aux5','Date'],axis=1)

cobertura=(df.groupby(["Ponto"])["Label"].value_counts())
cobertura=cobertura.unstack(level='Label')
cobertura2=cobertura.T

labels=cobertura2.index.values.tolist()
cob3=(cobertura2/cobertura2.sum())*100

cob3.to_csv(path_or_buf='/home/joao/bentologia/cobertura_nos_pontos.csv')
