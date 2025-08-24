import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configurações da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo 2D Simples")

# Relógio para controlar a taxa de quadros
relogio = pygame.time.Clock()

# Variável da pontuação
pontuacao = 0
# Configuração da fonte para a pontuação
fonte = pygame.font.Font(None, 36)

# --- Classe do Jogador ---
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = LARGURA_TELA // 2 - 25
        self.rect.y = ALTURA_TELA - 60
        self.velocidade_x = 0

    def update(self):
        self.rect.x += self.velocidade_x
        
        # Limita o jogador dentro da tela
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > LARGURA_TELA - self.rect.width:
            self.rect.x = LARGURA_TELA - self.rect.width

# --- Classe do Inimigo ---
class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(LARGURA_TELA - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidade_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.velocidade_y

# --- Grupos de Sprites ---
lista_sprites_ativos = pygame.sprite.Group()
lista_inimigos = pygame.sprite.Group()

# Cria o jogador
jogador = Jogador()
lista_sprites_ativos.add(jogador)

# Cria 20 inimigos
for i in range(20):
    inimigo = Inimigo()
    lista_sprites_ativos.add(inimigo)
    lista_inimigos.add(inimigo)

# --- Loop principal do jogo ---
feito = False
while not feito:
    # --- Gerenciamento de eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            feito = True
        
        # Lida com pressionar de tecla
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jogador.velocidade_x = -5
            elif evento.key == pygame.K_RIGHT:
                jogador.velocidade_x = 5

        # Lida com soltar de tecla
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jogador.velocidade_x = 0

    # --- Lógica do jogo ---
    lista_sprites_ativos.update()

    # Verifica colisões entre o jogador e os inimigos
    colisoes = pygame.sprite.spritecollide(jogador, lista_inimigos, False)
    if colisoes:
        feito = True  # Encerra o jogo se houver colisão

    # Verifica se os inimigos saíram da tela e atualiza a pontuação
    for inimigo in lista_inimigos:
        if inimigo.rect.y > ALTURA_TELA:
            pontuacao += 1
            # Reposiciona o inimigo no topo da tela
            inimigo.rect.x = random.randrange(LARGURA_TELA - inimigo.rect.width)
            inimigo.rect.y = random.randrange(-100, -40)

    # --- Renderização ---
    tela.fill(PRETO)  # Preenche o fundo com preto
    lista_sprites_ativos.draw(tela)  # Desenha todos os sprites

    # Desenha a pontuação na tela
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    tela.blit(texto_pontuacao, (10, 10))

    # Atualiza a tela
    pygame.display.flip()

    # Limita a 60 quadros por segundo
    relogio.tick(60)

# Encerra o Pygame
pygame.quit()