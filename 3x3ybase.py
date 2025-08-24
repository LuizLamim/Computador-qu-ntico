import numpy as np
import matplotlib.pyplot as plt

# 1. Reescrever a equação para isolar y
# 3x + 3y = 0
# 3y = -3x
# y = -x
def f(x):
  """
  Esta função retorna o valor de y para a equação y = -x.
  """
  return -x

# 2. Gerar valores para o eixo x
x = np.linspace(-10, 10, 100)

# 3. Calcular os valores correspondentes para o eixo y
y = f(x)

# 4. Criar o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$3x + 3y = 0 \Rightarrow y = -x$', color='red')

# 5. Personalizar o gráfico
plt.title('Gráfico da Equação $3x + 3y = 0$', fontsize=16)
plt.xlabel('Eixo x', fontsize=12)
plt.ylabel('Eixo y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()

# 6. Exibir o gráfico
plt.show()