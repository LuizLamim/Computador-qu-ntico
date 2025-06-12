import matplotlib.pyplot as plt
import numpy as np

def plot_cubic_function():
    """
    Plota a função f(x) = x^3 + 3x^2 + 3x + 3.
    """
    # Gera 400 pontos igualmente espaçados entre -5 e 5 para o eixo x
    x = np.linspace(-5, 5, 400)

    # Calcula os valores de y para cada x usando a função
    y = x**3 + 3*x**2 + 3*x + 3

    # Configura a figura e o eixo do gráfico
    plt.figure(figsize=(10, 6)) # Define o tamanho da figura (largura, altura)
    plt.plot(x, y, label=r'$f(x) = x^3 + 3x^2 + 3x + 3$', color='blue') # Plota a função
    plt.title('Gráfico da Função $f(x) = x^3 + 3x^2 + 3x + 3$') # Título do gráfico
    plt.xlabel('x') # Rótulo do eixo x
    plt.ylabel('f(x)') # Rótulo do eixo y
    plt.grid(True) # Adiciona uma grade ao gráfico

    # Adiciona linhas nos eixos x=0 e y=0 para melhor visualização
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)

    plt.legend() # Mostra a legenda com a função
    plt.show() # Exibe o gráfico

if __name__ == "__main__":
    plot_cubic_function()