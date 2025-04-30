import numpy as np
import matplotlib.pyplot as plt

# Definindo a função escalar f(x, y)
def f(x, y):
    return np.log(x) + y**2

# Derivadas parciais
def df_dx(x, y):
    return 1 / x

def df_dy(x, y):
    return 2 * y

# Criando uma grade de pontos
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Calculando o gradiente em cada ponto da grade
U = df_dx(X, Y)
V = df_dy(X, Y)

# Plotando o campo vetorial (gradiente)
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V, color='red')
plt.title('Campo Gradiente ∇f(x, y) para f(x, y) = ln(x) + y²')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.show()
