import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Configurações da Simulação ---
G = 3.0           # Constante gravitacional (simplificada)
m1 = 5.0          # Massa da partícula 1 (azul)
m2 = 5.0          # Massa da partícula 2 (vermelha)
dt = 0.05         # Passo de tempo (velocidade da simulação)
total_frames = 400 # Quantidade de quadros

# --- Condições Iniciais ---
# Posições iniciais (x, y) - separadas no eixo X
p1 = np.array([-0.5, 0.0])
p2 = np.array([1.0, 0.0])

# Velocidades iniciais (vx, vy) 
# Ajustadas para criar uma órbita circular estável
# Para massas iguais em órbita circular: v = sqrt(G*m / (2*r))
v_mag = np.sqrt(G * m1 / (2 * 1.0)) # 1.0 é a distância ao centro (raio)

v1 = np.array([0.0, -v_mag]) # Partícula 1 vai para baixo
v2 = np.array([0.0, v_mag])  # Partícula 2 vai para cima

# --- Preparação do Gráfico ---
fig, ax = plt.subplots(figsize=(8, 8))
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

# --- Função de Atualização (Física) ---
def update(frame):
    global p1, p2, v1, v2
    
    # 1. Calcular o vetor distância (r) e a magnitude da distância
    r_vec = p2 - p1
    distance = np.linalg.norm(r_vec)
    
    # Evitar divisão por zero (colisão)
    if distance < 0.1: distance = 0.1
        
    # 2. Calcular a Força Gravitacional (Newton)
    # F = G * m1 * m2 / r^2
    force_mag = G * m1 * m2 / (distance**2)
    
    # Direção da força (vetor unitário)
    force_dir = r_vec / distance
    
    # Vetor Força (atração mútua)
    F_on_1 = force_mag * force_dir  # Puxa 1 em direção a 2
    F_on_2 = -F_on_1                # Puxa 2 em direção a 1 (3ª Lei de Newton)
    
    # 3. Atualizar Velocidades (F = ma -> a = F/m)
    # v_nova = v_atual + (a * dt)
    v1 += (F_on_1 / m1) * dt
    v2 += (F_on_2 / m2) * dt
    
    # 4. Atualizar Posições
    # p_nova = p_atual + (v * dt)
    p1 += v1 * dt
    p2 += v2 * dt
    
    # 5. Atualizar os Rastros
    x1_trail.append(p1[0])
    y1_trail.append(p1[1])
    x2_trail.append(p2[0])
    y2_trail.append(p2[1])
    
    # Limitar o tamanho do rastro (opcional, para não ficar muito pesado)
    limit = 50
    
    # 6. Atualizar os dados do gráfico
    particle1.set_data([p1[0]], [p1[1]])
    particle2.set_data([p2[0]], [p2[1]])
    
    trail1.set_data(x1_trail[-limit:], y1_trail[-limit:])
    trail2.set_data(x2_trail[-limit:], y2_trail[-limit:])
    
    return particle1, particle2, trail1, trail2

# --- Criar Animação ---
ani = FuncAnimation(fig, update, frames=total_frames, interval=20, blit=True)

plt.show()