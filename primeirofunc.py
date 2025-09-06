import matplotlib.pyplot as plt
import numpy as np

# A função que queremos plotar
def f(x):
  return 33 * x + 3

# Cria 100 pontos no eixo x, de -10 a 10
x = np.linspace(-10, 10, 100)

# Calcula os valores correspondentes de y para cada x
y = f(x)

# Cria o gráfico
plt.figure(figsize=(8, 6)) # Define o tamanho da figura (opcional)
plt.plot(x, y, label='y = 33x + 3', color='blue')

# Adiciona título e rótulos aos eixos
plt.title('Gráfico da Função Linear y = 33x + 3', fontsize=16)
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)

# Adiciona uma grade ao gráfico
plt.grid(True, linestyle='--', alpha=0.6)

# Adiciona uma legenda
plt.legend()

# Adiciona linhas nos eixos x=0 e y=0 para melhor visualização
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')

# Exibe o gráfico
plt.show()