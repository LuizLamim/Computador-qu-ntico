import numpy as np
import matplotlib.pyplot as plt

def crescimento_bacteriano(N0, taxa_crescimento, tempo_total, intervalo):
    """
    Gera e plota o gráfico de crescimento bacteriano.
    
    Parâmetros:
    N0: População inicial de bactérias
    taxa_crescimento: Taxa de crescimento (por unidade de tempo)
    tempo_total: Tempo total de simulação
    intervalo: Intervalo de tempo entre os pontos de medição
    """
    tempos = np.arange(0, tempo_total + intervalo, intervalo)
    populacoes = N0 * np.exp(taxa_crescimento * tempos)

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(tempos, populacoes, label='Crescimento Bacteriano', color='red')
    plt.title('Crescimento Bacteriano Exponencial')
    plt.xlabel('Tempo')
    plt.ylabel('Número de Bactérias')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Exemplo de uso
N0 = 100            # População inicial
r = 0.4             # Taxa de crescimento
tempo_total = 24    # Tempo total (ex: horas)
intervalo = 1       # Intervalo de tempo (ex: 1 hora)

crescimento_bacteriano(N0, r, tempo_total, intervalo)
