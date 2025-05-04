import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define as dimensões do retângulo
altura_retangulo = 2
largura_retangulo = 1

# Define o número de quadros para a animação
num_frames = 100

# Cria a figura e o eixo
fig, ax = plt.subplots()
ax.set_xlim(-largura_retangulo - 0.5, largura_retangulo + 0.5)
ax.set_ylim(-altura_retangulo / 2 - 0.5, altura_retangulo / 2 + 0.5)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Inicializa o retângulo que será rotacionado
retangulo, = ax.plot([], [], 'b-', linewidth=2)

# Inicializa as linhas que formam o cilindro
num_linhas = 20
linhas_cilindro = [ax.plot([], [], 'r-', linewidth=0.5, alpha=0.5)[0] for _ in range(num_linhas)]

# Função para inicializar a animação
def init():
    retangulo.set_data([], [])
    for linha in linhas_cilindro:
        linha.set_data([], [])
    return [retangulo] + linhas_cilindro

# Função para atualizar cada quadro da animação
def animate(i):
    angulo = 2 * np.pi * i / num_frames

    # Calcula as coordenadas do retângulo rotacionado
    x_ret = [-largura_retangulo / 2 * np.cos(angulo),
             largura_retangulo / 2 * np.cos(angulo),
             largura_retangulo / 2 * np.cos(angulo),
             -largura_retangulo / 2 * np.cos(angulo),
             -largura_retangulo / 2 * np.cos(angulo)]
    y_ret = [-altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo),
             -altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo),
             altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo),
             altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo),
             -altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo)]
    retangulo.set_data(x_ret, y_ret)

    # Calcula as coordenadas das linhas que formam o cilindro
    for j, linha in enumerate(linhas_cilindro):
        theta = 2 * np.pi * j / num_linhas
        x_cil = [largura_retangulo / 2 * np.cos(angulo), largura_retangulo / 2 * np.cos(angulo + 2 * np.pi)]
        y_cil = [-altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo),
         -altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo)] + [j * (altura_retangulo / (num_linhas - 1))]
        linha.set_data(x_cil * np.cos(theta) - y_cil * np.sin(theta),
                       x_cil * np.sin(theta) + y_cil * np.cos(theta))

    return [retangulo] + linhas_cilindro

# Cria a animação
ani = FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=50, blit=True)

# Salva a animação como um GIF (opcional - requer o ImageMagick instalado)
# ani.save('cilindro_revolucao.gif', writer='imagemagick')

# Exibe a animação
plt.show()