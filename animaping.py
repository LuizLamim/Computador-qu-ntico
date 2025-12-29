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

relogio = pygame.time.Clock()

# --- Loop Principal ---
rodando = True
while rodando:
    # 1. Checar eventos (fechar janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 2. Atualizar Física
    velocidade_y += gravidade # A gravidade aumenta a velocidade de queda
    
    y += velocidade_y
    x += velocidade_x

    # Colisão com o chão (Fundo)
    if y + raio_bola >= ALTURA:
        y = ALTURA - raio_bola     # Corrige a posição para não entrar no chão
        velocidade_y *= -elasticidade # Inverte a direção e aplica perda de energia
        velocidade_x *= atrito     # Aplica atrito no chão

        # Se a velocidade for muito baixa, para de quicar para evitar "vibração"
        if abs(velocidade_y) < 2:
            velocidade_y = 0

    # Colisão com as paredes laterais
    if x + raio_bola >= LARGURA or x - raio_bola <= 0:
        velocidade_x *= -1 # Inverte a direção horizontal

    # 3. Desenhar na tela
    tela.fill(PRETO) # Limpa a tela
    
    # Desenha a bola
    pygame.draw.circle(tela, VERMELHO, (int(x), int(y)), raio_bola)

    # Atualiza o display
    pygame.display.flip()

    # Controla os FPS (60 quadros por segundo)
    relogio.tick(60)

pygame.quit()
sys.exit()