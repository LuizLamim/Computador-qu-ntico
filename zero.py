import numpy as np
import matplotlib.pyplot as plt

# Cria uma matriz 4x4 de zeros usando NumPy
matriz = np.zeros((4, 4))

# Plota a matriz
fig, ax = plt.subplots()
ax.matshow(matriz, cmap='gray')

# Adiciona os valores (0) em cada célula
for (i, j), val in np.ndenumerate(matriz):
    ax.text(j, i, int(val), ha='center', va='center', color='black')

# Adiciona grades e rótulos
ax.set_xticks(np.arange(matriz.shape[1]))
ax.set_yticks(np.arange(matriz.shape[0]))
ax.set_xticklabels(np.arange(1, matriz.shape[1] + 1))
ax.set_yticklabels(np.arange(1, matriz.shape[0] + 1))
ax.set_title('Matriz 4x4 de Zeros')

# Exibe a plotagem
plt.show()