import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plot_tetrahedron():
    """
    Cria e plota um tetraedro em 3D.
    """
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Definir os vértices do tetraedro
    # Vamos usar um tetraedro regular simples como exemplo
    vertices = np.array([
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, -1],
        [1, -1, -1]
    ])

    # Definir as faces do tetraedro usando os índices dos vértices
    # Cada tupla representa uma face, conectando 3 vértices
    faces = [
        [vertices[0], vertices[1], vertices[2]],
        [vertices[0], vertices[1], vertices[3]],
        [vertices[0], vertices[2], vertices[3]],
        [vertices[1], vertices[2], vertices[3]]
    ]

    # Adicionar as faces ao plot 3D
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.6))

    # Plotar os vértices (opcional, mas ajuda a visualizar)
    ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], c='blue', s=50)

    # Configurar os limites dos eixos para que o tetraedro seja visível
    max_range = np.array([vertices[:,0].max()-vertices[:,0].min(),
                          vertices[:,1].max()-vertices[:,1].min(),
                          vertices[:,2].max()-vertices[:,2].min()]).max() / 2.0
    mid_x = (vertices[:,0].max()+vertices[:,0].min()) * 0.5
    mid_y = (vertices[:,1].max()+vertices[:,1].min()) * 0.5
    mid_z = (vertices[:,2].max()+vertices[:,2].min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)


    # Adicionar rótulos aos eixos
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')
    ax.set_title('Visualização de um Tetraedro')

    # Mostrar o gráfico
    plt.show()

if __name__ == "__main__":
    plot_tetrahedron()