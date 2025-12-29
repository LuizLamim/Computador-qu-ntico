import pygame
import sys

pygame.init()

# Cores (R, G, B)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 50, 50)

LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simulação de Bola Quicando")