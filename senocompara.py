import numpy as np
import matplotlib.pyplot as plt

# Definir o intervalo de x, de -2*pi a 2*pi
# Usamos np.linspace para gerar 200 pontos nesse intervalo para um plot suave
x = np.linspace(-2 * np.pi, 2 * np.pi, 200)

# Calcular os valores de y para as duas funções
y_seno = np.sin(x)
y_abs_seno = np.abs(np.sin(x))

# Criar a figura e o eixo do plot
plt.figure(figsize=(10, 6))

# Plotar a função seno(x)
plt.plot(x, y_seno, label='sin(x)', color='blue')

# Plotar a função |seno(x)|
plt.plot(x, y_abs_seno, label='|sin(x)|', color='orange')

# Adicionar título e rótulos aos eixos
plt.title('Gráfico de $sin(x)$ e $|sin(x)|$')
plt.xlabel('x (em radianos)')
plt.ylabel('y')

# Adicionar uma grade para facilitar a leitura
plt.grid(True)

# Adicionar uma legenda para identificar as funções
plt.legend()

# Mostrar o gráfico
plt.show()