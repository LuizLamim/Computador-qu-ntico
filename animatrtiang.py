import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Configuração da Figura
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal') # Garante que o triângulo não fique distorcido
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Animação de Triângulo Girando")

# 2. Definindo os vértices do triângulo (Centrado na origem)
# Pontos: (x, y). O último ponto repete o primeiro para fechar o desenho.
vertices_iniciais = np.array([
    [0, 1],    # Topo
    [-0.866, -0.5], # Canto esquerdo
    [0.866, -0.5],  # Canto direito
    [0, 1]     # Fechando no topo
])

# Cria o objeto de linha que será atualizado na animação
triangulo_line, = ax.plot([], [], 'b-', lw=2, color='purple')

# 3. Função de Rotação (Matemática)
def aplicar_rotacao(vertices, angulo_graus):
    angulo_rad = np.radians(angulo_graus)
    cos_a = np.cos(angulo_rad)
    sin_a = np.sin(angulo_rad)
    
    # Matriz de rotação 2D
    matriz_rotacao = np.array([
        [cos_a, -sin_a],
        [sin_a, cos_a]
    ])
    
    # Aplica a rotação (multiplicação de matrizes)
    # Transpomos (.T) para multiplicar corretamente e transpomos de volta
    return np.dot(vertices, matriz_rotacao.T)

# 4. Função de Inicialização da Animação
def init():
    triangulo_line.set_data([], [])
    return triangulo_line,

# 5. Função de Atualização (Chamada a cada frame)
def update(frame):
    # O 'frame' aqui representa o ângulo atual
    novos_vertices = aplicar_rotacao(vertices_iniciais, frame)
    
    # Separa X e Y para o plot
    x = novos_vertices[:, 0]
    y = novos_vertices[:, 1]
    
    triangulo_line.set_data(x, y)
    return triangulo_line,

# Cria a animação
# frames=np.arange(0, 360, 2) -> Vai de 0 a 360 graus, pulando de 2 em 2
# interval=20 -> 20 milissegundos entre cada frame
anim = FuncAnimation(fig, update, frames=np.arange(0, 360, 2),
                     init_func=init, blit=True, interval=20)