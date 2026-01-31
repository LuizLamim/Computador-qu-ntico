import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Configurações do campo
def magnetic_field(x, y, x0, y0, m_dir):
    """
    Calcula o campo magnético de um dipolo magnético (ímã ideal).
    m_dir: vetor momento magnético (direção do ímã)
    """
    mu_0 = 4 * np.pi * 1e-7
    m = 1.0  # Intensidade do momento magnético
    
    # Vetores de posição em relação ao centro do ímã
    dx, dy = x - x0, y - y0
    r = np.sqrt(dx**2 + dy**2) + 1e-9  # evita divisão por zero
    
    # Equação do Campo do Dipolo: B(r) = (mu_0 / 4pi) * [3r(m.r)/r^5 - m/r^3]
    # Aqui simplificamos a constante para fins de visualização
    dot_product = dx * m_dir[0] + dy * m_dir[1]
    
    Bx = (3 * dx * dot_product / r**5 - m_dir[0] / r**3)
    By = (3 * dy * dot_product / r**5 - m_dir[1] / r**3)
    
    return Bx, By