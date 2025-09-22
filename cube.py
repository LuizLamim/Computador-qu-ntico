import pygame
import math

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cubo 3D Girando")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Posições dos vértices do cubo 3D (X, Y, Z)
# Os valores são relativos ao centro (0,0,0) do cubo
# e serão projetados para a tela 2D
points = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
]

# A escala do cubo na tela
scale = 100

# Posição do centro do cubo na tela
center_pos = [WIDTH // 2, HEIGHT // 2]

# Ângulos de rotação iniciais
angle_x = angle_y = angle_z = 0

# Função para conectar os vértices do cubo
def connect_points(i, j, points_projected):
    pygame.draw.line(screen, WHITE, points_projected[i], points_projected[j], 1)

# Loop principal
running = True
while running:
    # Lida com eventos de saída
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpa a tela
    screen.fill(BLACK)

    # Aumenta os ângulos de rotação para cada quadro
    angle_x += 0.01
    angle_y += 0.01
    angle_z += 0.01

    # Lista para armazenar as coordenadas 2D projetadas
    projected_points = [None] * len(points)

    # Transforma os pontos 3D para 2D
    for i, point in enumerate(points):
        x, y, z = point[0], point[1], point[2]

        # Matrizes de rotação (conceito de álgebra linear)
        # Rotação em torno do eixo X
        rotated_x = x
        rotated_y = y * math.cos(angle_x) - z * math.sin(angle_x)
        rotated_z = y * math.sin(angle_x) + z * math.cos(angle_x)

        # Rotação em torno do eixo Y
        x, y, z = rotated_x, rotated_y, rotated_z
        rotated_x = z * math.sin(angle_y) + x * math.cos(angle_y)
        rotated_y = y
        rotated_z = z * math.cos(angle_y) - x * math.sin(angle_y)

        # Rotação em torno do eixo Z
        x, y, z = rotated_x, rotated_y, rotated_z
        rotated_x = x * math.cos(angle_z) - y * math.sin(angle_z)
        rotated_y = x * math.sin(angle_z) + y * math.cos(angle_z)
        rotated_z = z

        # Projeção em 2D
        projected_x = int(rotated_x * scale) + center_pos[0]
        projected_y = int(rotated_y * scale) + center_pos[1]

        projected_points[i] = [projected_x, projected_y]

    # Conecta os pontos para desenhar o cubo
    # Define as arestas do cubo (índices dos vértices que se conectam)
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Arestas frontais
        (4, 5), (5, 6), (6, 7), (7, 4),  # Arestas traseiras
        (0, 4), (1, 5), (2, 6), (3, 7)   # Arestas de conexão
    ]