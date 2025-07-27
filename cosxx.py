import numpy as np
import matplotlib.pyplot as plt

# 1. Gerar os valores de x
# Vamos criar um array de 1000 pontos entre -10 e 10 para uma curva suave.
x = np.linspace(-10, 10, 1000)

# 2. Calcular os valores de y (cos(x) + x)
y = np.cos(x) + x

# 3. Criar o gráfico
plt.figure(figsize=(10, 6)) # Define o tamanho da figura (largura, altura)
plt.plot(x, y, label='$cos(x) + x$', color='blue') # Plota a função

# 4. Adicionar rótulos e título
plt.title('Gráfico da Função $f(x) = cos(x) + x$', fontsize=16)
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7) # Adiciona um grid ao gráfico
plt.axhline(0, color='black', linewidth=0.5) # Linha no eixo X=0
plt.axvline(0, color='black', linewidth=0.5) # Linha no eixo Y=0
plt.legend(fontsize=12) # Mostra a legenda com o nome da função

# 5. Mostrar o gráfico
plt.show()