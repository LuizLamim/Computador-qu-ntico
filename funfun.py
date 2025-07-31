import numpy as np
import matplotlib.pyplot as plt

# Define a função
def f(x):
  """
  Calcula a função x*cos(x) + sin(x).
  """
  return x * np.cos(x) + np.sin(x)

# Cria o domínio da função (o intervalo de x)
x = np.linspace(-10, 10, 400) # De -10 a 10, com 400 pontos para uma curva suave

# Calcula os valores de y para cada x
y = f(x)

# Cria a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Plota a função
ax.plot(x, y, label=r'$f(x) = x \cos(x) + \sin(x)$', color='blue')

# Adiciona o título e os rótulos dos eixos
ax.set_title('Gráfico da função $f(x) = x \cos(x) + \sin(x)$', fontsize=16)
ax.set_xlabel('Eixo x', fontsize=12)
ax.set_ylabel('Eixo y', fontsize=12)

# Adiciona uma grade para facilitar a leitura
ax.grid(True, linestyle='--', alpha=0.6)

# Adiciona uma legenda
ax.legend(fontsize=12)

# Adiciona linhas nos eixos x=0 e y=0 para referência
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)

# Mostra o gráfico
plt.show()