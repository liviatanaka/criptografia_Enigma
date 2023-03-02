import numpy as np
from matriz_alfabeto import matriz_alfabeto, legenda_alfabeto


"""Funções que compõem uma biblioteca Python para criptografia usando enigma."""

""" Função | Decodifica mensagens como uma matriz usando one-hot encoding."""
def para_one_hot(msg):
    # para_one_hot(msg : str)

    list_msg = list(msg)
    one_hot = np.array([np.zeros(38)])
    for l in list_msg:
        index = legenda_alfabeto.index(l)
        lista = matriz_alfabeto[index]
        one_hot = np.concatenate([one_hot, [lista]])

    matriz_one_hot = np.delete(one_hot, 0, axis=0).T
    return matriz_one_hot

""" Função | Converte mensagens da representação one-hot encoding para uma string legível."""
def para_string(M):
    # para_string(M : np.ndarray)

    

""" Função | Aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada."""
# obs: 'P' é uma matriz de permutação que realiza a cifra. 
def cifrar(msg, P):
    # cifrar(msg : str, P : np.array)
    pass

""" Função | Recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original."""
# obs: 'P' é a matriz de permutação que realiza a cifra.
def de_cifrar(msg, P):
    # de_cifrar(msg : str, P : np.array) 
    pass

""" Função | Faz a cifra enigma na mensagem de entrada usando o cifrador `P` e o cifrador auxiliar `E`."""
# obs: ambos representados como matrizes de permutação.
def enigma(msg, P, E):
    # enigma(msg : str, P : np.array, E : np.array)
    pass

""" Função | Recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`."""
# obs: ambos representados como matrizes de permutação.
def de_enigma(msg, P, E):
    # de_enigma(msg : str, P : np.array, E : np.array)
    pass
