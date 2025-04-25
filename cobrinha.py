import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha (Inspirado)")

# Cores
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

# Configurações do ponto inicial
tamanho_ponto = 20
posicao_x = largura // 2
posicao_y = altura // 2
velocidade = 10

# Configurações da comida (blocos)
tamanho_comida = 20
posicao_comida_x = random.randrange(0, largura - tamanho_comida, 20)
posicao_comida_y = random.randrange(0, altura - tamanho_comida, 20)

# Função para desenhar o ponto
def desenhar_ponto(tamanho, x, y):
    pygame.draw.rect(tela, verde, [x, y, tamanho, tamanho])

# Função para desenhar a comida
def desenhar_comida(tamanho, x, y):
    pygame.draw.rect(tela, vermelho, [x, y, tamanho, tamanho])

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                posicao_x -= velocidade
            if evento.key == pygame.K_RIGHT:
                posicao_x += velocidade
            if evento.key == pygame.K_UP:
                posicao_y -= velocidade
            if evento.key == pygame.K_DOWN:
                posicao_y += velocidade

    # Mantém o ponto dentro da tela
    if posicao_x < 0:
        posicao_x = 0
    elif posicao_x > largura - tamanho_ponto:
        posicao_x = largura - tamanho_ponto
    if posicao_y < 0:
        posicao_y = 0
    elif posicao_y > altura - tamanho_ponto:
        posicao_y = altura - tamanho_ponto

    # Verifica se o ponto comeu a comida
    if posicao_x < posicao_comida_x + tamanho_comida and \
       posicao_x + tamanho_ponto > posicao_comida_x and \
       posicao_y < posicao_comida_y + tamanho_comida and \
       posicao_y + tamanho_ponto > posicao_comida_y:
        tamanho_ponto += 5  # Aumenta o tamanho do ponto
        posicao_comida_x = random.randrange(0, largura - tamanho_comida, 20)
        posicao_comida_y = random.randrange(0, altura - tamanho_comida, 20)

    # Limpa a tela
    tela.fill(branco)

    # Desenha a comida
    desenhar_comida(tamanho_comida, posicao_comida_x, posicao_comida_y)

    # Desenha o ponto
    desenhar_ponto(tamanho_ponto, posicao_x, posicao_y)

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()