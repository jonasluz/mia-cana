# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:32:34 2017
@author: Jonas de A. Luz Jr. <unifor@jonasluz.com>
"""

def q5avaliador(participantes:list, resolvidos:list, tempos:list) -> list:
    """
    Solução da questão 5: "procedimento que, dados como entrada um vetor de 
    tamanho n com os nomes dos participantes, um vetor respectivo com a 
    quantidade de problemas resolvidos e um vetor respectivo com o tempo total 
    de execução, indica o vencedor." O procedimento deve ser Θ(n).
    """
    ## Validação inicial. Os tamanhos dos vetores têm que ser iguais. 
    # 
    assert len(participantes) == len(resolvidos), len(resolvidos) == len(tempos)
    if len(participantes) == 0:       # listas vazias.
        return None     

    melhores, maior, melhor = [], 0, float('inf')   # inicializa variáveis.
    for k, v in enumerate(resolvidos):
        if v > maior:                 # foi encontrado um valor melhor que o anterior. 
            melhores = []             # limpa a lista de "vencedores" anteriores.
            melhores.append(participantes[k]) # adiciona o índice do novo "vencedor".
            maior    = v              # atualizao o total resolvido de vencedores.
            melhor   = tempos[k]      # atualiza o melhor tempo para vencedores.
        elif v == maior:              # há mais alguém com o mesmo nº de resolvidos.
            if tempos[k] < melhor:    # novo candidadto possui tempo melhor.
                melhores = []         # limpa lista de "vencedores".
                melhores.append(participantes[k]) # adiciona o índice do novo vencedor.
                melhor = tempos[k]    # atualiza o melhor tempo para vencedores.
            elif tempos[k] == melhor: # novo candidato tem o mesmo tempo d'outros.
                melhores.append(participantes[k]) # adiciona novo candidato à lista.
    # Ao final, a lista dos índices de candidatos a vencedores está em melhores.
    
    ## Exibe e retorna o resultado.
    # 
    msg = 'O vencedor é {}' if len(melhores) == 1 else 'Os vencedores são:\n{}'
    print(msg.format(melhores))
    return(melhores)
    