import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o intervalo de x
# Vamos gerar valores de x de -10 a 10 para ter uma boa visualização
x = np.linspace(-10, 10, 400) # 400 pontos para uma linha suave

# 2. Definir as funções
y1 = 3*x + 3   # Primeira função: y = 3x + 3
y2 = -3*x + 3  # Segunda função: y = -3x + 3

# 3. Criar o gráfico
plt.figure(figsize=(8, 6)) # Define o tamanho da figura (largura, altura em polegadas)

# Plotar a primeira função
plt.plot(x, y1, label='y = 3x + 3', color='blue', linestyle='-')

# Plotar a segunda função
plt.plot(x, y2, label='y = -3x + 3', color='red', linestyle='--')

# 4. Adicionar elementos ao gráfico
plt.title('Gráfico das Funções y = 3x + 3 e y = -3x + 3') # Título do gráfico
plt.xlabel('Eixo X') # Rótulo do eixo X
plt.ylabel('Eixo Y') # Rótulo do eixo Y
plt.grid(True) # Adiciona uma grade ao gráfico
plt.axhline(0, color='black', linewidth=0.5) # Linha no eixo X (y=0)
plt.axvline(0, color='black', linewidth=0.5) # Linha no eixo Y (x=0)
plt.legend() # Mostra a legenda com os rótulos das funções

# 5. Exibir o gráfico
plt.show()