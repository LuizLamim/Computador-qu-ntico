import numpy as np
import matplotlib.pyplot as plt

# 1. Gerar os dados para o eixo x
# Criamos um array de 1000 pontos entre -2*pi e 2*pi para garantir um gráfico suave.
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 2. Calcular os valores da função para o eixo y
# Aplicamos a função cosseno a cada ponto de 'x' e, em seguida,
# calculamos o valor absoluto de cada resultado.
y = np.abs(np.cos(x))

# 3. Criar a figura e os eixos do gráfico
# Definimos um tamanho de figura para melhor visualização.
plt.figure(figsize=(10, 6))

# 4. Plotar a função
# Desenhamos o gráfico usando os dados de x e y.
plt.plot(x, y, color='red', label='|cos(x)|')

# 5. Adicionar rótulos e título
# Isso torna o gráfico mais fácil de entender.
plt.title('Gráfico da função f(x) = |cos(x)|', fontsize=16)
plt.xlabel('Eixo x', fontsize=12)
plt.ylabel('Eixo y', fontsize=12)
plt.legend()
plt.grid(True)

# 6. Exibir o gráfico
# Este comando mostra a janela com o gráfico plotado.
plt.show()