# -*- coding: utf-8 -*-

##  Main.py
#   Código de apoio à execução do tabalho.
#   Por Jonas de A. Luz Jr. 
#

from q5 import *
from q6 import *

import merge_sort as sort

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

g_y0, g_ylim = 0, 10

def plotItem(item):
    """
    Configura e mostra o gráfico do item indicado.
    """
    
    global g_y0, g_ylim
    
    fig, ax = plt.subplots()
    plt.xlim(0, 5)
    plt.ylim(g_y0, g_ylim)
    plt.xlabel('$n$')
    plt.ylabel('$f(n), g(n)$')
    plt.title('Item {}'.format(item))
     
    n = np.linspace(0, 10, 100)
    
    values = {
         '1a': (n**5, n, '\Theta(n^5)', '\Theta(n)', None, None, False),
         '1b': (n**3, n, '\Omega(n^3)', 'O(n)', False, True, False),
         '1c': (n**4, n**2, '\Omega(n^4)', '\Omega(n^2)', False, False, False),
         '1d': (n**5, n**2, 'O(n^5)', '\Omega(n^2)', True, False, False),
         '1e': (n**2, n**3, 'O(n^2)', '\Omega(n^3)', True, False, True),
         '1f': (n, n**2, 'O(n)', 'O(n^2)', True, True, True),
         '1g': (n**3, n**2, '\Omega(n^3)', 'O(n^2)', False, True, True),
         '1h': (n**4, n, '\Omega(n^4)', 'O(n)', False, True, False),
         '2a': (2**(2*n+1), 3**(3*n), '2^{2n+1}', '3^{3n}', None, True, False),
         '2b': ((4*n-5)**10, n**10, '(4n-5)^{10}', 'n^{10}', None, False, False),
         '2c': (2*n**3, n**2, '2n^3', 'n^2', None, True, False),
         '2d-O': (4*n**6+3*n**5-4*n**3+2*n**2-n, 9*n**6, '4n^6+3n^5-4n^3+2n^2-n', 'c.n^6, c=9', None, True, False),
         '2d-Ω': (4*n**6+3*n**5-4*n**3+2*n**2-n, 3*n**6, '4n^6+3n^5-4n^3+2n^2-n', 'c.n^6, c=3', None, False, False),
         #'01': (-2*n**2, -4*n**2+2*n, '-2n^2', '-4n^2+2n', None, None, False),
         #'01': (-n, 2*n-1, '-n', '2n-1', None, None, False),
         #'01': (-6*n**2, -4*n**2-n, '-6n^2', '-4n^2-n', None, None, False),
         #'01': (-3*n**4, 3*n**4-6*n**2, '-3n^4', '3n^4-6n^2', None, None, False),
         '01': (2*n**5, 4*n**5-3*n**4, '2n^5', '4n^5-3n^4', None, None, False),
         }
    a, b, labelA, labelB, fillOA, fillOB, doubt = values[item]
    
    ax.plot(n, a, label='$A={}$'.format(labelA))
    ax.plot(n, b, label='$B={}$'.format(labelB))
    if fillOA != None:
        y1, y2 = (0, a) if fillOA else (a, 10)
        ax.fill_between(n, y1, y2, alpha=0.5)
    if fillOB != None:
        y1, y2 = (0, b) if fillOB else (b, 10)
        ax.fill_between(n, y1, y2, alpha=0.5)
    if doubt:
        ax.fill_between(n, 0, 10, alpha=0.2)
    
    ax.legend(loc='upper right', shadow=True)
    plt.show()

def doQuestion(question):
    """
    Executa as operações para a questão indicada.
    """
    
    global g_y0, g_ylim
    
    if question == 1:       # Questão #1
        g_ylim = 10
        plotItem('1a')
        plotItem('1b')
        plotItem('1c')
        plotItem('1d')
        plotItem('1e')
        plotItem('1f')
        plotItem('1g')
        plotItem('1h')

    elif question == 2:
        g_ylim = 1000
        plotItem('2a')
        plotItem('2b')
        g_ylim = 10
        plotItem('2c')
        g_ylim = 10000
        plotItem('2d-O')
        g_ylim = 1000
        plotItem('2d-Ω')

    elif question == 5:
        import random
        candidatos = [
                'Joaquim José da Silva Xavier',
                'Pedro Álvares de Alencar',
                'Luiz C Bonaparte Peixoto',
                'Claudio Emanuel da Silva',
            ]
        cumpridos  = random.sample(range(100), 4)
        cumpridos[3] = cumpridos[1] # adiciona um repetido.
        tempos     = random.sample(range(100), 4)
        #tempos[2] = tempos[0]       # adiciona um repetido. 
        tempos[3] = tempos[1]       # adiciona um repetido. 
        #tempos = cumpridos = [0,0,0,0]
        print('Avaliando os candidatos, algoritmos executados e tempos respectivos:')
        for k, n in enumerate(candidatos):
            print('{} \t\t- {} em {}t'.format(n, cumpridos[k], tempos[k]))
        q5avaliador(candidatos, cumpridos, tempos)
        
    elif question == 6:
        import random
        a = random.sample(range(100), 50)
        i = q6recmenor(a)
        print ('Índice encontrado: {} com valor {}'.format(i, a[i]))
        sort.mergeSort(a)
        print(a[0])
        
    elif question == 0:
        g_y0, g_ylim = -100, 100
        plotItem('01')
        
## ROTINA PRINCIPAL
#

#doQuestion(0) # Comparação de funções.
#doQuestion(1)
#doQuestion(2)
#doQuestion(5)
doQuestion(6)