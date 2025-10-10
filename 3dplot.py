import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o domínio da função (valores de x e y)
# Criamos um array de pontos de -5 a 5 com 50 passos
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

# Criamos uma malha de coordenadas (grid) a partir dos arrays de x e y
# X e Y serão matrizes 50x50, o que é necessário para o plot 3D
X, Y = np.meshgrid(x, y)

# 2. Calcular os valores da função Z = 2 * X * Y
Z = 2 * X * Y

# 3. Criar a figura e o eixo 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

# 4. Plotar o gráfico de superfície
# O 'cmap' define o esquema de cores. 'viridis' é um bom padrão.
surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=False)
