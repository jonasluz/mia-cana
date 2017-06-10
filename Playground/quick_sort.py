# -*- coding: utf-8 -*-
"""
Created on Sat May 20 07:20:05 2017

@author: Jonas de A. Luz Jr <unifor@jonasluz.com>
"""

import random

def partition(A, p, r):
    """
    Particiona o vetor.
    """
    x = A[r]
    i = p - 1
    for j in range(p, r): # de p a r-1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i] # troca valores
    A[i+1], A[r] = A[r], A[i+1]     # troca valores

    return i + 1

def randomPartition(A, p, r):
    """
    Versão aleatória do particionamento.
    """
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)
    
def quickSort(A, p=0, r=None):
    """
    Ordena o subvetor em A de p a r.
    """
    if r == None:
        r = len(A) - 1 
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def randomQuickSort(A, p=0, r=None):
    """ 
    Versão aleatória do quick sort.
    """
    if r == None:
        r = len(A) - 1 
    if p < r:
        q = randomPartition(A, p, r)
        randomQuickSort(A, p, q-1)
        randomQuickSort(A, q+1, r)
        
    
"""
Rotinas de teste
"""
test = [2, 8, 7, 1, 3, 5, 6, 4]
#quickSort(test)
randomQuickSort(test)
print(test)