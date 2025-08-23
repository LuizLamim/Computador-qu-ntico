import numpy as np
import matplotlib.pyplot as plt

# A função que será plotada
def f(x):
    return np.log10(x) + 10

# Gera valores para o eixo x.
# O logaritmo é definido apenas para números positivos,
# então começamos de um valor ligeiramente maior que zero.
x = np.linspace(0.1, 10, 100)

# Calcula os valores de y para cada x
y = f(x)

# Cria o gráfico
plt.figure(figsize=(8, 6))

# Plota a função
plt.plot(x, y, label=r'$y = \log_{10}(x) + 10$', color='blue')

# Adiciona título e rótulos aos eixos
plt.title('Gráfico da função $y = \log_{10}(x) + 10$')
plt.xlabel('x')
plt.ylabel('y')

# Adiciona uma grade
plt.grid(True)

# Adiciona uma legenda
plt.legend()

# Exibe o gráfico
plt.show()