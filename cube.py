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
