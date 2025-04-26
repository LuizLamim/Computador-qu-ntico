import numpy as np
import matplotlib.pyplot as plt

# Cria os pontos para o círculo unitário
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

# Cria a figura e os eixos
fig, ax = plt.subplots(figsize=(6, 6))

# Plota o círculo
ax.plot(x, y, label='Círculo Trigonométrico')

# Plota os eixos x e y
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Define os limites dos eixos para que o círculo não fique deformado
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])

# Define os ticks dos eixos
ax.set_xticks(np.arange(-1, 1.1, 0.5))
ax.set_yticks(np.arange(-1, 1.1, 0.5))

# Adiciona legendas e título
ax.set_xlabel('Eixo x (Cosseno)')
ax.set_ylabel('Eixo y (Seno)')
ax.set_title('Círculo Trigonométrico')
ax.legend()
ax.set_aspect('equal') # Garante que o círculo seja desenhado como um círculo

# Adiciona ângulos e linhas radiais (opcional)
for angle in np.arange(0, 360, 30):
    rad = np.deg2rad(angle)
    cos_val = np.cos(rad)
    sin_val = np.sin(rad)
    ax.plot([0, cos_val], [0, sin_val], color='gray', linestyle='--', linewidth=0.5)
    if angle % 90 == 0:
        ax.text(1.1*cos_val, 1.1*sin_val, f'{angle}°', ha='center', va='center')
    else:
        ax.text(1.2*cos_val, 1.2*sin_val, f'{angle}°', ha='center', va='center', fontsize=8)

# Exibe o gráfico
plt.grid(True)
plt.show()