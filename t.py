import numpy as np
import matplotlib.pyplot as plt

# Define a função para um componente simplificado do tensor de Einstein
def componente_einstein(x, y):
  """
  Função de exemplo para um componente do tensor de Einstein em 2D.
  Esta é uma função arbitrária para fins de visualização.
  Em um cenário real, essa função seria derivada de uma métrica do espaço-tempo.
  """
  r_squared = x**2 + y**2
  return np.exp(-r_squared) * (2 * r_squared - 1)

# Cria uma grade de pontos (x, y)
num_pontos = 100
x = np.linspace(-5, 5, num_pontos)
y = np.linspace(-5, 5, num_pontos)
X, Y = np.meshgrid(x, y)

# Calcula o valor do componente em cada ponto da grade
Z = componente_einstein(X, Y)

# Cria o gráfico de mapa de cores
plt.figure(figsize=(8, 6))
plt.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', cmap='viridis')
plt.colorbar(label='Valor do Componente')
plt.xlabel('Coordenada Espacial x')
plt.ylabel('Coordenada Espacial y')
plt.title('Visualização Simplificada de um Componente do Tensor de Einstein')
plt.grid(True)
plt.show()