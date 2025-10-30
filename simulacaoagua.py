import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Parâmetros da Simulação ---
NUM_PARTICULAS = 50
GRAVIDADE = np.array([0, -0.05])  # Força da gravidade (em y negativo)
FATOR_AMORTECIMENTO = 0.95        # Fator de perda de velocidade (viscosidade/ar)
FATOR_COLISAO_PAREDE = 0.8        # Fator de 'salto' ao colidir com a parede
TEMPO_PASSO = 0.1                 # Delta de tempo para a integração
LIMITE_X = (0, 10)                # Limites da área de simulação (x)
LIMITE_Y = (0, 10)                # Limites da área de simulação (y)
TAMANHO_PARTICULA = 0.1           # Tamanho (raio) da partícula para colisões

# --- Inicialização ---

# Posições iniciais aleatórias (x, y)
posicoes = np.random.uniform(LIMITE_X[0] + TAMANHO_PARTICULA,
                            LIMITE_X[1] - TAMANHO_PARTICULA,
                            (NUM_PARTICULAS, 2))

# Velocidades iniciais (vx, vy) - aleatórias e pequenas
velocidades = np.random.uniform(-0.1, 0.1, (NUM_PARTICULAS, 2))

# --- Funções de Simulação ---

def atualizar_particulas(posicoes, velocidades, dt):
    """Atualiza a posição e velocidade das partículas aplicando gravidade e limites."""

    # 1. Aplicar a Gravidade (Integração de Euler)
    # V_novo = V_atual + Gravidade * dt
    velocidades[:] += GRAVIDADE * dt

    # 2. Atualizar Posição
    # P_novo = P_atual + V_novo * dt
    posicoes[:] += velocidades * dt

    # 3. Tratar Colisões com as Paredes
    
    # Colisão com o limite X inferior (x < LIMITE_X[0])
    idx_colisao_x_min = posicoes[:, 0] < LIMITE_X[0] + TAMANHO_PARTICULA
    velocidades[idx_colisao_x_min, 0] *= -FATOR_COLISAO_PAREDE # Inverte vx e amortece
    posicoes[idx_colisao_x_min, 0] = LIMITE_X[0] + TAMANHO_PARTICULA # Reposiciona

    # Colisão com o limite X superior (x > LIMITE_X[1])
    idx_colisao_x_max = posicoes[:, 0] > LIMITE_X[1] - TAMANHO_PARTICULA
    velocidades[idx_colisao_x_max, 0] *= -FATOR_COLISAO_PAREDE # Inverte vx e amortece
    posicoes[idx_colisao_x_max, 0] = LIMITE_X[1] - TAMANHO_PARTICULA # Reposiciona

    # Colisão com o limite Y inferior (y < LIMITE_Y[0] - "chão")
    idx_colisao_y_min = posicoes[:, 1] < LIMITE_Y[0] + TAMANHO_PARTICULA
    velocidades[idx_colisao_y_min, 1] *= -FATOR_COLISAO_PAREDE # Inverte vy e amortece
    posicoes[idx_colisao_y_min, 1] = LIMITE_Y[0] + TAMANHO_PARTICULA # Reposiciona
    
    # Colisão com o limite Y superior (y > LIMITE_Y[1])
    idx_colisao_y_max = posicoes[:, 1] > LIMITE_Y[1] - TAMANHO_PARTICULA
    velocidades[idx_colisao_y_max, 1] *= -FATOR_COLISAO_PAREDE # Inverte vy e amortece
    posicoes[idx_colisao_y_max, 1] = LIMITE_Y[1] - TAMANHO_PARTICULA # Reposiciona

    # 4. Aplicar Amortecimento (para simular perda de energia/viscosidade)
    velocidades[:] *= FATOR_AMORTECIMENTO

# --- Configuração da Animação ---

fig, ax = plt.subplots(figsize=(6, 6))

# Configurações do gráfico
ax.set_xlim(LIMITE_X)
ax.set_ylim(LIMITE_Y)
ax.set_aspect('equal', adjustable='box')
ax.set_title("Simulação Básica de Partículas - Água")
ax.set_xlabel("Posição X")
ax.set_ylabel("Posição Y")

# Criação inicial dos pontos (sc é o "scatter" do Matplotlib)
sc = ax.scatter(posicoes[:, 0], posicoes[:, 1], s=10, color='blue', alpha=0.7)

# Função chamada a cada quadro (frame) da animação
def animate(frame):
    """Função de atualização para a animação."""
    
    # Roda a lógica da física
    atualizar_particulas(posicoes, velocidades, TEMPO_PASSO)
    
    # Atualiza os dados do scatter plot com as novas posições
    sc.set_offsets(posicoes)
    
    return sc, # Retorna a lista de objetos gráficos modificados

# Cria a animação
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True, repeat=True)

# Exibe a animação
plt.show()

# Se você quiser salvar a animação como GIF ou vídeo (pode demorar):
# ani.save('simulacao_agua.gif', writer='imagemagick', fps=20)