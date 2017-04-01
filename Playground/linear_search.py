# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 18:05:45 2017

@author: Jonas <unifor@jonasluz.com>
"""

def linearSearch(data:list, item):
    """
    Algoritmo de busca linear.
    """
    for k, v in enumerate(data):
        if v == item:
            return(k)
        
    return(-1) # não encontrado.

## TESTES
#
data     = [2,5,6,7,6,3,2,5,5,3454,45,2,234,2,2487,687,68,76,8678,76,4324,23]
searches = [234, 500]
for search in searches:
    p = linearSearch(data, search)
    msg = '{} foi encontrado na posição {}.' if p >= 0 else '{} não foi encontrado (resultado {})'
    print(msg.format(search, p))