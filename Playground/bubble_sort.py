# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:38:56 2017

@author: Jonas Luz Jr. <unifor@jonasluz.com>

Implementação do algoritmo de ordenação do método da bolha... bubblesort.

"""

def bubbleSort(values: list) -> list:
    """
    Método de ordenação da bolha (ineficiente).
    """
    
    for i in range(0, len(values)-1):
        for j in range(len(values)-1, i, -1):
            if values[j] < values[j-1]:
                values[j], values[j-1] = values[j-1], values[j]
                
    return values

## Test
#
print(bubbleSort([1,5,2,10,4,7,9,3,2,6,0,12]))
