import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Configuração da Figura
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal') # Garante que o triângulo não fique distorcido
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Animação de Triângulo Girando")

# 2. Definindo os vértices do triângulo (Centrado na origem)
# Pontos: (x, y). O último ponto repete o primeiro para fechar o desenho.
vertices_iniciais = np.array([
    [0, 1],    # Topo
    [-0.866, -0.5], # Canto esquerdo
    [0.866, -0.5],  # Canto direito
    [0, 1]     # Fechando no topo
])