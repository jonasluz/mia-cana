# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:54:27 2017
@author: Jonas de A Luz Jr. <unifor@jonasluz.com>
"""

def q6recmenor(a:list, p:int=None, r:int=None) -> int:
    """
    Solução da questão 6: "Seja um vetor A de n elementos inteiros. É possível 
    determinar a posição do menor elemento do vetor em Θ(n) percorrendo-se os 
    elementos do vetor de forma iterativa. Alternativamente, podese utilizar um 
    método de divisão-e-conquista. Faça uma função para determinar a posição do 
    menor elemento do vetor. O algoritmo deve recursivamente dividir o vetor em 
    duas partes de tamanhos aproximadamente iguais até se chegar a um caso 
    trivial." 
    """
    ## Atualiza valores default para os limites da ordenação.
    #
    if p == None:                   # sem limites do vetor - pegá-lo completo.                 
        assert r == None
        p, r = 0, len(a) - 1        # marca os limites do vetor completo.

    ## Chamadas recursivas da verificação do menor valor.
    #
    if p < r:
        s = int((p+r)/2)               # calcula ponto intermediário do vetor.
        il = q6recmenor(a, p, s)       # verifica lado esquerdo.
        ir = q6recmenor(a, s+1, r)     # verifica lado direito.
        return il if a[il] < a[ir] else ir # retorna o menor dos valores.
    
    return p         # caso trivial, vetor unitário, retorna único índice.