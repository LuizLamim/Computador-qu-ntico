import numpy as np
import matplotlib.pyplot as plt

# Gera valores de x de -2*pi a 2*pi com 1000 pontos para uma curva suave
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

y = np.abs(np.sin(x) * np.cos(x))

# Cria a figura e os eixos
plt.figure(figsize=(10, 6))

# Plota a função
plt.plot(x, y, label=r'$|sen(x)cos(x)|$')

plt.title(r'Gráfico da função $|sen(x)cos(x)|$', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Adiciona uma grade para facilitar a leitura
plt.grid(True, linestyle='--', alpha=0.6)

# Adiciona uma legenda
plt.legend()

# Define os limites do eixo y para uma melhor visualização
plt.ylim(0, 1.1)

# Plota os eixos x e y em 0 para referência
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Mostra o gráfico
plt.show()