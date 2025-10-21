import pygame
import sys

# 1. Inicialização do Pygame
pygame.init()

# 2. Definição das dimensões e cor
LARGURA = 1920
ALTURA = 1080
DIMENSOES = (LARGURA, ALTURA)

# Definição da cor Roxo (Purple) em RGB
# Um roxo comum é (128, 0, 128). Você pode ajustá-lo!
ROXO = (128, 0, 128) 

# 3. Configuração da Janela (Tela)
# Cria a superfície de exibição (a janela)
tela = pygame.display.set_mode(DIMENSOES)
# Define o título da janela
pygame.display.set_caption("Tela Roxo 1920x1080")

executando = True
while executando:
    # 5. Tratamento de Eventos
    for evento in pygame.event.get():
        # Verifica se o usuário clicou no botão de fechar (X)
        if evento.type == pygame.QUIT:
            executando = False
        
        # Verifica se o usuário pressionou a tecla ESC para fechar
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False
tela.fill(ROXO)

    pygame.display.flip()

# 8. Finalização do Pygame
pygame.quit()
sys.exit()