import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o intervalo de valores para x
# O np.linspace cria um array de 100 pontos uniformemente espaçados entre -10 e 10.
x = np.linspace(-10, 10, 100)

# 2. Calcular os valores de y para cada x, com base na função y = 3x + 2
y = 3*x + 2

# 3. Criar a figura e os eixos do gráfico
plt.figure(figsize=(8, 6))

# 4. Plotar o gráfico
plt.plot(x, y, label='y = 3x + 1 + log(10)  (ou seja, y = 3x + 2)', color='blue')

# 5. Adicionar título e rótulos aos eixos
plt.title('Gráfico da Função Linear', fontsize=16)
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)

# 6. Adicionar grade para melhor visualização
plt.grid(True)

# 7. Adicionar a legenda
plt.legend()

# 8. Mostrar o gráfico
plt.show()