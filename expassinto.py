import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def animate_log_function():
    fig, ax = plt.subplots(figsize=(8, 6))
    x_data = []
    y_data = []

    # Configurações iniciais do gráfico
    ax.set_title("Animação de uma Função Logarítmica com Assíntota Vertical")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_xlim(-1, 10)
    ax.set_ylim(-5, 5)
    ax.grid(True)

    # Linha para a função
    line, = ax.plot([], [], 'b-', lw=2)
    # Linha para a assíntota vertical
    asymptote_line, = ax.plot([], [], 'r--', lw=1.5, label="Assíntota Vertical")
    ax.legend()

    # Ponto da assíntota vertical (vamos fixar em x=1 para este exemplo)
    vertical_asymptote_x = 1

    def init():
        line.set_data([], [])
        asymptote_line.set_data([], [])
        return line, asymptote_line

    def update(frame):
        # Aumenta o domínio da função gradualmente
        x_values = np.linspace(vertical_asymptote_x + 0.01, vertical_asymptote_x + 0.01 + frame * 0.1, 500)
        y_values = np.log(x_values - vertical_asymptote_x) # ln(x - c)

        line.set_data(x_values, y_values)

        # Desenha a assíntota vertical
        asymptote_line.set_data([vertical_asymptote_x, vertical_asymptote_x], ax.get_ylim())

        return line, asymptote_line

    # Cria a animação
    # frames: número de passos na animação
    # interval: tempo entre cada frame em ms
    ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

    plt.show()

if __name__ == "__main__":
    animate_log_function()