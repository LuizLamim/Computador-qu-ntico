import numpy as np
import matplotlib.pyplot as plt

# Cria um array de valores para x no intervalo de -2π a 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calcula os valores da função f(x) = 3sin(x) + 25cos(x)
y_funcao = 3 * np.sin(x) + 25 * np.cos(x)

# Cria um array para a linha horizontal y = 18
y_constante = np.full_like(x, 18)

# Configurações do gráfico
plt.figure(figsize=(10, 6))

# Plota a função
plt.plot(x, y_funcao, label='$f(x) = 3\sin(x) + 25\cos(x)$', color='blue')

# Plota a linha y = 18
plt.plot(x, y_constante, label='$y = 18$', color='red', linestyle='--')

# Adiciona título e rótulos aos eixos
plt.title('Gráfico da Equação $3\sin(x) + 25\cos(x) = 18$')
plt.xlabel('x')
plt.ylabel('y')

# Adiciona uma grade para facilitar a leitura
plt.grid(True, linestyle=':', alpha=0.6)

# Adiciona uma legenda para identificar as curvas
plt.legend()

# Plota as linhas nos eixos x e y para melhor visualização
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Define os limites dos eixos para uma visualização clara
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.ylim(min(y_funcao) - 2, max(y_funcao) + 2)

# Exibe o gráfico
plt.show()