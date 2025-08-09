import matplotlib.pyplot as plt
import numpy as np

# Define a função
def f(x):
  """
  Calcula o valor da função f(x) = e^x + 3x
  """
  return np.exp(x) + 3 * x

# Cria um intervalo de valores para x
x_valores = np.linspace(-5, 5, 400)

# Calcula os valores correspondentes de y
y_valores = f(x_valores)

# Cria o gráfico
plt.figure(figsize=(10, 6)) # Define o tamanho da figura
plt.plot(x_valores, y_valores, label=r'$f(x) = e^x + 3x$', color='blue')

# Adiciona títulos e rótulos
plt.title('Gráfico da função $f(x) = e^x + 3x$', fontsize=16)
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)

# Adiciona uma grade para melhor visualização
plt.grid(True, linestyle='--', alpha=0.6)

# Adiciona a legenda
plt.legend(fontsize=12)

# Adiciona linhas de referência para os eixos x=0 e y=0
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Exibe o gráfico
plt.show()