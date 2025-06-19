import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_sine_wave():
    """
    Cria uma animação da função seno.
    """
    # Configura os parâmetros da onda
    amplitude = 1.0  # Amplitude da onda
    frequencia = 1.0 # Frequência da onda (ciclos por unidade de x)
    velocidade = 0.1 # Velocidade de propagação da onda

    # Cria a figura e o eixo para o gráfico
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2 * np.pi) # Define o limite do eixo x
    ax.set_ylim(-amplitude * 1.5, amplitude * 1.5) # Define o limite do eixo y
    ax.set_title("Animação da Função Seno")
    ax.set_xlabel("Ângulo (radianos)")
    ax.set_ylabel("Amplitude")
    ax.grid(True)

    # Inicializa a linha que será atualizada na animação
    line, = ax.plot([], [], lw=2)

    # Função de inicialização para a animação
    def init():
        line.set_data([], [])
        return line,

    # Função de animação que será chamada a cada quadro
    def update(frame):
        # Gera os valores de x
        x = np.linspace(0, 2 * np.pi, 1000)
        # Calcula os valores de y para a função seno, adicionando um deslocamento no tempo
        y = amplitude * np.sin(frequencia * x - velocidade * frame)
        # Atualiza os dados da linha
        line.set_data(x, y)
        return line,

    # Cria a animação
    # `FuncAnimation` pega a figura, a função de atualização, a função de inicialização
    # e o intervalo entre os quadros (em milissegundos)
    ani = animation.FuncAnimation(
        fig, update, frames=200, init_func=init, blit=True, interval=20
    )

    plt.show()

if __name__ == "__main__":
    animate_sine_wave()