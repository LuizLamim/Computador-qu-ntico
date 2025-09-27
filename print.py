import matplotlib.pyplot as plt

def plotar_primeiras_letras():
    # As 5 primeiras letras do alfabeto
    letras = ['A', 'B', 'C', 'D', 'E']

    # Posições no eixo X (1, 2, 3, 4, 5)
    x_pos = list(range(1, len(letras) + 1))

    # Posições no eixo Y (todas no mesmo nível, por exemplo, 1)
    y_pos = [1] * len(letras)

    # Cria a figura e os eixos
    fig, ax = plt.subplots()

    # Itera sobre as letras para plotar cada uma como um texto no gráfico
    for i, letra in enumerate(letras):
        # ax.text(x, y, texto, ...)
        ax.text(x_pos[i], y_pos[i], letra,
                fontsize=20,  # Define o tamanho da fonte
                ha='center',  # Alinhamento horizontal: centralizado
                va='center')  # Alinhamento vertical: centralizado

# Configura o gráfico

    # Remove os "ticks" e os rótulos dos eixos para um visual mais limpo
    ax.set_xticks([])
    ax.set_yticks([])

    # Define os limites dos eixos para que as letras fiquem bem centralizadas
    # Adiciona um pouco de margem em torno das letras
    ax.set_xlim(0.5, len(letras) + 0.5)
    ax.set_ylim(0.5, 1.5)

    # Título do gráfico
    ax.set_title('As 5 Primeiras Letras do Alfabeto')

    # Remove as bordas do gráfico (as "spines")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Mostra o gráfico
    plt.show()