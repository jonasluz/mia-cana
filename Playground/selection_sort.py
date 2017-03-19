# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:02:54 2017

@author: Jonas Luz <unifor@jonasluz.com>

Algoritmo de ordenação por seleção.
"""
    
def selectionSort(values: list) -> list:
    """
    Ordenação por seleção, com busca pelo menor.
    """
    
    for i in range(0, len(values)):
        k = i
        for j in range(i+1, len(values)):
            if values[j] < values[k]:
                k = j
        values[i], values[k] = values[k], values[i]
        
    return values

def selectionSort2(values: list) -> list:
    """
    Ordenação por seleção, com busca pelo menor e pelo maior.
    """
    
    for i in range(0, int(len(values)/2)):
        limit = len(values)-1-i
        kmin, kmax = i, limit
        if values[kmin] > values[kmax]:
            values[kmin], values[kmax] = values[kmax], values[kmin]
        for j in range(i+1, limit):
            if values[j] < values[kmin]:
                kmin = j
            elif values[j] > values[kmax]:
                kmax = j
        values[i], values[kmin] = values[kmin], values[i]
        values[limit], values[kmax] = values[kmax], values[limit]
        
    return values
    
# Teste 
#print(selectionSort2([7, 8, 2, 6, 5, 4, 1, 2, 3, 7, 9]))