import numpy as np
import matplotlib.pyplot as plt

# 1. Definir a função logarítmica com base 4
def log_base_4(x):
    """Calcula o logaritmo de x na base 4."""
    return np.log(x) / np.log(4)

# 2. Gerar valores para o eixo x
# O logaritmo é definido apenas para x > 0
x_values = np.linspace(0.1, 10, 400)  # De 0.1 a 10, com 400 pontos

# 3. Calcular os valores correspondentes para o eixo y
y_values = log_base_4(x_values)

# 4. Criar o gráfico
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.plot(x_values, y_values, label='$y = \log_4(x)$', color='blue')

# 5. Adicionar rótulos e título
plt.title('Gráfico da Função Logarítmica Base 4')
plt.xlabel('x')
plt.ylabel('$f(x) = \log_4(x)$')

# 6. Adicionar grade e legenda
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5) # Eixo x
plt.axvline(0, color='black',linewidth=0.5) # Eixo y
plt.legend()

# 7. Exibir o gráfico
plt.show()