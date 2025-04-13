import pygame

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))

# Define o título da janela
pygame.display.set_caption("Cursor com Setas do Teclado")

# Define a cor de fundo
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Define a posição inicial do cursor
cursor_x = largura // 2
cursor_y = altura // 2
tamanho_cursor = 20

# Loop principal do jogo
rodando = True
while rodando:
    # Trata os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                cursor_x -= 10
            elif evento.key == pygame.K_RIGHT:
                cursor_x += 10
            elif evento.key == pygame.K_UP:
                cursor_y -= 10
            elif evento.key == pygame.K_DOWN:
                cursor_y += 10

    # Mantém o cursor dentro da tela
    if cursor_x < 0:
        cursor_x = 0
    elif cursor_x > largura - tamanho_cursor:
        cursor_x = largura - tamanho_cursor
    if cursor_y < 0:
        cursor_y = 0
    elif cursor_y > altura - tamanho_cursor:
        cursor_y = altura - tamanho_cursor

    # Limpa a tela
    tela.fill(branco)

    # Desenha o cursor
    pygame.draw.rect(tela, vermelho, (cursor_x, cursor_y, tamanho_cursor, tamanho_cursor))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()