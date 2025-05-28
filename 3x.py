import matplotlib.pyplot as plt
import numpy as np

# Define a função
def f(x):
  return 3*x**3 + 3*x**2 + 3*x + 3

# Cria um array de valores de x
x = np.linspace(-10, 10, 400) # Gera 400 pontos entre -10 e 10

# Calcula os valores de y correspondentes
y = f(x)

# Cria o gráfico
plt.figure(figsize=(8, 6)) # Define o tamanho da figura
plt.plot(x, y, label='f(x) = 3x³ + 3x² + 3x + 3', color='blue')

# Adiciona títulos e legendas
plt.title('Gráfico da Função $3x^3 + 3x^2 + 3x + 3$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Mostra o gráfico
plt.show()