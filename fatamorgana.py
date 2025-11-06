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