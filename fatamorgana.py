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