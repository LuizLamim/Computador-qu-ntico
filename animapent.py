import pygame
import math

pygame.init()

LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pentágono Giratório - Pygame")

PRETO = (0, 0, 0)
NEON_CYAN = (0, 255, 255)

centro_x, centro_y = LARGURA // 2, ALTURA // 2
raio = 150
angulo_rotacao = 0
velocidade = 0.02  

clock = pygame.time.Clock()

executando = True
while executando:
    # 1. Checar eventos (fechar janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # 2. Atualizar lógica (Aumentar o ângulo para girar)
    angulo_rotacao += velocidade

    # 3. Calcular os 5 vértices do pentágono
    # Um pentágono tem 5 lados, então dividimos o círculo (2*PI) por 5.
    pontos = []
    for i in range(5):
        # Fórmula matemática para posição circular:
        # x = r * cos(theta) + centro_x
        # y = r * sin(theta) + centro_y
        
        # O ângulo de cada vértice é a base (i * 2pi/5) + a rotação atual
        theta = i * (2 * math.pi / 5) + angulo_rotacao
        
        x = centro_x + raio * math.cos(theta)
        y = centro_y + raio * math.sin(theta)
        pontos.append((x, y))

        
    tela.fill(PRETO) 
    
    pygame.draw.polygon(tela, NEON_CYAN, pontos, 3)

    pygame.display.flip() 
    clock.tick(60) 

pygame.quit()