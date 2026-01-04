import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4 * np.pi, 4 * np.pi, 1000)

y = np.sin(x) + 10 * np.cos(x)

plt.figure(figsize=(10, 6)) # Define o tamanho da figura
plt.plot(x, y, label=r'$\sin(x) + 10\cos(x)$', color='blue')

plt.title('Gráfico da Função: sen(x) + 10cos(x)')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.axhline(0, color='black', linewidth=0.8) # Linha do eixo X
plt.axvline(0, color='black', linewidth=0.8) # Linha do eixo Y
plt.grid(True, linestyle='--', alpha=0.6)    # Grade de fundo
plt.legend()

plt.show()