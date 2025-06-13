import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def animate_ln_x_function():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Configurações iniciais do gráfico
    ax.set_title("Animação da Função y = ln(x) com Assíntota Vertical")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_xlim(-1, 10) # X não pode ser menor ou igual a 0 para ln(x)
    ax.set_ylim(-5, 5)
    ax.grid(True)

    # Linha para a função ln(x)
    line, = ax.plot([], [], 'b-', lw=2, label="y = ln(x)")
    # Linha para a assíntota vertical em x = 0
    asymptote_line, = ax.plot([], [], 'r--', lw=1.5, label="Assíntota Vertical (x=0)")
    ax.legend()

    # A assíntota vertical para ln(x) é sempre em x = 0
    vertical_asymptote_x = 0

    def init():
        line.set_data([], [])
        asymptote_line.set_data([], [])
        return line, asymptote_line

    def update(frame):
        # Gera valores de x. Começamos um pouco depois de 0 para evitar log(0)
        # e estendemos o domínio gradualmente
        x_values = np.linspace(0.01, 0.01 + frame * 0.1, 500)
        y_values = np.log(x_values) # Função ln(x)

        line.set_data(x_values, y_values)

        # Desenha a assíntota vertical em x=0
        asymptote_line.set_data([vertical_asymptote_x, vertical_asymptote_x], ax.get_ylim())

        return line, asymptote_line

    # Cria a animação
    # frames: número de passos na animação
    # interval: tempo entre cada frame em ms
    ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

    plt.show()

if __name__ == "__main__":
    animate_ln_x_function()