import matplotlib.pyplot as plt
import numpy as np

# Definir a massa (m) como uma constante
massa = 10  # em kg

# Criar um array de valores para a aceleração (a)
# de 0 a 10, com 100 pontos
aceleracao = np.linspace(0, 10, 100)  # em m/s²

# Calcular a força (F) para cada valor de aceleração
forca = massa * aceleracao  # F = m * a

# Criar o gráfico
plt.figure(figsize=(8, 6))  # Define o tamanho da figura
plt.plot(aceleracao, forca, label=f'massa = {massa} kg', color='blue')

# Adicionar títulos e rótulos
plt.title('Força vs. Aceleração (massa constante)')
plt.xlabel('Aceleração (m/s²)')
plt.ylabel('Força (N)')
plt.legend()
plt.grid(True)  # Adiciona a grade
plt.show()