import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo de x
x = np.linspace(-2 * np.pi, 2 * np.pi, 400) # De -2pi a 2pi, com 400 pontos para suavidade

# 2. Calcular os valores de y para a função
y = np.sin(x) + 35 * np.cos(x)

# 3. Criar o gráfico
plt.figure(figsize=(10, 6)) # Define o tamanho da figura para melhor visualização
plt.plot(x, y, label=r'$f(x) = \sin(x) + 35\cos(x)$', color='blue')

# 4. Adicionar título e rótulos aos eixos
plt.title('Gráfico da função $f(x) = \sin(x) + 35\cos(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')

# 5. Adicionar grade e legenda
plt.grid(True)
plt.legend()

# 6. Adicionar linha horizontal no y=0 e linha vertical no x=0
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# 7. Exibir o gráfico
plt.show()