import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Configurações da Figura ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box') # Garante que o círculo não fique oval

# --- Limites dos Eixos ---
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])

# --- Desenhar o Círculo Unitário ---
circulo = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2, linestyle='--')
ax.add_patch(circulo)

# --- Desenhar Eixos Cartesianos ---
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)

# --- Título e Rótulos ---
ax.set_title('Animação do Ciclo Trigonométrico')
ax.set_xlabel('Cosseno (cos θ)')
ax.set_ylabel('Seno (sin θ)')

# --- Elementos para Animar ---
# Ponto no círculo
ponto_circulo, = ax.plot([], [], 'ro', markersize=8) # 'ro' para ponto vermelho
# Linha do raio
raio_linha, = ax.plot([], [], 'r-', linewidth=1.5) # Linha vermelha
# Projeção no eixo X (cosseno)
proj_x_linha, = ax.plot([], [], 'g--', linewidth=1) # Linha verde pontilhada
# Projeção no eixo Y (seno)
proj_y_linha, = ax.plot([], [], 'm--', linewidth=1) # Linha magenta pontilhada

# Texto para exibir o ângulo e os valores de seno/cosseno
texto_info = ax.text(0.02, 0.95, '', transform=ax.transAxes) # Posição relativa ao eixo

# --- Função de Inicialização da Animação ---
def init():
    ponto_circulo.set_data([], [])
    raio_linha.set_data([], [])
    proj_x_linha.set_data([], [])
    proj_y_linha.set_data([], [])
    texto_info.set_text('')
    return ponto_circulo, raio_linha, proj_x_linha, proj_y_linha, texto_info

# --- Função de Animação (chamada para cada frame) ---
def animate(i):
    # 'i' representa o número do frame, vamos usá-lo para calcular o ângulo
    angle_rad = np.radians(i)  # Ângulo em radianos (convertendo de graus para cada frame)
    angle_deg = i              # Ângulo em graus

    x = np.cos(angle_rad)
    y = np.sin(angle_rad)

    # Atualiza o ponto no círculo
    ponto_circulo.set_data([x], [y])
    # Atualiza a linha do raio
    raio_linha.set_data([0, x], [0, y])
    # Atualiza a linha de projeção no eixo X (cosseno)
    proj_x_linha.set_data([x, x], [0, y])
    # Atualiza a linha de projeção no eixo Y (seno)
    proj_y_linha.set_data([0, x], [y, y])

    # Atualiza o texto de informações
    info_text = f'Ângulo: {angle_deg:.0f}°\nSen: {y:.2f}\nCos: {x:.2f}'
    texto_info.set_text(info_text)

    return ponto_circulo, raio_linha, proj_x_linha, proj_y_linha, texto_info

# --- Criar a Animação ---
# FuncAnimation(figura, função_animacao, função_inicializacao, frames, intervalo, blit)
# frames=361 para ir de 0 a 360 graus
# interval=20 para 20ms entre cada frame (50 frames por segundo)
# blit=True para otimizar o redesenho (apenas os elementos que mudam)
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=361, interval=20, blit=True)

# --- Exibir a Animação ---
plt.grid(True)
plt.show()

# --- Para salvar a animação como um arquivo MP4 (opcional) ---
# Você precisará ter o 'ffmpeg' instalado no seu sistema para isso.
# ani.save('ciclo_trigonometrico.mp4', writer='ffmpeg', fps=50)