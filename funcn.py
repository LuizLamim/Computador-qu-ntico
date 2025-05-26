import matplotlib.pyplot as plt
import numpy as np

# 1. Definir a função
def f(x):
    return 3 * x**2 + 2 * x + 3

# 2. Gerar valores para x
# Vamos criar um intervalo de x para plotar a função
x = np.linspace(-10, 10, 400) # De -10 a 10, com 400 pontos para um gráfico suave

# 3. Calcular os valores correspondentes de y
y = f(x)

# 4. Criar o gráfico
plt.figure(figsize=(8, 6)) # Define o tamanho da figura
plt.plot(x, y, label='$3x^2 + 2x + 3$', color='blue') # Plota a função

# 5. Adicionar rótulos e título
plt.title('Gráfico da Função $f(x) = 3x^2 + 2x + 3$')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True) # Adiciona uma grade ao gráfico
plt.axhline(0, color='black',linewidth=0.5) # Adiciona o eixo X
plt.axvline(0, color='black',linewidth=0.5) # Adiciona o eixo Y
plt.legend() # Mostra a legenda da função

# 6. Exibir o gráfico
plt.show()