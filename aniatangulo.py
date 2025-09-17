import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define as cores
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Configurações da janela
LARGURA_JANELA = 800
ALTURA_JANELA = 600

tamanho_janela = (LARGURA_JANELA, ALTURA_JANELA)
tela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("Retângulo Vermelho Giratório")

# Posição e tamanho do retângulo
largura_retangulo = 200
altura_retangulo = 100
posicao_x = (LARGURA_JANELA - largura_retangulo) // 2
posicao_y = (ALTURA_JANELA - altura_retangulo) // 2
retangulo_original = pygame.Rect(0, 0, largura_retangulo, altura_retangulo)
