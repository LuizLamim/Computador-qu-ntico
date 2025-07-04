import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parâmetros da Simulação ---
# Raio da "esfera" central (pode ser pensado como o raio de Schwarzschild para um buraco negro)
RAIO_ESFERA = 0.5
# Número de linhas a serem visualizadas
NUM_LINHAS = 20
# Limites do plot
LIMITE_X = 2.0
LIMITE_Y = 2.0
# "Força" da distorção (simulando a massa do objeto)
FORCA_DISTORCAO = 0.1

# --- Funções Auxiliares ---

def calcular_distorcao(x, y, raio_esfera, forca_distorcao):
    """
    Calcula o deslocamento de um ponto devido à "distorção".
    Esta é uma função simplificada para visualização 2D.
    """
    distancia = np.sqrt(x**2 + y**2)
    if distancia < raio_esfera:
        # Dentro da esfera, a distorção é diferente ou não calculada neste modelo simples
        return 0, 0
    else:
        # Quanto mais perto da esfera, maior a distorção
        # A distorção é na direção radial
        fator_distorcao = forca_distorcao / distancia**2
        dx = -x * fator_distorcao
        dy = -y * fator_distorcao
        return dx, dy

# --- Configuração da Figura e Eixos ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-LIMITE_X, LIMITE_X)
ax.set_ylim(-LIMITE_Y, LIMITE_Y)
ax.set_aspect('equal', adjustable='box')
ax.set_title('Simulação 2D de Lente Gravitacional')
ax.set_xlabel('Espaço X')
ax.set_ylabel('Espaço Y')
ax.grid(True)

# Desenha a "esfera" central
esfera = plt.Circle((0, 0), RAIO_ESFERA, color='black', alpha=0.7, label='Objeto Massivo')
ax.add_patch(esfera)

# Inicializa as linhas que serão distorcidas
linhas_plotadas = []
# Cria linhas paralelas iniciais
for i in range(NUM_LINHAS):
    y_inicial = (i / (NUM_LINHAS - 1)) * (LIMITE_Y * 2) - LIMITE_Y
    line, = ax.plot([], [], 'b-', lw=1)
    linhas_plotadas.append(line)

# Texto para exibir o tempo/quadro
tempo_texto = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12)

# --- Função de Animação ---
def animar(frame):
    for i, line in enumerate(linhas_plotadas):
        y_inicial = (i / (NUM_LINHAS - 1)) * (LIMITE_Y * 2) - LIMITE_Y

        # Pontos da linha original (reta)
        x_pontos_originais = np.linspace(-LIMITE_X, LIMITE_X, 100)
        y_pontos_originais = np.full_like(x_pontos_originais, y_inicial)

        # Aplica a distorção (esta parte é mais complexa em um modelo real)
        # Aqui, estamos simulando a distorção de forma "estática"
        # Para uma animação da distorção *mudando*, precisaríamos de um parâmetro de tempo na função de distorção.
        x_distorcido = []
        y_distorcido = []
        for x, y in zip(x_pontos_originais, y_pontos_originais):
            # A distorção é aplicada aqui. Podemos simular uma variação com o tempo
            # se quiséssemos mostrar a distorção "aparecendo" ou "desaparecendo".
            # Neste exemplo, a distorção é constante no espaço, mas podemos visualizá-la
            # como um "instantâneo" de como a luz se curvaria.
            dx, dy = calcular_distorcao(x, y, RAIO_ESFERA, FORCA_DISTORCAO * np.sin(frame * 0.05 + 1.5) + FORCA_DISTORCAO) # Simula uma oscilação na força
            x_distorcido.append(x + dx)
            y_distorcido.append(y + dy)

        line.set_data(x_distorcido, y_distorcido)

    tempo_texto.set_text(f'Quadro: {frame}')
    return linhas_plotadas + [tempo_texto]

# --- Criação da Animação ---
ani = FuncAnimation(fig, animar, frames=100, interval=50, blit=True)

plt.legend()
plt.show()

# Se quiser salvar a animação (requer 'ffmpeg' ou 'imagemagick')
# ani.save('distorcao_espaco_tempo_2d.gif', writer='pillow', fps=20)