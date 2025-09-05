import numpy as np
import matplotlib.pyplot as plt

def f(x):
  """
  Calcula o valor da função f(x) = tan(x) + 37x.
  """
  return np.tan(x) + 37 * x

# Cria um intervalo de valores para x.
# O intervalo foi escolhido para evitar as descontinuidades da tangente (pi/2, 3pi/2, etc.).
# Você pode ajustar o intervalo se precisar de uma visualização diferente.
x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

# Calcula os valores de y para cada valor de x.
y = f(x)

# Plota o gráfico.
plt.figure(figsize=(11, 7))  # Define o tamanho da figura
plt.plot(x, y, label='tan(x) + 37x', color='red')

# Adiciona título e rótulos aos eixos
plt.title('Gráfico da função $f(x) = \\tan(x) + 37x$')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

# Adiciona uma grade ao gráfico
plt.grid(True)

# Adiciona a legenda
plt.legend()

# Exibe o gráfico
plt.show()