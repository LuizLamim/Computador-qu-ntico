import numpy as np
import matplotlib.pyplot as plt

# Gera valores de x de -2*pi a 2*pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calcula sen(x)
y_seno = np.sin(x)

# Calcula a derivada de sen(x), que é cos(x)
y_cosseno = np.cos(x)

# Cria a figura e os eixos para o plot
plt.figure(figsize=(10, 6))

# Plota sen(x)
plt.plot(x, y_seno, label='$\sin(x)$', color='blue')

# Plota cos(x) (a derivada de sen(x))
plt.plot(x, y_cosseno, label='$\cos(x)$ (Derivada de $\sin(x)$)', color='red', linestyle='--')

# Adiciona título e rótulos aos eixos
plt.title('Gráfico de $\sin(x)$ e sua Derivada $\cos(x)$')
plt.xlabel('x')
plt.ylabel('y')

# Adiciona uma grade
plt.grid(True)

# Adiciona uma legenda para identificar as linhas
plt.legend()

# Define os limites do eixo y para melhor visualização
plt.ylim([-1.5, 1.5])

# Exibe o gráfico
plt.show()