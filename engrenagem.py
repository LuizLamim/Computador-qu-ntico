import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def create_gear_points(num_teeth=12, outer_radius=1.0, inner_radius=0.7, tooth_width_factor=0.5):
    """
    Gera os pontos para desenhar uma engrenagem.
    """
    angles = np.linspace(0, 2 * np.pi, num_teeth * 4, endpoint=False)
    points = []
    for i, angle in enumerate(angles):
        # A cada 4 pontos, alternamos entre raio externo e interno para criar os dentes
        if i % 4 == 0 or i % 4 == 1:
            r = outer_radius
        else:
            r = inner_radius
        
        # Ajusta ligeiramente a largura do dente
        if i % 2 == 0:
            current_angle = angle
        else:
            current_angle = angle + (2 * np.pi / (num_teeth * 4)) * tooth_width_factor
        
        points.append((r * np.cos(current_angle), r * np.sin(current_angle)))
    return np.array(points)

# Configuração da figura e dos eixos
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Cria os pontos da engrenagem
gear_points = create_gear_points()
line, = ax.plot([], [], 'k-', lw=2)

# Função de inicialização da animação
def init():
    line.set_data([], [])
    return line,

# Função de atualização para cada quadro da animação
def animate(frame):
    angle = np.radians(frame * 5)  # Gira 5 graus por quadro
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    rotated_points = np.dot(gear_points, rotation_matrix.T)
    line.set_data(rotated_points[:, 0], rotated_points[:, 1])
    return line,

# Cria a animação
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=72, interval=50, blit=True)

plt.show()

