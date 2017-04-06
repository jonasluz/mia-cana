# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:14:37 2017
@author: Jonas de A. Luz Jr. <unifor@jonasluz.com>
"""
from enum import Enum 

Tecnica = Enum('Tecnica', 'recursao formula')
    
def q7piramidal4(n:int, tecnica:Tecnica) -> int:
    """
    Retorna o número piramidal quadrado.
    """
    if tecnica == Tecnica.recursao:
        if n == 1   : return 1
        else        : return q7piramidal4(n-1, tecnica) + n**2
    elif tecnica == Tecnica.formula:
        return int(((2*n + 1)*n*(n+1))/6)

def q7puzzle(n:int) -> int:
    """
    Análise da questão 7. Impementação executável do algoritmo para análise.
    """
    sum = 0
    for i in range(1, n+1):     # em Python, o limite direito de range não entra.
        for j in range(1, n+1):
            for k in range(j, n+1):
                sum += k
    return sum

def main(m:int):
    for n in range(1,m+1):
        #piramidal4 = q7piramidal4(n, Tecnica.formula) 
        piramidal4 = q7piramidal4(n, Tecnica.recursao)
        puzzle = q7puzzle(n)
        relacao = puzzle / piramidal4
        print('Para n = {}: piramidal quadrado = {}\te o mistério = {}.\tA razão: {}.'.
              format(n, piramidal4, puzzle, relacao))

main(10)