import pygame
import sys
import math

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Quadrado Rotacionando")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Posição e tamanho do quadrado
pos_x, pos_y = largura // 2, altura // 2
tamanho_lado = 100

# Variáveis para a rotação
angulo = 0
velocidade_rotacao = 2  # em graus por frame

# Loop principal da animação
rodando = True
while rodando:
    # Lida com eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Limpa a tela
    tela.fill(preto)

    # Calcula os vértices do quadrado rotacionado
    vertices = []
    for i in range(4):
        # Aumenta o ângulo em 90 graus para cada vértice
        angulo_vertice = angulo + i * 90
        
        # Converte o ângulo para radianos para usar com as funções trigonométricas
        radianos = math.radians(angulo_vertice)
        
        # Calcula as coordenadas X e Y do vértice em relação ao centro
        x_rotacionado = pos_x + tamanho_lado / 2 * math.cos(radianos)
        y_rotacionado = pos_y + tamanho_lado / 2 * math.sin(radianos)
        
        vertices.append((x_rotacionado, y_rotacionado))

    # Desenha o quadrado conectando os vértices
    pygame.draw.polygon(tela, branco, vertices, 3) # O 3 cria uma linha com espessura

    # Atualiza o ângulo para a próxima rotação
    angulo += velocidade_rotacao

    # Atualiza a tela para exibir as mudanças
    pygame.display.flip()

    # Controla a taxa de quadros (framerate)
    pygame.time.Clock().tick(60)

# Finaliza o Pygame
pygame.quit()
sys.exit()