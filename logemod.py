import numpy as np
import matplotlib.pyplot as plt

def plot_log_abs():
    """
    Plota o gráfico da função f(x) = |log(x)| para x > 0.
    """
    # Cria um array de valores para x.
    # Usamos np.linspace para ter uma distribuição uniforme de pontos.
    # Excluímos o zero, pois log(0) não é definido.
    x = np.linspace(0.01, 10, 400)

    # Calcula o valor da função para cada x.
    # np.log() calcula o logaritmo natural.
    y = np.abs(np.log(x))

    # Cria a figura e os eixos do gráfico.
    plt.figure(figsize=(10, 6))

    # Plota a função.
    plt.plot(x, y, label=r'$f(x) = |\log(x)|$', color='blue')

    # Adiciona título e rótulos aos eixos.
    plt.title('Gráfico da função $f(x) = |\\log(x)|$', fontsize=16)
    plt.xlabel('Eixo x', fontsize=12)
    plt.ylabel('Eixo y', fontsize=12)

    # Adiciona a grade para facilitar a leitura.
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Adiciona uma legenda para identificar a função.
    plt.legend()

    # Adiciona os eixos x e y em 0.
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Mostra o gráfico.
    plt.show()

# Chama a função para gerar o gráfico.
if __name__ == '__main__':
    plot_log_abs()