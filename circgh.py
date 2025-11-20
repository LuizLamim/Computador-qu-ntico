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

# Função de animação: será chamada em cada quadro
def animate(i):
    # Calcula o raio do círculo com base no quadro atual
    radius = i * 0.05
    if radius > 1.5: # Limita o tamanho máximo do círculo
        radius = 1.5

    # Cria os dados para desenhar um círculo
    theta = np.linspace(0, 2*np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    circle.set_data(x, y)
    circle.set_markersize(0) # Não queremos marcadores, apenas a linha

    return circle,

# Cria a animação
ani = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=60, interval=50, blit=True)

plt.title("Animação de um Círculo Sendo Gerado")
plt.show()