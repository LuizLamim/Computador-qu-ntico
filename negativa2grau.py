import matplotlib.pyplot as plt
import numpy as np

# A função é f(x) = -3x + 3x + 3, que simplifica para f(x) = 3
def f(x):
    return 3

# Cria um conjunto de valores para x (de -10 a 10)
x_vals = np.linspace(-10, 10, 400)

# Calcula os valores correspondentes de y
y_vals = f(x_vals)

# Configura a plotagem
plt.figure(figsize=(9, 6))
plt.plot(x_vals, y_vals, label='y = -3x + 3x + 3  ou  y = 3', color='red')

# Adiciona título e rótulos
plt.title('Gráfico da função f(x) = 3')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

# Adiciona uma grade e a legenda
plt.grid(True)
plt.legend()

# Adiciona uma linha horizontal em y = 0 para melhor visualização
plt.axhline(0, color='black', linewidth=0.5)
# Adiciona uma linha vertical em x = 0
plt.axvline(0, color='black', linewidth=0.5)

# Mostra o gráfico
plt.show()