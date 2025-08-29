import numpy as np
import matplotlib.pyplot as plt

# Define a função
def f(x):
  """
  Calcula o valor da função 13 * cos(x).
  """
  return 13 * np.cos(x)

# Cria um array de valores para o eixo x
# Usamos np.linspace para gerar 1000 pontos entre -2*pi e 2*pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calcula os valores correspondentes para o eixo y
y = f(x)

# Cria a figura e o eixo para o gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Plota a função
ax.plot(x, y, label=r'$f(x) = 13 \cos(x)$', color='blue', linewidth=2)

# Adiciona título e rótulos aos eixos
ax.set_title('Gráfico da função $f(x) = 13 \cos(x)$', fontsize=16)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)

# Adiciona grade para facilitar a leitura
ax.grid(True, linestyle='--', alpha=0.6)

# Adiciona uma linha horizontal em y=0 para melhor visualização
ax.axhline(0, color='black', linewidth=0.5)

# Adiciona uma linha vertical em x=0 para melhor visualização
ax.axvline(0, color='black', linewidth=0.5)

# Adiciona a legenda
ax.legend(fontsize=12)

# Mostra o gráfico
plt.show()