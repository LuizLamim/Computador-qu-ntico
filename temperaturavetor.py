import numpy as np
import matplotlib.pyplot as plt

def plotar_gradiente_temperatura():
    """
    Este programa plota o mapa de calor de uma função de temperatura bidimensional
    e o seu campo de gradiente usando setas vermelhas.
    """
    
    # 1. Definir o domínio e a função de temperatura
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    
    # A função de temperatura (exemplo: uma superfície gaussiana)
    Z = np.exp(-(X**2 + Y**2) / 2)
    
    # 2. Calcular o gradiente
    # O gradiente é um vetor que aponta na direção de maior crescimento da função.
    # np.gradient retorna as derivadas parciais.
    dZ_dx, dZ_dy = np.gradient(Z, x[1] - x[0], y[1] - y[0])
    
    # 3. Criar a visualização
    plt.figure(figsize=(11, 9))
    
    # Plotar o mapa de calor (superfície de temperatura)
    plt.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', cmap='plasma')
    plt.colorbar(label='Temperatura')
    
    # Plotar o campo do vetor gradiente com setas vermelhas
    # Usamos o 'slice' [::3, ::3] para reduzir a quantidade de setas e
    # não sobrecarregar o gráfico, facilitando a visualização.
    plt.quiver(X[::3, ::3], Y[::3, ::3], dZ_dx[::3, ::3], dZ_dy[::3, ::3], color='red', scale=20, label='Vetor Gradiente')

    # 4. Adicionar rótulos e título
    plt.title('Mapa de Calor e Vetor Gradiente de Temperatura')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    plt.grid(False)
    
    # 5. Exibir o gráfico
    plt.show()

# Chamar a função para executar o programa
if __name__ == "__main__":
    plotar_gradiente_temperatura()