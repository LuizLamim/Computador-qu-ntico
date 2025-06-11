import numpy as np
import matplotlib.pyplot as plt

def plot_log_equation():
    """
    Plota a equação y = log(x) (logaritmo natural).
    """
    # 1. Gerar valores para x
    # O logaritmo natural é definido apenas para x > 0.
    # Usaremos um intervalo que exclui o zero para evitar erros.
    # np.linspace cria um array de números igualmente espaçados em um intervalo.
    # Escolhemos um grande número de pontos para uma curva suave.
    x = np.linspace(0.1, 10, 500) # Começa em 0.1 para evitar log(0) e vai até 10

    # 2. Calcular os valores correspondentes de y
    # np.log() calcula o logaritmo natural (base e) para cada elemento em x.
    y = np.log(x)

    # 3. Criar o gráfico
    plt.figure(figsize=(10, 6)) # Define o tamanho da figura para melhor visualização
    plt.plot(x, y, label='$y = \log(x)$', color='blue') # Plota a linha, adiciona um label e cor

    # 4. Adicionar rótulos, título e grade
    plt.title('Gráfico da Equação $y = \log(x)$', fontsize=16)
    plt.xlabel('$x$', fontsize=14)
    plt.ylabel('$y$', fontsize=14)
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8) # Linha horizontal em y=0
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.8) # Linha vertical em x=0
    plt.grid(True, linestyle=':', alpha=0.7) # Adiciona uma grade ao gráfico
    plt.legend(fontsize=12) # Mostra a legenda com o label da equação

    # 5. Exibir o gráfico
    plt.show()

# Chamar a função para gerar o gráfico
if __name__ == "__main__":
    plot_log_equation()