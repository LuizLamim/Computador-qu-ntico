import numpy as np
import matplotlib.pyplot as plt

def plot_tan_abs_plus_one():
    """
    Plota a função f(x) = |tan(x)| + 1 no intervalo de -2pi a 2pi.
    """
    # Cria um array de valores x no intervalo de -2pi a 2pi.
    # Usamos 1000 pontos para garantir uma curva suave.
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    # Calcula os valores de y para a função f(x) = |tan(x)| + 1.
    # np.tan(x) calcula a tangente para cada valor de x.
    # np.abs() calcula o valor absoluto.
    y = np.abs(np.tan(x)) + 1

    # Cria a figura e os eixos do gráfico.
    plt.figure(figsize=(10, 6))

    # Plota a função.
    # 'b-' define a cor da linha como azul ('b') e o estilo como sólido ('-').
    plt.plot(x, y, 'b-', label=r'$f(x) = |\tan(x)| + 1$')

    # Configura os limites do eixo y.
    # Isso evita que o gráfico se estenda infinitamente devido às assíntotas.
    plt.ylim(0, 10)

    # Adiciona rótulos e título.
    plt.title('Gráfico da função $f(x) = |\\tan(x)| + 1$')
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')

    # Adiciona a grade para melhor visualização.
    plt.grid(True)

    # Adiciona a legenda.
    plt.legend()

    # Mostra o gráfico.
    plt.show()

# Chama a função para gerar o gráfico.
plot_tan_abs_plus_one()