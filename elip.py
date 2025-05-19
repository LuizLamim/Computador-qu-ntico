import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def plot_ellipse(center_x, center_y, semi_major, semi_minor, angle=0, color='blue', alpha=1.0):
    """
    Plota uma elipse usando matplotlib.

    Args:
        center_x (float): Coordenada x do centro da elipse.
        center_y (float): Coordenada y do centro da elipse.
        semi_major (float): Raio maior da elipse.
        semi_minor (float): Raio menor da elipse.
        angle (float, optional): Ângulo de rotação da elipse em graus (anti-horário). Defaults to 0.
        color (str, optional): Cor da elipse. Defaults to 'blue'.
        alpha (float, optional): Nível de transparência da elipse (0 a 1). Defaults to 1.0.
    """
    ellipse = patches.Ellipse((center_x, center_y), 2 * semi_major, 2 * semi_minor, angle=angle,
                              edgecolor=color, facecolor='none', alpha=alpha)
    fig, ax = plt.subplots(1)
    ax.add_patch(ellipse)
    ax.set_aspect('equal', adjustable='box') # Garante que a elipse não pareça deformada
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_title("Elipse")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # Exemplo 1: Elipse simples no centro
    plot_ellipse(0, 0, 5, 3)

    # Exemplo 2: Elipse com centro deslocado e cor diferente
    plot_ellipse(2, 1, 4, 2, color='red')

    # Exemplo 3: Elipse rotacionada e transparente
    plot_ellipse(-3, -2, 6, 2, angle=45, color='green', alpha=0.5)