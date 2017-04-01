# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:23:33 2017

@author: Jonas Luz Jr. <unifor@jonasluz.com>

Implementação do algoritmo de ordenação por intercalação.

"""
import sys
import numpy as np

def merge(a: list, p, q, r, verbose):
    """ 
    Faz a intercalação ordenada dos vetores.
    """
    # Determina os vetores parciais
    left, right = a[p:q+1], a[q+1:r+1]
    if verbose:
        print('Fazendo a intercalação dos vetores {} e {}'.
              format(left, right))
        
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1

    if verbose:
        print('Resultado da intercalação: {}'.format(result))
    
    # Substitui valores no vetor original pelos ordenados.
    assert r-p+1 == len(result)
    for i in range(0,len(result)):
        a[p+i] = result[i]

def mergeSort(values: list, p=None, r=None, verbose=False):
    """
    Rotina recursiva da técnica de intercalação.
    """
    if p == None:                   # sem limites da lista - pegar completa.                 
        assert r == None
        p, r = 0, len(values)-1     # marca os limites da lista completa.    
    if verbose:
        print('Ordenando a lista {}'.format(values[p:r+1]))

    if p == r:                      # condição de parada da recursão.
        if verbose:
            print('Condição de parada atingida para ordenação de {}'.
                  format([values[p]]))
        return()
    else:
        q = p+int((r-p)/2)          # calcula ponto intermediário da lista.
        if q < 0: sys.exit(-1)
        if verbose:
            print('Ponto intermediário entre {} e {} calculado: {}'.
                  format(p, r, q))
        # Ordena lado esquerdo.
        mergeSort(values, p, q, verbose)
        #Ordena lado direito.
        mergeSort(values, q+1, r, verbose)
        # faz a intercalação
        merge(values, p, q, r, verbose)
        return()
    
"""
TESTES
"""
import random 

data = random.sample(range(100), 13)
print('Lista a ordenar: {}\n'.format(data))

size = len(data)
#sys.setrecursionlimit(1500)

mergeSort(data, verbose=True)
print(data)