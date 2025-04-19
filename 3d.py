import pygame
import math

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Quarto 3D Simples")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Definição dos vértices do cubo
vertices_cubo = [
    (-50, -50, -50),
    (50, -50, -50),
    (50, 50, -50),
    (-50, 50, -50),
    (-50, -50, 50),
    (50, -50, 50),
    (50, 50, 50),
    (-50, 50, 50)
]

# Definição das arestas do cubo (conexões entre os vértices)
arestas_cubo = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Face inferior
    (4, 5), (5, 6), (6, 7), (7, 4),  # Face superior
    (0, 4), (1, 5), (2, 6), (3, 7)   # Conexões verticais
]

# Posição inicial do cursor
cursor_x = largura // 2
cursor_y = altura // 2
velocidade_cursor = 5

# Função para projetar um ponto 3D para 2D
def projetar(ponto):
    focal = 300
    z = ponto[2]
    escala = focal / (focal + z)
    x_2d = escala * ponto[0] + largura // 2
    y_2d = escala * ponto[1] + altura // 2
    return (int(x_2d), int(y_2d))

# Loop principal do jogo
rodando = True
while rodando:
    tela.fill(preto)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                cursor_x -= velocidade_cursor
            if evento.key == pygame.K_RIGHT:
                cursor_x += velocidade_cursor
            if evento.key == pygame.K_UP:
                cursor_y -= velocidade_cursor
            if evento.key == pygame.K_DOWN:
                cursor_y += velocidade_cursor

    # Desenhar o cubo
    pontos_projetados = [projetar(v) for v in vertices_cubo]
    for aresta in arestas_cubo:
        ponto1 = pontos_projetados[aresta[0]]
        ponto2 = pontos_projetados[aresta[1]]
        pygame.draw.line(tela, branco, ponto1, ponto2, 2)

    # Desenhar o cursor
    pygame.draw.circle(tela, vermelho, (cursor_x, cursor_y), 5)

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()