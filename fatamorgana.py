import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# --- 1. Configurações Físicas/Geométricas ---

# Altura máxima da simulação (em metros, aprox.)
ALTURA_MAX = 100
# Número de segmentos para modelar a curva do raio de luz
NUM_SEGMENTOS = 50
# Posição do objeto distante (a fonte da luz)
X_OBJETO = 1000  # Distância (metros)
Y_OBJETO = 50    # Altura (metros)

# --- 2. Simulação da Curvatura da Luz (Refração) ---

def indice_refracao(y):
    """
    Simula o índice de refração (n) em função da altura (y).
    
    No caso da Fata Morgana (miragem superior):
    - Camada de ar frio (inferior): n é mais alto.
    - Camada de ar quente (superior): n é mais baixo.
    
    Abaixo, simulamos uma inversão térmica: n decresce rapidamente no topo,
    depois se estabiliza.
    """
    # Valor base do índice de refração
    n_base = 1.00029
    # Um termo que simula a inversão térmica (n alto em y baixo)
    n_variacao = 0.00005 * np.exp(-y / 20)
    return n_base + n_variacao

def calcular_trajetoria_curva(x_obj, y_obj, num_seg):
    """
    Calcula uma trajetória curva (simplificada) devido à refração.
    A luz se curva em direção ao índice de refração mais alto (o ar frio).
    """
    x_coords = np.linspace(0, x_obj, num_seg)
    y_coords = np.zeros(num_seg)
    
    # Altura inicial (onde a luz "deixa" o objeto)
    y_coords[-1] = y_obj

    # Curvatura simulada: A luz se curva para baixo (em direção ao chão)
    # A curvatura é mais acentuada quando a variação de n é maior (próximo ao chão)
    for i in range(num_seg - 2, -1, -1):
        # Gradiente simplificado de curvatura baseado na altura
        curvatura = (indice_refracao(y_coords[i+1]) - indice_refracao(y_coords[i+1] - 1)) * 500000
        
        # O próximo ponto é ligeiramente mais baixo (curvando para baixo)
        y_coords[i] = y_coords[i+1] - (x_obj / num_seg) * curvatura
        
        # Garante que o raio não vá abaixo do "solo"
        if y_coords[i] < 0:
            y_coords[i] = 0
            break
            
    # O observador está na posição (0, y_coords[0]) e vê a imagem aparente
    return x_coords, y_coords

# --- 3. Configuração da Animação Matplotlib ---

# Inicializa a figura e o eixo
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, X_OBJETO + 100)
ax.set_ylim(-5, ALTURA_MAX)
ax.set_xlabel("Distância (m)")
ax.set_ylabel("Altura (m)")
ax.set_title("Simulação Geométrica de Fata Morgana (Refração)")
ax.grid(True)

# Desenha o solo
ax.hlines(0, 0, X_OBJETO + 100, color='gray', linestyle='-', linewidth=4, label='Solo (Ar Frio)')

# Desenha o objeto real (um ponto na distância)
obj_real, = ax.plot(X_OBJETO, Y_OBJETO, 'o', color='red', markersize=8, label='Objeto Real')

# Desenha a trajetória da luz (inicialmente vazia)
trajetoria, = ax.plot([], [], '-', color='orange', linewidth=2, label='Trajetória Curva da Luz')

# Desenha a linha de visão aparente (como o observador "pensa" que a luz viajou)
linha_aparente, = ax.plot([], [], '--', color='blue', linewidth=1, label='Linha de Visão Aparente')

# Posição do observador (próximo à origem, a uma altura baixa)
OBS_X = 0
OBS_Y = 5
observador, = ax.plot(OBS_X, OBS_Y, 's', color='black', markersize=8, label='Observador')

# Desenha a imagem aparente (onde o objeto *parece* estar)
img_aparente, = ax.plot([], [], 'x', color='blue', markersize=10, label='Imagem Aparente (Miragem)')

# Adiciona uma legenda para a estratificação (inversão térmica)
ax.text(X_OBJETO / 2, ALTURA_MAX * 0.9, 'Camada de Ar Quente (n Baixo)', color='red', ha='center')
ax.text(X_OBJETO / 2, ALTURA_MAX * 0.1, 'Camada de Ar Frio (n Alto)', color='blue', ha='center')