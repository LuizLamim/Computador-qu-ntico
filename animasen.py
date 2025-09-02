import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configura a figura e os eixos do plot
fig, ax = plt.subplots()
# Define os limites do eixo x de -2π a 2π
x_data = np.linspace(-2 * np.pi, 2 * np.pi, 390)
# Define os limites do eixo y de -1.1 a 1.1
ax.set_ylim(-1.1, 1.1)
# Configura o rótulo do eixo x
ax.set_xlabel("x")
# Configura o rótulo do eixo y
ax.set_ylabel("sen(x)")
# Configura o título do gráfico
ax.set_title("Animação da Função Seno")
# Desenha a grade no plano de fundo
ax.grid(True)

# Cria um objeto de linha vazio que será atualizado na animação
line, = ax.plot([], [], lw=2)

# Função de inicialização da animação
def init():
    # Define os dados iniciais da linha como vazios
    line.set_data([], [])
    # Retorna o objeto de linha
    return line,

# Função de animação que será chamada a cada frame
def animate(i):
    # Calcula os dados de y para a função seno
    y_data = np.sin(x_data + i * 0.1)
    # Define os novos dados para a linha
    line.set_data(x_data, y_data)
    # Retorna o objeto de linha
    return line,

# Cria a animação usando FuncAnimation
ani = FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=80,  # Número de quadros (frames) da animação
    interval=50,  # Intervalo de tempo entre os quadros em milissegundos
    blit=True  # Otimiza o desenho atualizando apenas o que mudou
)

# Exibe o gráfico com a animação
plt.show()