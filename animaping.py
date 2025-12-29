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

# --- Variáveis da Bola ---
raio_bola = 20
x = LARGURA // 2  # Começa no meio horizontalmente
y = 50            # Começa no topo
velocidade_x = 4  # Velocidade horizontal (para ela ir para o lado)
velocidade_y = 0  # Velocidade vertical inicial

# --- Física ---
gravidade = 0.5       # Força que puxa para baixo
elasticidade = 0.8    # Quanto a bola "perde" de força ao bater (0.8 = 80% de retorno)
atrito = 0.99         # Resistência do ar/chão (para desacelerar horizontalmente)