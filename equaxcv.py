import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 20, 100)

# 2. Definir a função (valores de y)
# y = -x + 15
y = -x + 15

# 3. Criar a figura e o gráfico
plt.figure(figsize=(8, 6))  # Define o tamanho da figura (opcional)
plt.plot(x, y, label='$y = -x + 15$', color='blue') # Plota a linha

# 4. Adicionar elementos ao gráfico para torná-lo mais informativo
plt.title('Gráfico da Função Linear $y = -x + 15$')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adiciona uma grade (opcional)
plt.grid(True)

# Adiciona a legenda (importante se houver múltiplas linhas)
plt.legend()