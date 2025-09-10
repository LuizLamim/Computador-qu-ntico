import pygame
import math

# Inicializando o Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Coração Animado')

# Cores
preto = (0, 0, 0)
vermelho = (255, 0, 0)
rosa = (255, 105, 180) # Cor de coração para o fundo

# Posição e tamanho inicial do coração
centro_x = largura // 2
centro_y = altura // 2
tamanho_base = 150
pulsar_velocidade = 0.5
tamanho_pulsar = 0.0

# Loop principal da animação
rodando = True
clock = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Aumenta ou diminui o tamanho para o efeito de pulsação
    tamanho_pulsar = tamanho_base + 15 * math.sin(pygame.time.get_ticks() * 0.005)
    
    # Limpa a tela
    tela.fill(rosa)

    # Desenha o coração
    pontos_coracao = []
    num_pontos = 100 # Número de pontos para desenhar a curva do coração

    for i in range(num_pontos):
        t = 2 * math.pi * i / num_pontos
        x = centro_x + tamanho_pulsar * 16 * math.sin(t)**3
        y = centro_y - tamanho_pulsar * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        pontos_coracao.append((x, y))

    if len(pontos_coracao) >= 3:
        pygame.draw.polygon(tela, vermelho, pontos_coracao)

    # Atualiza a tela
    pygame.display.flip()
    
    # Controla a taxa de quadros (FPS)
    clock.tick(60)

# Sair do Pygame
pygame.quit()