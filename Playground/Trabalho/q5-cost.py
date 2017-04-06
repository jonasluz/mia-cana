# -*- coding: utf-8 -*-
"""
calcula o custo do programa da questão 5.
Created on Wed Apr  5 14:02:49 2017
@author: Jonas
"""

import numpy as np

lines = [int(i) for i in np.linspace(1, 41, 41)]

no, zero, one, n = '-', '0', '1', 'n'

costs = [
            zero, 
            zero, 
            zero, 
            zero,
            zero, 
            zero,
            zero, 
            zero, 
            zero, 
            zero,
            zero, 
            zero,
            zero,
            zero, 
            zero,
            'c_1', 'c_2', 'c_3', no, 'c_4', # até linha 20
            'c_5', 'c_6', 'c_7', 'c_8', 'c_9', 'c_{10}',
            'c_{11}', # elif linha 27
            'c_{12}', 'c_{13}', 'c_{14}', 'c_{15}',
            '0,c_{16}', '0,c_{17}', 
            zero, no, zero, zero, 
            'c_{18} / c_{19}', 
            'c_{20}', 'c_{21}', '0, c_{22}',
        ]
qtty =  [
            zero, 
            zero, 
            zero, 
            zero,
            zero, 
            zero,
            zero, 
            zero, 
            zero, 
            zero,
            zero, 
            zero,
            zero,
            zero, 
            zero,
             one, one, '0, 1', no, one, # até linha 20
            'n+1', 'n', '0, n', '0, n', '0, n', '0, n',
            '0, n', # elif linha 27
            '0, n','0, n','0, n','0, n',
            '0, n','0, n',
            zero, no, zero, zero, 
            'm+1 / m; m \in \Z \text{ e } m \leq n', 
            one, one, one,
        ]
total = [
            zero, 
            zero, 
            zero, 
            zero,
            zero, 
            zero,
            zero, 
            zero, 
            zero, 
            zero,
            zero, 
            zero,
            zero,
            zero, 
            zero,
            'c_1', 'c_2', '0, c_3', no, 'c_4', # até linha 20
            'c_5(n+1)', 'c_6n', '0, c_7n', '0, c_8n', '0, c_9n', '0, c_{10}n',
            '0, c_{11}n', # elif linha 27
            '0,c_{12}n', '0,c_{13}n', '0,c_{14}n', '0,c_{15}n',
            '0,c_{16}n', '0,c_{17}n', 
            zero, no, zero, zero, 
            'c_{18}(m+1) / c_{19}m; m \in \Z \text{ e } m \leq n', 
            'c_{20}', 'c_{21}', '0, c_{22}',
        ]

print('{}\n{}\n{}\n{}'.format(len(lines), len(costs), len(qtty), len(total)))
for k, l in enumerate(lines):
    print('{}\t& ${}$\t& ${}$\t& ${}$ \\\\'.format(l, costs[k], qtty[k], total[k]))
