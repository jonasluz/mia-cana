# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:23:33 2017

@author: Jonas Luz Jr. <unifor@jonasluz.com>

Implementação do algoritmo de ordenação por intercalação.

"""
import sys
import numpy as np

INF = float('Inf')

def merge(a: list, p, q, r, verbose):
    """ 
    Faz a intercalação ordenada dos vetores.
    """
    global INF
    
    ## Separa os os vetores parciais
    #
    left, right = a[p:q+1], a[q+1:r+1]
    if verbose:
        print('Fazendo a intercalação dos vetores {} e {}'.
              format(left, right))
    left.append(INF)    # Adiciona marcador infinito ao final dos vetores
    right.append(INF)   # 
    
    ## Faz a intercalação ordenada
    #
    i = j = 0
    for idx in range(p, r+1):
        if (left[i] < right[j]):
            a[idx] = left[i]
            i+=1
        else: 
            a[idx] = right[j]
            j+=1

    if verbose:
        print('Resultado da intercalação: {}'.format(a[p:r+1]))
    
def mergeSort(values: list, p=None, r=None, verbose=False):
    """
    Rotina recursiva da técnica de intercalação.
    """
    
    ## Atualiza valores default para os limites da ordenação.
    #
    if p == None:                   # sem limites da lista - pegar completa.                 
        assert r == None
        p, r = 0, len(values)-1     # marca os limites da lista completa.    
    if verbose:
        print('Ordenando a lista {}'.format(values[p:r+1]))

    ## Chamadas recursivas da ordenação.
    #
    if p < r:
        q = int((p+r)/2)            # calcula ponto intermediário da lista.
        if verbose:
           print('Ponto intermediário entre {} e {} calculado: {}'.
                 format(p, r, q)) 
        mergeSort(values, p, q, verbose)    # ordena lado esquerdo.
        mergeSort(values, q+1, r, verbose)  # ordena lado direito.
        merge(values, p, q, r, verbose)     # faz a intercalação.

    return(values)

"""
TESTES
"""
import random 

data = random.sample(range(100), 13)
print('Lista a ordenar: {}\n'.format(data))

size = len(data)
#sys.setrecursionlimit(1500)

mergeSort(data)#, verbose=True)
print(data)