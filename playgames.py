import pygame
import time
import random

# Inicializa o pygame
pygame.init()

# Cores (RGB)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 102)
PRETO = (0, 0, 0)
VERMELHO = (213, 50, 80)
VERDE = (0, 255, 0)
AZUL = (50, 153, 213)

# Dimensões da tela
LARGURA_TELA = 600
ALTURA_TELA = 400

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Jogo da Cobrinha - Python')

clock = pygame.time.Clock()

# Configurações da Cobra
TAMANHO_BLOCO = 10
VELOCIDADE_COBRA = 11

# Fontes
fonte_estilo = pygame.font.SysFont("bahnschrift", 25)
fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)

def placar(pontos):
    valor = fonte_pontuacao.render("Pontuação: " + str(pontos), True, AMARELO)
    tela.blit(valor, [0, 0])

def nossa_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, VERDE, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def mensagem(msg, cor):
    msg_renderizada = fonte_estilo.render(msg, True, cor)
    # Centraliza a mensagem
    tela.blit(msg_renderizada, [LARGURA_TELA / 6, ALTURA_TELA / 3])

def jogo_loop():
    fim_de_jogo = False
    game_over = False

    # Posição inicial
    x1 = LARGURA_TELA / 2
    y1 = ALTURA_TELA / 2

    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    # Posição da comida
    comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / 10.0) * 10.0
    comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / 10.0) * 10.0

    while not fim_de_jogo:

        while game_over == True:
            tela.fill(PRETO)
            mensagem("Fim de Jogo! C-Continuar ou Q-Sair", VERMELHO)
            placar(comprimento_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fim_de_jogo = True
                        game_over = False
                    if event.key == pygame.K_c:
                        jogo_loop()

        # Captura de Teclas
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudanca = -TAMANHO_BLOCO
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x1_mudanca = TAMANHO_BLOCO
                    y1_mudanca = 0
                elif event.key == pygame.K_UP:
                    y1_mudanca = -TAMANHO_BLOCO
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y1_mudanca = TAMANHO_BLOCO
                    x1_mudanca = 0

        # Checagem de colisão com as paredes
        if x1 >= LARGURA_TELA or x1 < 0 or y1 >= ALTURA_TELA or y1 < 0:
            game_over = True
        
        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(PRETO)
        
        # Desenhar comida
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])
        
        # Lógica de crescimento da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)
        
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Checagem de colisão com o próprio corpo
        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                game_over = True

        nossa_cobra(TAMANHO_BLOCO, lista_cobra)
        placar(comprimento_cobra - 1)

        pygame.display.update()

        # Comer a comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / 10.0) * 10.0
            comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(VELOCIDADE_COBRA)

    pygame.quit()
    quit()

# Iniciar o jogo
jogo_loop()