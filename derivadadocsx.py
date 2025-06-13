import numpy as np
import matplotlib.pyplot as plt

# Gera valores de x de -2*pi a 2*pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calcula cos(x)
y_cosseno = np.cos(x)

# Calcula a derivada de cos(x), que é -sin(x)
y_menos_seno = -np.sin(x)

# Cria a figura e os eixos para o plot
plt.figure(figsize=(10, 6))

# Plota cos(x)
plt.plot(x, y_cosseno, label='$\cos(x)$', color='purple')

# Plota -sin(x) (a derivada de cos(x))
plt.plot(x, y_menos_seno, label='$-\sin(x)$ (Derivada de $\cos(x)$)', color='green', linestyle='--')

# Adiciona título e rótulos aos eixos
plt.title('Gráfico de $\cos(x)$ e sua Derivada $-\sin(x)$')
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