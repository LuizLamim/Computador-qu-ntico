import numpy as np
import matplotlib.pyplot as plt

# 1. Gerar valores para x
# Usamos np.linspace para criar um intervalo de valores de -2*pi a 2*pi
# (que cobre duas ondas completas do seno) com muitos pontos para uma curva suave.
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# 2. Calcular os valores correspondentes de y
# Aplicamos a função seno e adicionamos 3 a cada valor de x
y = np.sin(x) + 3

# 3. Criar o gráfico
plt.figure(figsize=(10, 6)) # Define o tamanho da figura para melhor visualização
plt.plot(x, y, label=r'$y = \sin(x) + 3$', color='blue') # Plota a linha, adiciona um rótulo e cor

# 4. Adicionar rótulos e título
plt.title('Gráfico da Função $y = \sin(x) + 3$')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# 5. Adicionar grade para facilitar a leitura
plt.grid(True)

# 6. Adicionar a legenda
plt.legend()

# 7. Exibir o gráfico
plt.show()