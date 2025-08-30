import matplotlib.pyplot as plt
import numpy as np

def plotar_funcao_1_sobre_x():
    """
    Plota o gráfico da função f(x) = 1/x.

    O gráfico é dividido em duas partes, uma para valores negativos de x
    e outra para valores positivos, para evitar o ponto de descontinuidade em x=0.
    """
    # Cria uma sequência de 1000 pontos para o gráfico.
    # A função np.linspace cria um array de números uniformemente espaçados.
    # Excluímos o zero para evitar a divisão por zero.
    x_negativo = np.linspace(-10, -0.1, 500)
    x_positivo = np.linspace(0.1, 10, 500)

    # Calcula os valores de y para cada intervalo de x.
    y_negativo = 1 / x_negativo
    y_positivo = 1 / x_positivo

    # Configura a figura e os eixos do gráfico.
    plt.figure(figsize=(10, 8))
    
    # Plota a parte negativa do gráfico.
    plt.plot(x_negativo, y_negativo, label=r'$f(x) = 1/x$', color='blue')
    
    # Plota a parte positiva do gráfico.
    plt.plot(x_positivo, y_positivo, color='blue')

    # Adiciona uma linha vertical pontilhada no eixo y (x=0)
    # para indicar a assíntota vertical.
    plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.8, label='Assíntota Vertical')

    # Adiciona uma linha horizontal pontilhada no eixo x (y=0)
    # para indicar a assíntota horizontal.
    plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8, label='Assíntota Horizontal')

    # Configura os rótulos e o título do gráfico.
    plt.title('Gráfico da Função $f(x) = 1/x$')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True)
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Exibe o gráfico.
    plt.show()

# Chama a função para gerar o gráfico.
if __name__ == "__main__":
    plotar_funcao_1_sobre_x()