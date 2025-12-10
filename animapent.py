import pygame
import math

pygame.init()

LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pentágono Giratório - Pygame")

PRETO = (0, 0, 0)
NEON_CYAN = (0, 255, 255)

centro_x, centro_y = LARGURA // 2, ALTURA // 2
raio = 150
angulo_rotacao = 0
velocidade = 0.02  

clock = pygame.time.Clock()