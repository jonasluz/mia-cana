# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:32:54 2017
@author: Jonas de A. Luz Jr. <unifor@jonasluz.com>

Implementação do algoritmo de ordenação por inserção.
"""

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
                
    return values

# Teste 
test = [7, 8, 6, 2, 5, 4, 1, 2]
print(insertionSort(test))
print(insertionSort(test, True))