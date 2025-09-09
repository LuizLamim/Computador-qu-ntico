import matplotlib.pyplot as plt
import numpy as np

# A função que representa a equação
def f(x):
  return 400 * x + 2

# Cria um intervalo de valores para x.
# O np.linspace gera 100 pontos entre -10 e 10, o que é um bom intervalo para a maioria dos casos.
x = np.linspace(-10, 10, 100)

# Calcula os valores correspondentes de y
y = f(x)

# Plota a linha
plt.plot(x, y, label='y = 400x + 2')

# Adiciona títulos e rótulos
plt.title('Gráfico da Equação y = 400x + 2')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adiciona uma grade
plt.grid(True)

# Adiciona uma legenda
plt.legend()

# Exibe o gráfico
plt.show()