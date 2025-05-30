import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define os parâmetros da elipse
a = 2  # Semi-eixo maior
b = 1  # Semi-eixo menor
centro_x = 0
centro_y = 0

# Cria a figura e o eixo
fig, ax = plt.subplots()
ax.set_xlim(centro_x - a - 0.5, centro_x + a + 0.5)
ax.set_ylim(centro_y - b - 0.5, centro_y + b + 0.5)
ax.set_aspect('equal', adjustable='box')
ax.set_title('Animação de uma Elipse')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)

# Linha que será animada
line, = ax.plot([], [], 'r-', lw=2) # 'r-' significa linha vermelha sólida

# Função de inicialização da animação
def init():
    line.set_data([], [])
    return line,

# Função de animação (chamada para cada quadro)
def animate(i):
    # Parâmetro t para a equação paramétrica da elipse
    # i varia de 0 a num_frames-1
    # Mapeamos i para o intervalo [0, 2*pi]
    t = np.linspace(0, 2 * np.pi, 100) # Gera 100 pontos para uma elipse suave
    
    # Equações paramétricas da elipse:
    # x = centro_x + a * cos(theta)
    # y = centro_y + b * sin(theta)
    
    # Desenha a elipse progressivamente
    theta_atual = t * (i / 100.0) # Aumenta o ângulo gradualmente
    
    x = centro_x + a * np.cos(theta_atual)
    y = centro_y + b * np.sin(theta_atual)
    
    line.set_data(x, y)
    return line,

# Número de quadros da animação
num_frames = 100
# Intervalo entre os quadros em milissegundos
intervalo = 50 

# Cria a animação
ani = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=num_frames, interval=intervalo, blit=True)

# Para exibir a animação
plt.show()

# Para salvar a animação (opcional, requer ffmpeg ou similar):
# ani.save('elipse_animada.gif', writer='pillow', fps=1000/intervalo)
# ani.save('elipse_animada.mp4', writer='ffmpeg', fps=1000/intervalo)

print("Animação da elipse criada.")