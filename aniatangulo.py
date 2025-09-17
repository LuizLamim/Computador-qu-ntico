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

# Variáveis para a animação
angulo_atual = 0
velocidade_rotacao = 1

# Clock para controlar a taxa de quadros (FPS)
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    # --- Gerenciamento de eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # --- Lógica da animação ---
    # Aumenta o ângulo para girar o retângulo
    angulo_atual += velocidade_rotacao

    # Cria uma superfície temporária para o retângulo
    retangulo_superficie = pygame.Surface(retangulo_original.size, pygame.SRCALPHA)
    pygame.draw.rect(retangulo_superficie, VERMELHO, retangulo_original)

    # Rotaciona a superfície
    retangulo_rotacionado = pygame.transform.rotate(retangulo_superficie, -angulo_atual)
    
    # Obtém a nova posição do retângulo rotacionado para centralizá-lo
    novo_retangulo_posicao = retangulo_rotacionado.get_rect(center=(posicao_x + largura_retangulo // 2, posicao_y + altura_retangulo // 2))

    # --- Desenho na tela ---
    tela.fill(PRETO)  # Preenche a tela com preto
    tela.blit(retangulo_rotacionado, novo_retangulo_posicao) # Desenha o retângulo rotacionado
    
    # --- Atualiza a tela ---
    pygame.display.flip()

    # --- Controla o FPS ---
    clock.tick(60) # Define 60 quadros por segundo

# --- Finaliza o Pygame ---
pygame.quit()
sys.exit()