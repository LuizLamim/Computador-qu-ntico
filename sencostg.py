import numpy as np
import matplotlib.pyplot as plt

def plotar_funcoes_trigonometricas():
    """
    Plota as funções trigonométricas seno, cosseno e tangente.
    """
    # Cria um array de 1000 pontos entre -2*pi e 2*pi
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    # Calcula os valores de y para cada função
    y_sen = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)

    # Cria uma figura e um conjunto de subplots
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))

    # --- Plot da função seno ---
    axs[0].plot(x, y_sen, label='sin(x)', color='blue')
    axs[0].set_title('Gráfico da função seno')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sen(x)')
    axs[0].grid(True)
    axs[0].legend()
    # Adiciona a linha do eixo x em y=0
    axs[0].axhline(0, color='black', linewidth=0.5)
    # Adiciona a linha do eixo y em x=0
    axs[0].axvline(0, color='black', linewidth=0.5)

    # --- Plot da função cosseno ---
    axs[1].plot(x, y_cos, label='cos(x)', color='red')
    axs[1].set_title('Gráfico da função cosseno')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')
    axs[1].grid(True)
    axs[1].legend()
    axs[1].axhline(0, color='black', linewidth=0.5)
    axs[1].axvline(0, color='black', linewidth=0.5)

    # --- Plot da função tangente ---
    axs[2].plot(x, y_tan, label='tan(x)', color='green')
    axs[2].set_title('Gráfico da função tangente')
    axs[2].set_xlabel('x')
    axs[2].set_ylabel('tan(x)')
    axs[2].set_ylim(-10, 10) # Limita o eixo y para evitar assíntotas infinitas
    axs[2].grid(True)
    axs[2].legend()
    axs[2].axhline(0, color='black', linewidth=0.5)
    axs[2].axvline(0, color='black', linewidth=0.5)

    # Ajusta o layout para evitar sobreposição de títulos e rótulos
    plt.tight_layout()

    # Mostra os gráficos
    plt.show()

# Chama a função para executar o programa
if __name__ == '__main__':
    plotar_funcoes_trigonometricas()