import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib.animation import FuncAnimation

# Parâmetros do IFS para a samambaia de Barnsley
probabilidades = [0.01, 0.85, 0.07, 0.07]
transformacoes = [
    np.array([[0.00, 0.00, 0.00],
              [0.00, 0.16, 0.00],
              [0.00, 0.00, 1.00]]),
    np.array([[0.85, 0.04, 0.00],
              [-0.04, 0.85, 1.60],
              [0.00, 0.00, 1.00]]),
    np.array([[0.20, -0.26, 0.00],
              [0.23, 0.22, 1.60],
              [0.00, 0.00, 1.00]]),
    np.array([[-0.15, 0.28, 0.00],
              [0.26, 0.24, 0.44],
              [0.00, 0.00, 1.00]])
]

# Número de pontos a serem gerados em cada quadro
pontos_por_quadro = 1000

# Número total de quadros na animação
num_quadros = 100

# Inicializa a figura e os eixos
fig, ax = plt.subplots()
scatter = ax.scatter([], [], s=1, color='green')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)
ax.axis('off')

# Função para gerar os pontos do fractal para cada quadro
def gerar_pontos(num_pontos):
    x, y = 0, 0
    pontos_x = []
    pontos_y = []
    for _ in range(num_pontos):
        prob = random.random()
        cumulative_prob = 0.0
        for i, p in enumerate(probabilidades):
            cumulative_prob += p
            if prob < cumulative_prob:
                transformacao = transformacoes[i]
                x_novo = transformacao[0, 0] * x + transformacao[0, 1] * y + transformacao[0, 2]
                y = transformacao[1, 0] * x + transformacao[1, 1] * y + transformacao[1, 2]
                x = x_novo
                pontos_x.append(x)
                pontos_y.append(y)
                break
    return pontos_x, pontos_y

# Função de animação
def animate(i):
    pontos_x_quadro, pontos_y_quadro = gerar_pontos(pontos_por_quadro)
    scatter.set_offsets(np.c_[pontos_x_quadro, pontos_y_quadro])
    return scatter,

# Cria a animação
ani = FuncAnimation(fig, animate, frames=num_quadros, interval=50, blit=True)

# Salva a animação como um GIF (requer o ImageMagick instalado)
# ani.save('fractal_folha.gif', writer='imagemagick', fps=30)

# Ou mostra a animação na tela
plt.show()