import numpy as np
import matplotlib.pyplot as plt

# Definindo a função escalar
def f(x, y):
    return x**2 + y**2

# Calculando o gradiente da função
def grad_f(x, y):
    df_dx = 2 * x
    df_dy = 2 * y
    return np.array([df_dx, df_dy])

# Criando uma malha de pontos (grid)
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Calculando o gradiente em cada ponto
U, V = grad_f(X, Y)

# Plotando o campo de vetores
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V, color='blue')
plt.title('Vetor Gradiente de f(x, y) = x² + y²')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.show()
