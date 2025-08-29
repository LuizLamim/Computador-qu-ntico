import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse(a, b, excentricidade):
    """
    Plota uma elipse com base em seus semi-eixos e excentricidade.

    Args:
        a (float): O semi-eixo maior.
        b (float): O semi-eixo menor.
        excentricidade (float): A excentricidade da elipse (e).
    """

    # Cria uma matriz de ângulos de 0 a 2*pi
    theta = np.linspace(0, 2 * np.pi, 100)

    # Coordenadas da elipse usando as equações paramétricas
    x = a * np.cos(theta)
    y = b * np.sin(theta)

    # Cria a figura e o eixo do plot
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plota a elipse
    ax.plot(x, y, label=f'Excentricidade = {excentricidade:.2f}')

    # Adiciona a legenda
    ax.legend()

    # Define o título do gráfico
    ax.set_title(f'Gráfico de uma Elipse com Excentricidade Alta')

    # Define os rótulos dos eixos
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')

    # Define a proporção dos eixos para que a elipse não pareça distorcida
    ax.set_aspect('equal', adjustable='box')

    # Adiciona as linhas de grade
    ax.grid(True, linestyle='--')

    # Mostra o gráfico
    plt.show()

# --- Exemplo de uso ---
# Elipse com excentricidade alta (próxima de 1)
# O semi-eixo maior (a) é 5 e o semi-eixo menor (b) é 1.
# Calculamos a excentricidade (e) com a fórmula: e = sqrt(1 - (b^2/a^2))
a = 5.0
b = 1.0
excentricidade = np.sqrt(1 - (b**2 / a**2))

# Chama a função para plotar a elipse
plot_ellipse(a, b, excentricidade)