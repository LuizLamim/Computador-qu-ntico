import numpy as np
import matplotlib.pyplot as plt

def plot_gradient_vector():
    """
    Plota o gráfico de um vetor gradiente para uma função 2D de exemplo.
    A função de exemplo é f(x, y) = x^2 + y^2 (um paraboloide).
    """

    # 1. Definir a função 2D de exemplo
    # Vamos usar f(x, y) = x^2 + y^2
    def f(x, y):
        return x**2 + y**2

    # 2. Calcular as derivadas parciais (o gradiente)
    # A derivada parcial de f em relação a x é df/dx = 2x
    # A derivada parcial de f em relação a y é df/dy = 2y
    def df_dx(x, y):
        return 2 * x

    def df_dy(x, y):
        return 2 * y

    # 3. Criar uma grade de pontos (domínio para a plotagem)
    x = np.linspace(-5, 5, 20)  # 20 pontos de -5 a 5 para x
    y = np.linspace(-5, 5, 20)  # 20 pontos de -5 a 5 para y
    X, Y = np.meshgrid(x, y)    # Cria a grade 2D

    # 4. Calcular os valores da função e do gradiente em cada ponto da grade
    Z = f(X, Y)
    U = df_dx(X, Y) # Componente x do vetor gradiente
    V = df_dy(X, Y) # Componente y do vetor gradiente

    # 5. Plotar o gráfico
    plt.figure(figsize=(10, 8))

    # Desenhar os contornos da função (mapa de nível)
    # Isso nos ajuda a visualizar a "superfície" da função
    plt.contour(X, Y, Z, levels=20, cmap='viridis', alpha=0.7)
    plt.colorbar(label='Valor da Função $f(x, y)$')

    # Plotar os vetores gradientes
    # O 'quiver' é usado para plotar campos de vetores.
    # 'scale' ajusta o comprimento das setas.
    plt.quiver(X, Y, U, V, color='red', scale=50, alpha=0.8,
               headwidth=5, headlength=7, headaxislength=6)

    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Vetor Gradiente de $f(x, y) = x^2 + y^2$')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box') # Garante que os eixos tenham a mesma escala
    plt.show()

# Chamada da função para plotar o gradiente
if __name__ == '__main__':
    plot_gradient_vector()