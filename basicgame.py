import pygame # Importa a biblioteca Pygame

# --- 1. Inicialização do Pygame ---
pygame.init() # Sempre a primeira coisa a fazer ao usar Pygame

# --- 2. Configurações da Janela ---
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO_JANELA = "Pygame Básico - Funções Essenciais"

# Cria a superfície da tela (a janela do jogo)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(TITULO_JANELA)

# --- 3. Cores (em formato RGB) ---
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# --- 4. Loop Principal do Jogo ---
rodando = True
while rodando:
    # --- 5. Lidar com Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Verifica se o usuário clicou no 'X' para fechar
            rodando = False

    # --- 6. Lógica do Jogo (Opcional, para um jogo real) ---
    # Aqui você colocaria o código que atualiza o estado do seu jogo:
    # - Movimento de personagens
    # - Detecção de colisões
    # - Contagem de pontos, etc.

    # --- 7. Desenhar na Tela ---
    # Limpa a tela com uma cor de fundo (preenche toda a superfície)
    tela.fill(AZUL) # Fundo azul

    # Desenha um retângulo vermelho
    # pygame.draw.rect(superficie, cor, [x, y, largura, altura], espessura_borda)
    # Se espessura_borda for 0, o retângulo é preenchido.
    pygame.draw.rect(tela, VERMELHO, [50, 50, 150, 100], 0)

    # Desenha um círculo verde
    # pygame.draw.circle(superficie, cor, (centro_x, centro_y), raio, espessura_borda)
    pygame.draw.circle(tela, VERDE, (400, 300), 70, 5) # Círculo com borda de 5px

    # Desenha uma linha amarela
    # pygame.draw.line(superficie, cor, (x1, y1), (x2, y2), espessura)
    pygame.draw.line(tela, AMARELO, (100, 500), (700, 500), 8)

    # Desenha texto na tela
    # Primeiro, escolha uma fonte e tamanho
    fonte = pygame.font.Font(None, 48) # None usa a fonte padrão, 48 é o tamanho
    texto = fonte.render("Olá, Pygame!", True, BRANCO) # (texto, suavizar_borda, cor_texto)
    # Obtenha o retângulo que envolve o texto para posicionamento
    texto_ret = texto.get_rect()
    texto_ret.center = (LARGURA_TELA // 2, 50) # Centraliza o texto no topo da tela
    tela.blit(texto, texto_ret) # Desenha o texto na tela

    # --- 8. Atualizar a Tela ---
    # Tudo o que foi desenhado até agora está no "buffer" da tela.
    # pygame.display.flip() ou pygame.display.update() tornam isso visível.
    pygame.display.flip() # Ou pygame.display.update()

# --- 9. Finalização do Pygame ---
pygame.quit() # Desinicializa todos os módulos Pygame e encerra o programa