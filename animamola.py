import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. Configurações Físicas ---
k = 10.0       # Constante elástica da mola (N/m)
m = 1.0        # Massa (kg)
A = 2.0        # Amplitude do movimento (m)
omega = np.sqrt(k / m)  # Frequência angular

# --- 2. Função para desenhar a mola (Visual) ---
def get_spring_coords(start_x, start_y, end_x, end_y, nodes=15, width=0.5):
    """
    Gera as coordenadas x e y para desenhar uma mola em ziguezague.
    """
    # Cria pontos linearmente espaçados entre o início e o fim
    x_data = np.linspace(start_x, end_x, nodes)
    y_data = np.linspace(start_y, end_y, nodes)
    
    # Adiciona o desvio lateral (ziguezague) apenas nos nós internos
    # Usamos uma onda senoidal ou alternância simples para simular as espiras
    offsets = np.zeros(nodes)
    offsets[1:-1] = width * ((np.arange(nodes-2) % 2) * 2 - 1)
    
    # Como a mola é vertical, o offset é aplicado no eixo X
    x_data += offsets
    
    return x_data, y_data