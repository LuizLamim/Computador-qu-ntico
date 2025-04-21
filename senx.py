import numpy as np
import matplotlib.pyplot as plt

# Cria um array de valores x espaçados linearmente de 0 a 2*pi
x = np.linspace(0, 2 * np.pi, 100)

# Calcula os valores de y para a função seno
y = np.sin(x)

# Cria a figura e os eixos do gráfico
fig, ax = plt.subplots()

# Plota a função seno
ax.plot(x, y)

# Adiciona um título ao gráfico
ax.set_title('Gráfico da Função Seno (sin x)')

# Adiciona rótulos aos eixos x e y
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')

# Adiciona uma grade ao gráfico (opcional)
ax.grid(True)

# Exibe o gráfico
plt.show()