import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. Configurações Físicas ---
k = 10.0       # Constante elástica da mola (N/m)
m = 1.0        # Massa (kg)
A = 2.0        # Amplitude do movimento (m)
omega = np.sqrt(k / m)  # Frequência angular

# --- 2. Função para desenhar a mola (Visual) ---
def get_spring_coords(start_x, start_y, end_x, end_y, nodes=15, width=0.5):
    """
    Gera as coordenadas x e y para desenhar uma mola em ziguezague.
    """
    # Cria pontos linearmente espaçados entre o início e o fim
    x_data = np.linspace(start_x, end_x, nodes)
    y_data = np.linspace(start_y, end_y, nodes)
    
    # Adiciona o desvio lateral (ziguezague) apenas nos nós internos
    # Usamos uma onda senoidal ou alternância simples para simular as espiras
    offsets = np.zeros(nodes)
    offsets[1:-1] = width * ((np.arange(nodes-2) % 2) * 2 - 1)
    
    # Como a mola é vertical, o offset é aplicado no eixo X
    x_data += offsets
    
    return x_data, y_data

# --- 3. Configuração do Gráfico ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-6, 1)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Simulação: Oscilador Massa-Mola")

# Elementos gráficos (Mola, Massa e Teto)
line_spring, = ax.plot([], [], 'k-', lw=2)  # Linha da mola (preta)
point_mass, = ax.plot([], [], 'ro', markersize=25, markeredgecolor='black') # Massa (bola vermelha)
ax.plot([-2, 2], [0, 0], 'k-', lw=5) # Teto fixo

# --- 4. Função de Atualização da Animação ---
def update(frame):
    t = frame * 0.05  # Passo de tempo
    
    # Equação do Movimento Harmônico Simples: y(t) = -L_eq + A * cos(omega * t)
    # L_eq é o comprimento de equilíbrio (para centralizar a animação visualmente)
    L_eq = 3.0
    y_pos = -L_eq + A * np.cos(omega * t)
    
    # Atualiza a posição da massa
    point_mass.set_data([0], [y_pos])
    
    # Atualiza o desenho da mola (do teto até a massa)
    xs, ys = get_spring_coords(0, 0, 0, y_pos)
    line_spring.set_data(xs, ys)
    
    return line_spring, point_mass

# --- 5. Executar Animação ---
ani = FuncAnimation(fig, update, frames=200, interval=20, blit=True)

plt.xlabel("Posição X")
plt.ylabel("Posição Y")
plt.show()