import numpy as np
import matplotlib.pyplot as plt

# Definir o intervalo para x
# Evitamos pontos onde cos(x) é zero para evitar divisão por zero
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
x = x[np.cos(x) != 0] # Remover os pontos onde cos(x) é zero

# Calcular a função secante: sec(x) = 1 / cos(x)
y = 1 / np.cos(x)

# Criar o gráfico
plt.figure(figsize=(10, 6)) # Define o tamanho da figura
plt.plot(x, y, label='sec(x) = 1/cos(x)', color='blue')

# Adicionar linhas de grade
plt.grid(True, linestyle='--', alpha=0.7)

# Adicionar rótulos e título
plt.xlabel('x (radianos)')
plt.ylabel('sec(x)')
plt.title('Gráfico da Função Secante')

# Adicionar linha do eixo X em y=0
plt.axhline(0, color='black', linewidth=0.5)
# Adicionar linha do eixo Y em x=0
plt.axvline(0, color='black', linewidth=0.5)

# Definir limites do eixo Y para melhor visualização, especialmente com assíntotas
plt.ylim(-10, 10)

# Adicionar legendas
plt.legend()

# Mostrar o gráfico
plt.show()