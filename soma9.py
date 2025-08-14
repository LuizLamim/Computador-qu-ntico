import matplotlib.pyplot as plt

def plotar_tabuada_soma(numero):
    """
    Gera e plota um gráfico de barras da tabuada da soma de um número.

    Args:
        numero (int): O número para o qual a tabuada será gerada.
    """
    
    # Cria uma lista para armazenar os resultados da soma
    resultados = []
    
    # Adiciona os resultados da soma do número com os valores de 0 a 10
    for i in range(11):
        resultados.append(numero + i)
        
    # Cria os rótulos do eixo X (números de 0 a 10)
    eixo_x = list(range(11))
    
    # Cria a figura e o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(eixo_x, resultados, color='skyblue')
    
    # Adiciona os títulos e rótulos
    plt.title(f'Tabuada da Soma de {numero}', fontsize=16)
    plt.xlabel('Número a ser somado', fontsize=12)
    plt.ylabel('Resultado da soma', fontsize=12)
    
    # Define os rótulos do eixo X para os números de 0 a 10
    plt.xticks(eixo_x)
    
    # Adiciona os valores da soma em cima de cada barra
    for i, resultado in enumerate(resultados):
        plt.text(i, resultado + 0.2, str(resultado), ha='center', va='bottom', fontsize=10)
        
    # Adiciona uma grade horizontal para facilitar a leitura
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Exibe o gráfico
    plt.show()

# Chama a função para plotar a tabuada da soma de 9
plotar_tabuada_soma(9)