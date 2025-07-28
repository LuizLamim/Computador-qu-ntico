import numpy as np
import matplotlib.pyplot as plt

# 1. Criar um intervalo de valores para x
# Usamos np.linspace para gerar 1000 pontos entre -2*pi e 2*pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 2. Calcular os valores de y para a função sen(x) + cos(x)
y = np.sin(x) + np.cos(x)

# 3. Criar o gráfico
plt.figure(figsize=(10, 6)) # Define o tamanho da figura (opcional)
plt.plot(x, y, label='sen(x) + cos(x)', color='blue')

# 4. Adicionar rótulos e título
plt.title('Gráfico da Função sen(x) + cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True) # Adiciona uma grade ao gráfico
plt.axhline(0, color='black',linewidth=0.5) # Linha horizontal no y=0
plt.axvline(0, color='black',linewidth=0.5) # Linha vertical no x=0
plt.legend() # Mostra a legenda (o label que definimos no plt.plot)

# 5. Exibir o gráfico
plt.show()