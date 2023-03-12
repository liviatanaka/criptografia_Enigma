import numpy as np
import re
from unidecode import unidecode

legenda_alfabeto = list('abcdefghijklmnopqrstuvwxyz _0123456789')
matriz_alfabeto = np.identity(38)

"""Funções auxiliares para a biblioteca de criptografia enigma."""

def limpa_mensagem(msg):
    # Transforma a string para minúsculo
    msg = msg.lower()
    # Remove acentos
    msg = unidecode(msg)
    # Substitui caracteres especiais por "_"
    msg = re.sub(r'[^a-z0-9\s]', '_', msg)
    return msg

"""Funções que compõem uma biblioteca Python para criptografia usando enigma."""

""" Função | Decodifica mensagens como uma matriz usando one-hot encoding."""
def para_one_hot(msg):
    # para_one_hot(msg : str)
    msg_ = limpa_mensagem(msg)
    list_msg = list(msg_)
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
    M = M.T 
    msg = ''
    for i in range(M.shape[0]):
        index = list(M[i]).index(1)
        msg += legenda_alfabeto[index]
    return msg


""" Função | Aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada."""
# obs: 'P' é uma matriz de permutação que realiza a cifra. 
def cifrar(msg, P):
    # cifrar(msg : str, P : np.array)
    matriz_msg = para_one_hot(msg)
    matriz_cifrada = P @ matriz_msg 
    msg_cifrada = para_string(matriz_cifrada)
    return msg_cifrada


""" Função | Recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original."""
# obs: 'P' é a matriz de permutação que realiza a cifra.
def de_cifrar(msg, P):
    # de_cifrar(msg : str, P : np.array) 
    matriz_cifrada = para_one_hot(msg)
    P_inversa = np.linalg.inv(P)
    matriz_msg = P_inversa @ matriz_cifrada
    msg_limpa = para_string(matriz_msg)
    return msg_limpa


""" Função | Faz a cifra enigma na mensagem de entrada usando o cifrador `P` e o cifrador auxiliar `E`."""
# obs: ambos representados como matrizes de permutação.
def enigma(msg, P, E):
    # enigma(msg : str, P : np.array, E : np.array)

    # transforma a mensagem em matriz
    matriz_msg = para_one_hot(msg)
    matriz_enigma = np.array([np.zeros(38)]).T # coluna zerada
    for i in range(matriz_msg.shape[1]):
        coluna_letra = np.array([matriz_msg[:,i]]).T 
        letra_cifrada = P @ coluna_letra
        P = E @ P
        matriz_enigma = np.concatenate((matriz_enigma, letra_cifrada), axis=1)

    matriz_final = np.delete(matriz_enigma, 0, axis=1) # retira a coluna zerada
    msg_enigma = para_string(matriz_final)
    return msg_enigma

""" Função | Recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`."""
# obs: ambos representados como matrizes de permutação.
def de_enigma(msg, P, E):
    # de_enigma(msg : str, P : np.array, E : np.array)
    
    matriz_cifrada = para_one_hot(msg)
    matriz_msg = np.array([np.zeros(38)]).T
    for i in range(matriz_cifrada.shape[1]):
        coluna_letra = np.array([matriz_cifrada[:,i]]).T
        P_inversa = np.linalg.inv(P)
        letra_traducao = P_inversa @ coluna_letra
        P = E @ P
        matriz_msg = np.concatenate((matriz_msg, letra_traducao), axis=1)
    
    matriz_final = np.delete(matriz_msg, 0, axis=1)
    msg_enigma = para_string(matriz_final)
    return msg_enigma
