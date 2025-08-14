import matplotlib.pyplot as plt

# A função para plotar a tabuada da soma
def plotar_tabuada_soma(numero):
    """
    Esta função gera e plota um gráfico de barras da tabuada da soma
    de um número específico.
    
    Args:
        numero (int): O número para o qual a tabuada será gerada.
    """
    
    # Lista para armazenar os resultados da soma
    resultados = []
    
    # Loop para calcular a soma de 'numero' com os números de 0 a 10
    for i in range(11):
        resultados.append(numero + i)
        
    # Cria uma lista de rótulos para o eixo x (os números de 0 a 10)
    eixo_x = list(range(11))
    
    # Cria o gráfico de barras
    plt.figure(figsize=(10, 6)) # Define o tamanho da figura
    plt.bar(eixo_x, resultados, color='skyblue') # Cria as barras
    
    # Adiciona os títulos e rótulos do gráfico
    plt.title(f'Tabuada da Soma de {numero}', fontsize=16)
    plt.xlabel('Número a ser somado', fontsize=12)
    plt.ylabel('Resultado da soma', fontsize=12)
    
    # Define os rótulos do eixo x para mostrar os números de 0 a 10
    plt.xticks(eixo_x)
    
    # Adiciona os resultados diretamente em cima de cada barra para clareza
    for i, resultado in enumerate(resultados):
        plt.text(i, resultado + 0.2, str(resultado), ha='center', va='bottom', fontsize=10)
        
    # Adiciona uma grade ao plano de fundo para facilitar a leitura
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Exibe o gráfico
    plt.show()

# Chama a função para plotar a tabuada da soma de 5
plotar_tabuada_soma(5)