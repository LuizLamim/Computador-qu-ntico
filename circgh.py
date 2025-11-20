import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Configura a figura e o eixo
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', adjustable='box')

# Cria o círculo inicial (um ponto no centro)
circle, = ax.plot([], [], 'o', markersize=0) # 'o' para círculo, markersize para o tamanho

# Função de inicialização: desenha um plano de fundo em branco
def init():
    circle.set_data([], [])
    return circle,

