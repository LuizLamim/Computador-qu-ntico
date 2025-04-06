import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def definir_funcao():
    
    def f(x, y, z):
        return x**2 + 2*y**2 - z**2 + x*y*z
    return f

def calcular_divergencia_aproximada(f, x, y, z, h=1e-6):
    
    df_dx = (f(x + h, y, z) - f(x - h, y, z)) / (2 * h)
    df_dy = (f(x, y + h, z) - f(x, y - h, z)) / (2 * h)
    df_dz = (f(x, y, z + h) - f(x, y, z - h)) / (2 * h)
    return df_dx + df_dy + df_dz

def plotar_divergencia(f, x_range, y_range, z_range, num_pontos=20):
   
    x = np.linspace(x_range[0], x_range[1], num_pontos)
    y = np.linspace(y_range[0], y_range[1], num_pontos)
    z = np.linspace(z_range[0], z_range[1], num_pontos)
    X, Y, Z = np.meshgrid(x, y, z)

    divergencia = calcular_divergencia_aproximada(f, X, Y, Z)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Use um mapa de cores para representar a intensidade da divergência
    norm = plt.Normalize(divergencia.min(), divergencia.max())
    cmap = plt.cm.viridis
    colors = cmap(norm(divergencia))

    # Plote os pontos com cores representando a divergência
    scatter = ax.scatter(X, Y, Z, c=colors.flatten())

    # Adicione uma barra de cores para interpretar as cores
    cbar = fig.colorbar(scatter)
    cbar.set_label('Divergência (∇f)')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Visualização da Divergência (∇f)')
    plt.show()

if __name__ == "__main__":
    funcao_f = definir_funcao()
    x_limites = (-2, 2)
    y_limites = (-2, 2)
    z_limites = (-2, 2)
    num_amostras = 15  # Ajuste para mais ou menos detalhes

    plotar_divergencia(funcao_f, x_limites, y_limites, z_limites, num_amostras)