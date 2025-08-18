import numpy as np
import matplotlib.pyplot as plt

def plot_tan_abs_plus_2x():
    """
    Plota a função f(x) = |tan(x)| + 2x no intervalo de -2pi a 2pi.
    """
    # Cria um array de valores x no intervalo de -2pi a 2pi.
    # Usamos 1000 pontos para garantir uma curva suave.
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    # Calcula os valores de y para a função f(x) = |tan(x)| + 2x.
    y = np.abs(np.tan(x)) + 2 * x

    # Cria a figura e os eixos do gráfico.
    plt.figure(figsize=(10, 6))

    # Plota a função.
    # 'g-' define a cor da linha como verde ('g') e o estilo como sólido ('-').
    plt.plot(x, y, 'g-', label=r'$f(x) = |\tan(x)| + 2x$')

    # Configura os limites do eixo y.
    # Isso evita que o gráfico se estenda infinitamente devido às assíntotas.
    plt.ylim(-15, 15)

    # Adiciona rótulos e título.
    plt.title('Gráfico da função $f(x) = |\\tan(x)| + 2x$')
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')

    # Adiciona a grade para melhor visualização.
    plt.grid(True)

    # Adiciona a legenda.
    plt.legend()

    # Mostra o gráfico.
    plt.show()

# Chama a função para gerar o gráfico.
plot_tan_abs_plus_2x()