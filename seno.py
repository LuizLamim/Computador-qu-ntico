import numpy as np
import matplotlib.pyplot as plt

# Cria um array de valores para o eixo x
x = np.linspace(0, 2 * np.pi, 100)

# Calcula os valores correspondentes para o eixo y (função seno)
y = np.sin(x)

# Plota o gráfico
plt.plot(x, y, color='red')

# Adiciona um título ao gráfico
plt.title('Gráfico da Função Seno')

# Adiciona rótulos aos eixos x e y
plt.xlabel('Ângulo (radianos)')
plt.ylabel('sen(ângulo)')

# Exibe o grid no gráfico
plt.grid(True)

# Mostra o gráfico
plt.show()