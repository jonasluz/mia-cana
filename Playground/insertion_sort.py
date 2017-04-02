# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:32:54 2017
@author: Jonas de A. Luz Jr. <unifor@jonasluz.com>

Implementação do algoritmo de ordenação por inserção.
"""

import random 

def insertionSort(values: list, reverse=False) -> list:
    """ 
    Ordenação por inserção, modo tradicional.
    """
    
    k = None
    for j in range(1, len(values)):
        k = values[j]
        i = j-1
        while i >= 0 and (values[i] < k if reverse else values[i] > k):
            values[i+1] = values[i]
            i-=1
        values[i+1] = k
                
    return(values)

def insertionSort2(values:list, i=None) -> list:
    """
    Ordenação por inserção, recursiva.
    """
    ## Ajusta valor default de i.
    # 
    if i == None : i = len(values)-1
    
    ## Rotina de ordenação por inserção.
    # 
    if i > 0:
        insertionSort2(values, i-1)
        k = values[i] ; i-=1
        while i >= 0 and values[i] > k:
            values[i+1] = values[i]
            i-=1
        values[i+1] = k

    return(values)
    
## TESTES
#
data = random.sample(range(100), 13)
print('Sequencia a ordenar:\n{}\n'.format(data))

d1 = insertionSort(data.copy())
print('Sequencia ordenada por inserção:\n{}\n'.format(d1))
d2 = insertionSort2(data.copy())
print('Sequencia ordenada por inserção recursiva:\n{}\n'.format(d2))
