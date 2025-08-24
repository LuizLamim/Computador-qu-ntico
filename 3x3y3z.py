import numpy as np
import matplotlib.pyplot as plt

# Importar o módulo para plotagem 3D
from mpl_toolkits.mplot3d import Axes3D

# 1. Definir a equação para z em termos de x e y
def z_function(x, y):
  """
  Esta função retorna o valor de z para a equação z = -x - y.
  """
  return -x - y

# 2. Criar uma grade de valores para os eixos x e y
# np.meshgrid cria duas matrizes 2D para todos os pares de coordenadas (x, y)
x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)
X, Y = np.meshgrid(x, y)

# 3. Calcular os valores correspondentes para o eixo z
Z = z_function(X, Y)

# 4. Criar a figura e o eixo 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 5. Plotar a superfície
ax.plot_surface(X, Y, Z, cmap='viridis')

# 6. Personalizar o gráfico
ax.set_title('Gráfico do Plano $3x + 3y + 3z = 0$', fontsize=16)
ax.set_xlabel('Eixo x', fontsize=12)
ax.set_ylabel('Eixo y', fontsize=12)
ax.set_zlabel('Eixo z', fontsize=12)

# 7. Exibir o gráfico
plt.show()