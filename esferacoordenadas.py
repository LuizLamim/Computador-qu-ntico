import matplotlib.pyplot as plt
import numpy as np

def plotar_esfera(raio=1):
    fig = plt.subplots(figsize=(8, 8), subplot_kw={'projection': '3d'})
    ax = fig[1]

    # Criando os dados para a esfera (coordenadas esféricas)
    # u varia de 0 a 2*pi (longitude)
    # v varia de 0 a pi (latitude)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    # Conversão para coordenadas cartesianas
    x = raio * np.outer(np.cos(u), np.sin(v))
    y = raio * np.outer(np.sin(u), np.sin(v))
    z = raio * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plotando a superfície
    # 'cmap' define a cor (magma, viridis, ocean, etc)
    # 'alpha' define a transparência
    ax.plot_surface(x, y, z, color='skyblue', edgecolor='k', alpha=0.6, linewidth=0.1)

    # Ajustando os limites para manter o aspecto de esfera
    max_range = raio
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(-max_range, max_range)

    ax.set_title(f'Esfera 3D com Raio = {raio}')
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    plt.show()

if __name__ == "__main__":
    plotar_esfera(raio=5)