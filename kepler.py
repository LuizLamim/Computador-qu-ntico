import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parâmetros da Órbita ---
# Semi-eixo maior (a) - define o tamanho da elipse
a = 10.0
# Excentricidade (e) - define o quão "achatada" é a elipse (0 para círculo, próximo de 1 para elipse muito alongada)
e = 0.5
# Posição do Sol (um dos focos)
# O foco está a uma distância de a * e do centro da elipse.
# Assumimos que o centro da elipse está em (0,0) para simplificação, e o Sol está no foco direito.
sol_x = a * e
sol_y = 0.0

# --- Geração da Elipse ---
# Ângulos de 0 a 2*pi para traçar a elipse
theta = np.linspace(0, 2 * np.pi, 1000)
# Coordenadas x e y de uma elipse
x_ellipse = a * np.cos(theta)
y_ellipse = a * np.sqrt(1 - e**2) * np.sin(theta)

# --- Configuração da Animação ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.set_title("Primeira Lei de Kepler: Órbitas Elípticas")
ax.set_xlabel("Posição X")
ax.set_ylabel("Posição Y")
ax.grid(True)

# Desenha a órbita elíptica
ax.plot(x_ellipse, y_ellipse, 'k--', linewidth=0.8, label='Órbita Elíptica')
# Desenha o Sol
sun, = ax.plot(sol_x, sol_y, 'o', color='gold', markersize=15, label='Sol')
# Desenha o planeta
planet, = ax.plot([], [], 'o', color='blue', markersize=10, label='Planeta')
# Adiciona uma linha para o vetor posição (do Sol ao planeta)
line, = ax.plot([], [], 'r-', linewidth=1.5, label='Vetor Posição')

# Ajusta os limites dos eixos para que a elipse e o movimento sejam bem visíveis
ax_limit = a + (a * e) * 0.2  # Adiciona uma margem
ax.set_xlim([-ax_limit, ax_limit])
ax.set_ylim([-ax_limit, ax_limit])

ax.legend()

# --- Função de Animação ---
def animate(i):
    # Calcula a posição do planeta em um determinado ângulo (i é o índice do frame)
    # Usamos o mesmo theta da elipse para garantir que o planeta se mova ao longo dela
    current_theta = theta[i % len(theta)]

    # Coordenadas do planeta no frame atual
    planet_x = a * np.cos(current_theta)
    planet_y = a * np.sqrt(1 - e**2) * np.sin(current_theta)

    planet.set_data(planet_x, planet_y)
    line.set_data([sol_x, planet_x], [sol_y, planet_y]) # Atualiza a linha do vetor posição
    return planet, line

# Cria a animação
# frames: número de quadros (aqui usamos o número de pontos na elipse)
# interval: atraso entre os quadros em ms
# blit: otimização para redesenhar apenas o que mudou
ani = FuncAnimation(fig, animate, frames=len(theta), interval=20, blit=True)

plt.show()