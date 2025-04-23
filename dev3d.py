import sympy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define as variáveis simbólicas
x, y = sympy.symbols('x y')

# Insira a função da qual você quer plotar a derivada parcial
# Exemplo: f = x**2 + y**3
f = sympy.sin(x) * sympy.cos(y)

# Escolha a variável para a derivada parcial
# Opções: x ou y
variavel_derivada = x

# Calcula a derivada parcial
derivada_parcial = sympy.diff(f, variavel_derivada)

# Converte a expressão simbólica para uma função numérica para plotagem
f_num = sympy.lambdify((x, y), f, 'numpy')
derivada_parcial_num = sympy.lambdify((x, y), derivada_parcial, 'numpy')

# Cria o espaço de amostragem para x e y
num = 50
x_vals = np.linspace(-5, 5, num)
y_vals = np.linspace(-5, 5, num)
X, Y = np.meshgrid(x_vals, y_vals)

# Calcula os valores de Z (função original) e Z_derivada (derivada parcial)
Z = f_num(X, Y)
Z_derivada = derivada_parcial_num(X, Y)

# Cria a figura e os subplots 3D
fig = plt.figure(figsize=(12, 6))

# Subplot para a função original
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')
ax1.set_title('Função Original: ' + str(f))
fig.colorbar(surf1)

# Subplot para a derivada parcial
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(X, Y, Z_derivada, cmap='coolwarm')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel(f'∂f/∂{variavel_derivada}')
ax2.set_title(f'Derivada Parcial em relação a {variavel_derivada}: ' + str(derivada_parcial))
fig.colorbar(surf2)

plt.tight_layout()
plt.show()