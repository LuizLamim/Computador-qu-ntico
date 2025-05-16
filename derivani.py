import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define a função do segundo grau
def parabola(x):
    return 0.5 * x**2 - 2 * x + 1

# Define a derivada da função
def derivada_parabola(x):
    return x - 2

# Cria os dados para a parábola
x = np.linspace(-5, 9, 400)
y = parabola(x)

# Cria a figura e os eixos
fig, ax = plt.subplots()
ax.plot(x, y, label='f(x) = 0.5x² - 2x + 1')

# Ponto inicial para a reta tangente
x_tangente = -4
y_tangente = parabola(x_tangente)
derivada_atual = derivada_parabola(x_tangente)

# Define a reta tangente inicial
reta_x = np.linspace(x_tangente - 2, x_tangente + 2, 100)
reta_y = derivada_atual * (reta_x - x_tangente) + y_tangente
tangente, = ax.plot(reta_x, reta_y, color='red', label='Reta Tangente')
ponto, = ax.plot(x_tangente, y_tangente, 'ro')

# Configurações do gráfico
ax.set_xlim([-6, 10])
ax.set_ylim([-5, 15])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Animação da Reta Tangente à Parábola')
ax.legend()
ax.grid(True)

# Função para atualizar a animação
def atualizar(i):
    global x_tangente, y_tangente, derivada_atual, reta_x, reta_y

    # Calcula a nova posição da reta tangente
    x_tangente = np.linspace(-4, 8, 200)[i]
    y_tangente = parabola(x_tangente)
    derivada_atual = derivada_parabola(x_tangente)

    # Atualiza os dados da reta tangente
    reta_x = np.linspace(x_tangente - 2, x_tangente + 2, 100)
    reta_y = derivada_atual * (reta_x - x_tangente) + y_tangente
    tangente.set_data(reta_x, reta_y)
    ponto.set_data(x_tangente, y_tangente)
    return tangente, ponto

# Cria a animação
animacao = FuncAnimation(fig, atualizar, frames=200, interval=20, blit=True)

# Para salvar a animação como um GIF (requer o ImageMagick instalado)
# animacao.save('reta_tangente.gif', writer='imagemagick')

plt.show()