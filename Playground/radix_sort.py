# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:52:57 2017

@author: Jonas de A. Luz Jr <unifor@jonasluz.com>
"""
import array

def findK(A):
    """
    Determina o valor de k, caso não seja conhecido (em geral, o é).
    """
    assert len(A) > 0
    k = A[0]
    for i in range(0, len(A)):
        if A[i] > k:
            k = A[i]

    return k

def countSort(A, k=None):
    """
    Ordenação por contagem.
    """
    if k == None: 
        # Encontra o valor de k.
        k = findK(A)
    k += 1
    
    ## Criação e inicialização dos arrays.
    #  @see http://stackoverflow.com/questions/521674/initializing-a-list-to-a-known-number-of-elements-in-python
    length = len(A)
    B, C = array.array('I',(0,)*length), array.array('I',(0,)*k)
    
    for i in range(0, length):
        C[A[i]] += 1
    
    for i in range(1, k):
        C[i] += C[i-1]
    
    for i in range(length-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    
    return list(B)

## TODO: radix sort.

"""
Rotinas de teste
"""
test = [2, 8, 7, 1, 13, 5, 6, 4]
test = countSort(test)
print(test)