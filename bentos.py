#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:18:49 2023

@author: joao
"""

''' Análise de dados das atividades de campo da disciplina Bentologia. 
Coral azul
Semestre 2023.2
'''
import pandas as pd
import matplotlib.pyplot as plt

'''abrindo o  primeiro arquivo'''
achando_csv ='/home/joao/bentologia/annotations.csv'
df = pd.read_csv(achando_csv,sep = ',')
df=df.drop(['Aux3','Aux4','Aux5','Date'],axis=1)

cobertura=(df.groupby(["Name", "Transecto","Ponto"],as_index=False)["Label"].value_counts())
#cobertura = cobertura.reset_index()

'''adicionando uma nova coluna - cobertura em %'''
#primeiro vou apagar as linhas onde existem sarcothelia
cobertura = cobertura.drop(cobertura[cobertura['Label']=='Sarcoth'].index)
#calculando a porcentagem de cobertura agora
cobertura['cobertura de Sarcothelia %']=(30-cobertura['count'])*100/30
#apagando as colunas label e count
cobertura=cobertura.drop(['Label','count'],axis=1)
#Salvando em csv
cobertura.to_csv(path_or_buf='/home/joao/bentologia/dados_bentos_completo.csv')


'''Media e desvio de todos os pontos'''
c_med=cobertura['cobertura de Sarcothelia %'].mean()
c_desv=cobertura['cobertura de Sarcothelia %'].std()

'''media e desvio de cada ponto'''
cob_med=cobertura.groupby("Ponto",as_index=False)['cobertura de Sarcothelia %'].mean()
cob_desv=cobertura.groupby("Ponto",as_index=False)['cobertura de Sarcothelia %'].std()
#

'''Boxplot'''

grouped = cobertura.groupby(['Ponto','Transecto'])['cobertura de Sarcothelia %'].apply(list)
# Criando o boxplot
plt.boxplot(grouped.values)
# Configurações do gráfico
plt.xlabel('Ponto')
plt.ylabel('Cobertura de $\it{Sarcothelia}$ sp. %')

