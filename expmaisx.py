import numpy as np
import matplotlib.pyplot as plt

def plotar_funcao_exponencial():
    """
    Plota a função y = e^x + x.
    """
    # Cria uma lista de 1000 pontos no intervalo de -5 a 5
    x = np.linspace(-5, 5, 1000)

    # Calcula os valores correspondentes de y para a função e^x + x
    y = np.exp(x) + x

    # Cria o gráfico
    plt.figure(figsize=(10, 6))

    # Plota a função
    plt.plot(x, y, label='$y = e^x + x$', color='blue')

    # Adiciona título e rótulos aos eixos
    plt.title('Gráfico da função $y = e^x + x$', fontsize=16)
    plt.xlabel('Eixo x', fontsize=12)
    plt.ylabel('Eixo y', fontsize=12)

    # Adiciona uma grade ao gráfico para facilitar a leitura
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adiciona uma legenda
    plt.legend()

    # Adiciona linhas para os eixos x e y em 0
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Exibe o gráfico
    plt.show()

# Chama a função para gerar o gráfico
plotar_funcao_exponencial()