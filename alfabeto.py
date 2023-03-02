import copy
import numpy as np

alfabeto = []
linha_zero = [0 for _ in range(28)]
for i in range(28):
    linha = copy.deepcopy(linha_zero)
    linha[i] = 1
    alfabeto.append(linha)

matriz_alfabeto = np.array([alfabeto])