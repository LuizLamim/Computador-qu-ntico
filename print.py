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
