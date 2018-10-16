# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:24:00 2018

@author: Lux
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
from pylab import xticks
from sklearn import preprocessing
#rom __future__ import division

import scipy.stats
#from numpy import *
from scipy.stats import norm


#informa a amostra
amostra = [181.37984274, 154.80600659, 182.33424888, 170.32065307, 179.82634437, 168.73723578, 164.28520413, 171.93415101, 171.71090179, 177.69136458,153.38183565, 151.13269527, 166.4994225,  828.37581774 ,168.02278222, 169.29065423, 138.46062748, 174.88588464, 155.01472584, 164.27356639]
print('')

#imprime a amostra
print('amostra = ',amostra)
print('')

#imprime o número de elementos da amostra
numero_de_elementos_amostra = len(amostra)
print('número de elementos da amostra = ', numero_de_elementos_amostra)
print('')

#imprime a média da amostra
media_da_amostra = sum(amostra)/len(amostra)
print('média da amostra =', media_da_amostra) 
print('')

#imprime o desvio padrão da amostra
desvio_padrao = np.std(amostra)
print('desvio padrao = ',desvio_padrao)
print('')

#imprime a variância da amostra
variancia = desvio_padrao**2
print('variância = ',variancia)
print('')

print(sorted(amostra))
print('')

#retira o outlier
amostra.remove(828.37581774)

print('A amostra sem o outlier possui', len(amostra),'elementos')

print('')

#imprime nova média da amostra (sem o outlier)
media_da_amostra_1 = sum(amostra)/len(amostra)
print('média da amostra sem o outlier =', media_da_amostra_1) 
print('')

desvio_padrao_1 = np.std(amostra)
print('desvio padrao sem o outlier = ',desvio_padrao_1)
print('')
#plota yn histograma representativo da amostra
#print(amostra)


plt.hist (amostra, bins = 5, facecolor = 'purple', normed = 1, rwidth = 0.85, alpha = 0.5)   
plt.xlabel ('valores')
plt.ylabel ('frequência')
plt.title ('Histograma da amostra *retirado o outlier')
plt.show()

print('')

#calcula o intervalo de confiança, dado um p-valor de 5% para a amostra sem o outlier
z = 1.96
intervalo_min = media_da_amostra_1 - (z*desvio_padrao_1/sqrt(len(amostra)))
#"print(intervalo_min)

intervalo_max = media_da_amostra_1 + (z*desvio_padrao_1/sqrt(len(amostra)))
#"print(intervalo_max)

print('Intervalo de confiança:(', intervalo_min,',', intervalo_max,')')
print((intervalo_min + intervalo_max)/2)

#calcula o intervalo de confiança, dado um p-valor de 5% para a amostra na íntegra

z = 1.96
intervalo_min = media_da_amostra - (z*desvio_padrao/sqrt(len(amostra)+1))
#"print(intervalo_min)

intervalo_max = media_da_amostra + (z*desvio_padrao/sqrt(len(amostra)+1))
#"print(intervalo_max)

print('Intervalo de confiança:(', intervalo_min,',', intervalo_max,')')
print((intervalo_min + intervalo_max)/2)


