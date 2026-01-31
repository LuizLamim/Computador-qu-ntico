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

# 2. Configuração da Grade
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_title("Animação de Campo Magnético (Ímã em Rotação)")

# Inicializa o gráfico de vetores (Quiver)
Q = ax.quiver(X, Y, np.zeros_like(X), np.zeros_like(Y), color='royalblue', pivot='mid')