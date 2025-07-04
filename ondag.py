import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parâmetros da Simulação ---
# Tamanho da grade (número de pontos em cada dimensão)
GRID_SIZE = 30
# Amplitude da onda (quão forte é o efeito de esticar/comprimir)
AMPLITUDE = 0.2
# Frequência da onda (quão rápido ela oscila)
FREQUENCIA = 0.1
# Velocidade de propagação da onda (velocidade da luz simulada)
VELOCIDADE_ONDA = 0.5
# Limites do plot
LIMITE_X = 5.0
LIMITE_Y = 5.0

# --- Configuração da Figura e Eixos ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-LIMITE_X, LIMITE_X)
ax.set_ylim(-LIMITE_Y, LIMITE_Y)
ax.set_aspect('equal', adjustable='box')
ax.set_title('Simulação 2D de Ondas Gravitacionais')
ax.set_xlabel('Espaço X')
ax.set_ylabel('Espaço Y')
ax.grid(True)

# Cria a grade inicial de pontos
x_inicial = np.linspace(-LIMITE_X, LIMITE_X, GRID_SIZE)
y_inicial = np.linspace(-LIMITE_Y, LIMITE_Y, GRID_SIZE)
X_inicial, Y_inicial = np.meshgrid(x_inicial, y_inicial)

# Plota os pontos iniciais (serão atualizados na animação)
# Usamos 'o-' para conectar os pontos e mostrar a distorção da "grade"
linhas_horizontais = []
linhas_verticais = []

for i in range(GRID_SIZE):
    # Linhas horizontais
    line_h, = ax.plot([], [], 'b-', lw=0.8, alpha=0.7)
    linhas_horizontais.append(line_h)
    # Linhas verticais
    line_v, = ax.plot([], [], 'r-', lw=0.8, alpha=0.7)
    linhas_verticais.append(line_v)

# Texto para exibir o tempo/quadro
tempo_texto = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12)

# --- Função de Animação ---
def animar(frame):
    global X_inicial, Y_inicial

    # Calcula o "tempo" da onda
    tempo_onda = frame * 0.1 # O fator 0.1 controla a velocidade da animação

    # Posições distorcidas dos pontos
    X_distorcido = np.copy(X_inicial)
    Y_distorcido = np.copy(Y_inicial)

    # A função h(t, x) representa a amplitude da onda gravitacional
    # Para uma onda que se propaga na direção X, o efeito é principalmente em Y
    # e Z (que seria a terceira dimensão). Em 2D, vamos ver um efeito em Y.
    # A onda gravitacional tipicamente tem dois modos de polarização,
    # um que estica e comprime em X e Y alternadamente (polarização '+')
    # e outro que estica e comprime a 45 graus (polarização 'x').
    # Vamos simular um modo simples de polarização '+' (estica em X, comprime em Y, ou vice-versa)

    # Onda propagando-se ao longo do eixo X
    # O termo np.cos(k*x - omega*t) simula a propagação da onda
    # k = 2 * pi * FREQUENCIA / VELOCIDADE_ONDA (número de onda)
    # omega = 2 * pi * FREQUENCIA (frequência angular)
    # Simplificamos para (X_inicial - VELOCIDADE_ONDA * tempo_onda) para propagação
    
    # Efeito de distorção (simulando a polarização '+')
    # X_distorcido += X_inicial * AMPLITUDE * np.sin(FREQUENCIA * (X_inicial - VELOCIDADE_ONDA * tempo_onda))
    Y_distorcido += Y_inicial * AMPLITUDE * np.cos(FREQUENCIA * (X_inicial - VELOCIDADE_ONDA * tempo_onda))

    # Para um efeito mais visual de "estica e encolhe"
    # A distorção acontece perpendicularmente à direção de propagação da onda.
    # Se a onda se propaga em X, o esticamento/encolhimento é em Y.
    # Vamos adicionar um pequeno esticamento/encolhimento em X também para um efeito 2D
    # Embora não seja rigorosamente correto para uma única polarização '+',
    # ajuda na visualização do conceito de distorção do espaço.
    X_distorcido += X_inicial * AMPLITUDE * np.sin(FREQUENCIA * (X_inicial - VELOCIDADE_ONDA * tempo_onda))


    # Atualiza as linhas horizontais
    for i in range(GRID_SIZE):
        linhas_horizontais[i].set_data(X_distorcido[i, :], Y_distorcido[i, :])

    # Atualiza as linhas verticais
    for j in range(GRID_SIZE):
        linhas_verticais[j].set_data(X_distorcido[:, j], Y_distorcido[:, j])

    tempo_texto.set_text(f'Quadro: {frame}')

    return linhas_horizontais + linhas_verticais + [tempo_texto]

# --- Criação da Animação ---
ani = FuncAnimation(fig, animar, frames=150, interval=50, blit=True)

plt.show()

# Se quiser salvar a animação (requer 'ffmpeg' ou 'imagemagick')
# ani.save('ondas_gravitacionais_2d.gif', writer='pillow', fps=20)