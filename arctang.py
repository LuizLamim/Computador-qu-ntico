import numpy as np
import matplotlib.pyplot as plt

# Gera um intervalo de valores para x
x = np.linspace(-5, 5, 400) # De -5 a 5, com 400 pontos para uma curva suave

# Calcula a derivada do arco tangente para cada valor de x
# A derivada de arctan(x) é 1 / (1 + x^2)
y = 1 / (1 + x**2)

# Cria o gráfico
plt.figure(figsize=(10, 6)) # Define o tamanho da figura
plt.plot(x, y, label=r"Derivada de $\arctan(x) = \frac{1}{1 + x^2}$", color='blue')

# Adiciona título e rótulos aos eixos
plt.title("Gráfico da Derivada do Arco Tangente")
plt.xlabel("x")
plt.ylabel("f'(x)")

# Adiciona uma grade ao gráfico
plt.grid(True)

# Adiciona a legenda
plt.legend()

# Adiciona linhas nos eixos x=0 e y=0 para melhor referência
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Exibe o gráfico
plt.show()