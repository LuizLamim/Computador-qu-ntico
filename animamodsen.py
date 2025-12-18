import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = np.linspace(0, 4 * np.pi, 500)

y_data = np.abs(np.sin(x_data))

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(0, 1.2)  # Um pouco acima de 1 para melhor visualização
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title(r'Animação da Função $y = |\sin(x)|$', fontsize=16)
ax.set_xlabel('x (radianos)')
ax.set_ylabel('y')