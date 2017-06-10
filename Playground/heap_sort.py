# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:18:25 2017

@author: Jonas de A. Luz Jr. <unifor@jonasluz.com>
"""

import numpy as np

def parent(i): 
    """
    Calcula o índice pai do índice dado
    """
    return i >> 1 if i > 1 else None

def left(i, heapsize=None):
    """
    Calcula o nó filho à esquerda.
    """
    res = i << 1
    if heapsize != None and res > heapsize:
        return None
    return res

def right(i, heapsize=None):
    """
    Calcula o nó filho à direita.
    """
    res = (i << 1) + 1
    if heapsize != None and res > heapsize:
        return None
    return res

def maxHeapify(A, heapsize, i=1):
    """
    Mantém a propriedade de max-heap.
    """
    l = left(i, heapsize)      # nó filho esquerdo.
    r = right(i, heapsize)     # nó filho direito.
    if l == None:
        return                 # nó i é folha.
    
    m = i                      # máximo default é o i.
    if A[l-1] > A[m-1]:
        m = l                  # nó esquerdo é maior.
    if r != None and A[r-1] > A[m-1]:
        m = r                  # nó direito é maior.
    if m != i:                 # troca valores entre i e m
        A[i-1], A[m-1] = A[m-1], A[i-1]
        maxHeapify(A, heapsize, m)

def buildMaxHeap(A, heapsize=None):
    """
    Constrói um max-heap
    """
    if heapsize == None:
        heapsize = len(A)
    for i in range(int(heapsize/2), 0, -1):
        maxHeapify(A, heapsize, i)
        
def heapSort(A):
    """
    Ordena o array.
    """
    heapsize = len(A)
    buildMaxHeap(A, heapsize)
    for i in range(heapsize, 1, -1):
        A[0], A[i-1] = A[i-1], A[0]
        heapsize -= 1
        maxHeapify(A, heapsize, 1)

def heapMaximum(A):
    """
    Retorna o valor máximo de um maxheap.
    """
    return A[0]

def heapExtractMax(A):
    """ 
    Extrai o valor máximo de um maxheap.
    """
    if len(A) < 1:
        return None
    m = A[0]
    A[0] = A[len(A)-1]
    maxHeapify(A, len(A)-1)
    
    return m

def heapIncreaseKey(A, i, key):
    """
    Atualiza o valor indexado em i por um valor maior.
    """
    if key < A[i]:
        return
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)
        
def heapMaxInsert(A, key):
    """
    Insere um novo valor no max heap.
    """
    ## TODO
    

    
"""
Rotinas de teste
"""
idx = [1, 10, 11]
for i in idx:
    print('parent({}) = {}'.format(i, parent(i)))
    print('left({}) = {}'.format(i, left(i)))
    print('right({}) = {}'.format(i, right(i)))

tests = [
        [16,4,10,14,7,9,3,2,8,1],
        [4,1,3,2,16,9,10,14,8,7]
        ]
#maxHeapify(tests[0], 2)
buildMaxHeap(tests[1])
heapSort(tests[0])
print(tests)