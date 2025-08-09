import numpy as np
import matplotlib.pyplot as plt

# 1. Definir a função
def f(x):
    """
    Calcula o valor da função f(x) = 2x + 2*sen(x) + 2*cos(x).
    """
    return 2*x + 2*np.sin(x) + 2*np.cos(x)

# 2. Gerar os dados para o gráfico
# Cria um array de 1000 pontos entre -10 e 10.
x = np.linspace(-10, 10, 1000)

# Calcula o valor de y para cada x, usando a função definida.
y = f(x)

# 3. Plotar o gráfico
plt.figure(figsize=(10, 6))  # Define o tamanho da figura (largura, altura).
plt.plot(x, y, label='$f(x) = 2x + 2\sin(x) + 2\cos(x)$', color='purple')

# Adicionar título e rótulos aos eixos
plt.title('Gráfico da função $f(x) = 2x + 2\sin(x) + 2\cos(x)$', fontsize=16)
plt.xlabel('Eixo x', fontsize=12)
plt.ylabel('Eixo y', fontsize=12)

# Adicionar grade para facilitar a leitura
plt.grid(True, linestyle='--', alpha=0.6)

# Adicionar uma legenda para identificar a linha
plt.legend(fontsize=12)

# Mostrar o gráfico
plt.show()