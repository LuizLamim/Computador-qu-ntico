import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Configurações da Simulação ---
G = 1.0           # Constante gravitacional (simplificada)
m1 = 1.0          # Massa da partícula 1 (azul)
m2 = 1.0          # Massa da partícula 2 (vermelha)
dt = 0.05         # Passo de tempo (velocidade da simulação)
total_frames = 400 # Quantidade de quadros

# --- Condições Iniciais ---
# Posições iniciais (x, y) - separadas no eixo X
p1 = np.array([-1.0, 0.0])
p2 = np.array([1.0, 0.0])

# Velocidades iniciais (vx, vy) 
# Ajustadas para criar uma órbita circular estável
# Para massas iguais em órbita circular: v = sqrt(G*m / (2*r))
v_mag = np.sqrt(G * m1 / (2 * 1.0)) # 1.0 é a distância ao centro (raio)

v1 = np.array([0.0, -v_mag]) # Partícula 1 vai para baixo
v2 = np.array([0.0, v_mag])  # Partícula 2 vai para cima

# --- Preparação do Gráfico ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal') # Garante que os círculos não pareçam ovais
ax.grid(True, alpha=0.3)
ax.set_title("Simulação de Órbita de Duas Partículas")

# Elementos visuais
particle1, = ax.plot([], [], 'o', color='blue', ms=10, label='Massa 1')
particle2, = ax.plot([], [], 'o', color='red', ms=10, label='Massa 2')
trail1, = ax.plot([], [], '-', color='blue', alpha=0.3, lw=1)
trail2, = ax.plot([], [], '-', color='red', alpha=0.3, lw=1)
ax.legend()

# Histórico para o rastro (trail)
x1_trail, y1_trail = [], []
x2_trail, y2_trail = [], []