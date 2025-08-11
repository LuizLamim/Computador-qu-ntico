import matplotlib.pyplot as plt
import numpy as np

# Cria uma sequência de 1000 pontos entre -10 e 10
# Isso garante que a curva do gráfico seja suave
x = np.linspace(-10, 10, 1000)

# Calcula o valor de y para cada ponto x, usando a função y = x^3
y = x**3

# Cria o plot
plt.figure(figsize=(8, 6)) # Define o tamanho da figura para melhor visualização
plt.plot(x, y, label='$f(x) = x^3$', color='blue') # Plota os pontos x e y com uma cor e um rótulo

# Adiciona título e rótulos aos eixos para deixar o gráfico mais claro
plt.title('Gráfico da função $f(x) = x^3$')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

# Adiciona uma grade ao gráfico para facilitar a leitura dos valores
plt.grid(True)

# Adiciona uma legenda que identifica a função no gráfico
plt.legend()

# Exibe o gráfico
plt.show()