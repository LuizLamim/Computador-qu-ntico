import numpy as np
import matplotlib.pyplot as plt

# 1. Definir a função
def f(x):
  """
  Esta função retorna o valor de 3x.
  """
  return 3 * x

# 2. Gerar valores para o eixo x
# Criamos um intervalo de valores de -10 a 10 com 100 pontos para ter um gráfico suave.
x = np.linspace(-10, 10, 100)

# 3. Calcular os valores correspondentes para o eixo y
y = f(x)

# 4. Criar o gráfico
plt.figure(figsize=(8, 6))  # Define o tamanho da figura
plt.plot(x, y, label=r'$f(x) = 3x$', color='blue')  # Plota a linha, define a legenda e a cor

# 5. Personalizar o gráfico
plt.title('Gráfico da Função f(x) = 3x', fontsize=16)  # Título do gráfico
plt.xlabel('Eixo x', fontsize=12)  # Rótulo do eixo x
plt.ylabel('Eixo y', fontsize=12)  # Rótulo do eixo y
plt.grid(True, linestyle='--', alpha=0.6)  # Adiciona uma grade
plt.axhline(0, color='black', linewidth=0.5)  # Adiciona uma linha horizontal em y=0
plt.axvline(0, color='black', linewidth=0.5)  # Adiciona uma linha vertical em x=0
plt.legend()  # Mostra a legenda

# 6. Exibir o gráfico
plt.show()