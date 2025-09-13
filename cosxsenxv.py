# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Cria uma sequência de valores de x de -2π a 2π
# np.linspace(start, stop, number_of_points)
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calcula os valores correspondentes de y para a função y = cos(x) * sin(x)
y = np.cos(x) * np.sin(x)

# Plota o gráfico
plt.figure(figsize=(11, 8))  # Define o tamanho da figura (largura, altura)
plt.plot(x, y, label=r'$y = \cos(x) \cdot \sin(x)$', color='red')

# Adiciona título e rótulos aos eixos
plt.title('Gráfico da Função $y = \cos(x) \cdot \sin(x)$')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

# Adiciona uma grade ao gráfico
plt.grid(True)

# Adiciona uma legenda para a linha do gráfico
plt.legend()

# Define os limites dos eixos para melhor visualização
plt.ylim(-0.6, 0.6)

# Adiciona uma linha horizontal em y=0 para destacar o eixo x
plt.axhline(0, color='black', linewidth=0.5)
# Adiciona uma linha vertical em x=0 para destacar o eixo y
plt.axvline(0, color='black', linewidth=0.5)

# Mostra o gráfico
plt.show()