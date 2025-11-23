import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Definindo o Campo Escalar (O "Terreno")
# Vamos usar uma função com picos e vales: f(x, y) = x * exp(-x^2 - y^2)
def f(x, y):
    return x * np.exp(-x**2 - y**2)

# 2. Definindo o Gradiente (A derivada parcial)
# O gradiente é um vetor [df/dx, df/dy]
def calcula_gradiente(x, y):
    # Derivada parcial em relação a x
    df_dx = np.exp(-x**2 - y**2) * (1 - 2*x**2)
    # Derivada parcial em relação a y
    df_dy = -2 * x * y * np.exp(-x**2 - y**2)
    return np.array([df_dx, df_dy])

# --- Configuração da Visualização ---

# Criar a grade de coordenadas para o fundo (Contour Plot)
x_range = np.linspace(-2, 2, 100)
y_range = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = f(X, Y)

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('equal')

# Desenhar o mapa de contorno (as "alturas")
contour = ax.contourf(X, Y, Z, levels=20, cmap='viridis')
fig.colorbar(contour, ax=ax, label='Valor de f(x,y)')
ax.contour(X, Y, Z, levels=20, colors='k', linewidths=0.5, alpha=0.5)

# Inicializar o ponto (partícula) e a seta (vetor gradiente)
ponto, = ax.plot([], [], 'ro', markersize=8, label='Partícula') # Ponto vermelho
# Quiver é usado para desenhar vetores
vetor_seta = ax.quiver([], [], [], [], color='red', scale=5, width=0.005, label='Vetor Gradiente')

ax.set_title('Animação do Vetor Gradiente ∇f')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc='upper right')

# --- Lógica da Animação ---

# Definir o caminho que a partícula vai percorrer (um círculo neste exemplo)
frames = 100
theta = np.linspace(0, 2*np.pi, frames)
raio = 1.0
caminho_x = raio * np.cos(theta)
caminho_y = raio * np.sin(theta)

def init():
    ponto.set_data([], [])
    vetor_seta.set_UVC([], [])
    return ponto, vetor_seta

def update(frame):
    # Pega a posição atual
    x_atual = caminho_x[frame]
    y_atual = caminho_y[frame]
    
    # Atualiza a posição do ponto
    ponto.set_data([x_atual], [y_atual])
    
    # Calcula o gradiente nessa posição
    grad = calcula_gradiente(x_atual, y_atual)
    dx, dy = grad[0], grad[1]
    
    # Atualiza a posição e a direção da seta
    # set_offsets define onde a seta começa (x, y)
    vetor_seta.set_offsets([x_atual, y_atual])
    # set_UVC define as componentes do vetor (dx, dy)
    vetor_seta.set_UVC(dx, dy)
    
    return ponto, vetor_seta

# Criar a animação
anim = FuncAnimation(fig, update, frames=frames, init_func=init, blit=False, interval=50)

plt.show()