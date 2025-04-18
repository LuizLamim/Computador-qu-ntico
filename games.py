import pygame

# Inicializa o Pygame
pygame.init()

# Define as cores
branco = (255, 255, 255)
azul = (0, 0, 255)

# Define as dimensões da janela
largura = 800
altura = 600

# Cria a janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Quarto Simples")

# Loop principal
rodando = True
while rodando:
    # Trata os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Desenha o fundo (paredes azuis)
    tela.fill(azul)

    # Desenha o chão (retângulo branco na parte inferior)
    pygame.draw.rect(tela, branco, (0, altura * 2 // 3, largura, altura // 3))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()