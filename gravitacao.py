import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Parâmetros da Simulação ---
G_SIM = 1.0  # Constante gravitacional simulada (ajuste para visualização)
M_YELLOW = 1000.0  # Massa da esfera amarela central
M_BLUE1 = 10.0     # Massa da primeira esfera azul
M_BLUE2 = 15.0     # Massa da segunda esfera azul (ligeiramente diferente para variar)

# Posição inicial da esfera amarela (estacionária)
pos_yellow = np.array([0.0, 0.0])

# Posições iniciais das esferas azuis
pos_blue1_initial = np.array([10.0, 0.0])
pos_blue2_initial = np.array([0.0, -15.0]) # Em um eixo diferente e distância diferente

# Velocidades iniciais das esferas azuis (para órbitas aproximadamente circulares)
# Para uma órbita circular, v = sqrt(G*M/r)
vel_blue1_initial = np.array([0.0, np.sqrt(G_SIM * M_YELLOW / np.linalg.norm(pos_blue1_initial))])
vel_blue2_initial = np.array([np.sqrt(G_SIM * M_YELLOW / np.linalg.norm(pos_blue2_initial)), 0.0])


# Intervalo de tempo para cada passo da simulação
DT = 0.01  # Pequeno intervalo de tempo para maior precisão

# --- Variáveis de Estado ---
# Usaremos listas para armazenar as posições e velocidades atuais
# Essas serão atualizadas a cada passo da animação
current_pos_blue1 = np.copy(pos_blue1_initial)
current_vel_blue1 = np.copy(vel_blue1_initial)

current_pos_blue2 = np.copy(pos_blue2_initial)
current_vel_blue2 = np.copy(vel_blue2_initial)

# --- Funções da Física ---

def calculate_gravitational_force(m1, m2, pos1, pos2):
    """Calcula a força gravitacional exercida por m1 em m2."""
    r_vec = pos1 - pos2  # Vetor de pos2 para pos1
    r_mag = np.linalg.norm(r_vec)
    if r_mag == 0:
        return np.array([0.0, 0.0]) # Evita divisão por zero
    
    # Lei da Gravitação Universal: F = G * m1 * m2 / r^2
    # A força é um vetor na direção de r_vec normalizado
    force_mag = G_SIM * m1 * m2 / (r_mag**2)
    force_vec = force_mag * (r_vec / r_mag)
    return force_vec

def update_state(pos, vel, mass_central, pos_central, mass_self, dt):
    """Atualiza a posição e velocidade de um corpo orbitante."""
    # Calcula a força gravitacional exercida pelo corpo central
    force = calculate_gravitational_force(mass_central, mass_self, pos_central, pos)
    
    # Calcula a aceleração (F = ma => a = F/m)
    acceleration = force / mass_self
    
    # Atualiza a velocidade (v = v0 + at)
    new_vel = vel + acceleration * dt
    
    # Atualiza a posição (s = s0 + vt + 0.5at^2, mas usamos v_new * dt para simplicidade Euler)
    # Ou, mais comumente, s = s0 + v_new * dt (método de Euler-Cromer se v_new é usado)
    # ou s = s0 + v_old * dt (método de Euler simples)
    # Vamos usar a velocidade atualizada para a nova posição
    new_pos = pos + new_vel * dt
    
    return new_pos, new_vel

# --- Configuração da Animação ---
fig, ax = plt.subplots()

# Define os limites do gráfico (ajuste conforme necessário)
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.set_aspect('equal', adjustable='box') # Garante que os círculos pareçam círculos
ax.set_title('Simulação de Órbita Planetária')
ax.grid(True, linestyle='--', alpha=0.7)

# Objetos do gráfico que serão atualizados
# Usamos scatter para poder controlar o tamanho e a cor facilmente
# O 's' é o tamanho do marcador ao quadrado (área)
yellow_sphere, = ax.plot([], [], 'o', markersize=15, color='yellow', label='Estrela Central (Amarela)') # Usando plot para 'o'
blue_sphere1, = ax.plot([], [], 'o', markersize=8, color='blue', label='Planeta Azul 1')
blue_sphere2, = ax.plot([], [], 'o', markersize=10, color='dodgerblue', label='Planeta Azul 2') # Cor ligeiramente diferente

# Para desenhar as trajetórias (opcional)
trail1_x, trail1_y = [], []
trail2_x, trail2_y = [], []
line_trail1, = ax.plot([], [], '-', color='blue', alpha=0.5, lw=1)
line_trail2, = ax.plot([], [], '-', color='dodgerblue', alpha=0.5, lw=1)
MAX_TRAIL_POINTS = 200 # Número de pontos para manter no rastro

def init():
    """Função de inicialização para a animação."""
    yellow_sphere.set_data([pos_yellow[0]], [pos_yellow[1]])
    blue_sphere1.set_data([], [])
    blue_sphere2.set_data([], [])
    line_trail1.set_data([], [])
    line_trail2.set_data([], [])
    ax.legend(loc='upper right', fontsize='small')
    return yellow_sphere, blue_sphere1, blue_sphere2, line_trail1, line_trail2

def animate(i):
    """Função de animação, chamada para cada quadro."""
    global current_pos_blue1, current_vel_blue1, current_pos_blue2, current_vel_blue2
    global trail1_x, trail1_y, trail2_x, trail2_y

    # Atualiza o estado da primeira esfera azul
    current_pos_blue1, current_vel_blue1 = update_state(
        current_pos_blue1, current_vel_blue1, M_YELLOW, pos_yellow, M_BLUE1, DT
    )
    
    # Atualiza o estado da segunda esfera azul
    current_pos_blue2, current_vel_blue2 = update_state(
        current_pos_blue2, current_vel_blue2, M_YELLOW, pos_yellow, M_BLUE2, DT
    )

    # Atualiza as posições dos objetos no gráfico
    blue_sphere1.set_data([current_pos_blue1[0]], [current_pos_blue1[1]])
    blue_sphere2.set_data([current_pos_blue2[0]], [current_pos_blue2[1]])

    # Atualiza o rastro da esfera azul 1
    trail1_x.append(current_pos_blue1[0])
    trail1_y.append(current_pos_blue1[1])
    if len(trail1_x) > MAX_TRAIL_POINTS:
        trail1_x.pop(0)
        trail1_y.pop(0)
    line_trail1.set_data(trail1_x, trail1_y)

    # Atualiza o rastro da esfera azul 2
    trail2_x.append(current_pos_blue2[0])
    trail2_y.append(current_pos_blue2[1])
    if len(trail2_x) > MAX_TRAIL_POINTS:
        trail2_x.pop(0)
        trail2_y.pop(0)
    line_trail2.set_data(trail2_x, trail2_y)
    
    return yellow_sphere, blue_sphere1, blue_sphere2, line_trail1, line_trail2

# Cria a animação
# frames: número de quadros. None para rodar indefinidamente (ou até fechar a janela)
# interval: atraso entre quadros em milissegundos
# blit=True: otimiza o desenho, redesenhando apenas o que mudou.
ani = animation.FuncAnimation(fig, animate, init_func=init, 
                              frames=None, interval=20, blit=True, repeat=True)

# Exibe o gráfico
plt.tight_layout() # Ajusta o layout para evitar sobreposições
plt.show()

print("Simulação iniciada. Feche a janela do Matplotlib para terminar.")
