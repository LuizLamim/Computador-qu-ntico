import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def integrand(x):
  """Função integrando: x * sen(x)"""
  return x * np.sin(x)

def integrated_function(x):
  """Função integral de x * sen(x)"""
  result, _ = quad(integrand, 0, x)
  return result

# Cria um array de valores x
x_values = np.linspace(-10, 10, 400)

# Calcula os valores y correspondentes
y_values = [integrated_function(x) for x in x_values]

# Plota o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='∫ x sen(x) dx')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Integral de x sen(x)')
plt.grid(True)
plt.legend()
plt.show()