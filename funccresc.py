import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define a função exponencial
def exponential_function(x, base):
    return base**x

# Define os parâmetros da animação
base = 2  # Base da função exponencial
tempo = np.linspace(0, 5, 100) # Intervalo de tempo (eixo x)
fig, ax = plt.subplots()
linha, = ax.plot([], [], 'r-', linewidth=2)
ax.set_xlim(0, 5)
ax.set_ylim(0, exponential_function(5, base) * 1.1) # Ajusta o limite y dinamicamente
ax.set_xlabel('Tempo')
ax.set_ylabel(f'Valor ({base}^t)')
ax.set_title(f'Animação do Crescimento Exponencial ({base}^t)')
ax.grid(True)

# Função para atualizar o gráfico a cada frame
def atualizar(frame):
    x_data = tempo[:frame+1]
    y_data = exponential_function(x_data, base)
    linha.set_data(x_data, y_data)
    return linha,

# Cria a animação
ani = animation.FuncAnimation(fig, atualizar, frames=len(tempo), interval=50, blit=True)

plt.show()