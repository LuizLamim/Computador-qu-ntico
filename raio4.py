import numpy as np
import matplotlib.pyplot as plt

def plot_circle(radius):
    """
    Plota um círculo dado o seu raio.
    """
    theta = np.linspace(0, 2*np.pi, 100) # Gera 100 pontos de 0 a 2*pi (um círculo completo)
    x = radius * np.cos(theta)         # Calcula as coordenadas x
    y = radius * np.sin(theta)         # Calcula as coordenadas y

    plt.figure(figsize=(6, 6)) # Define o tamanho da figura para que o círculo não fique achatado
    plt.plot(x, y, color='blue')
    plt.title(f'Gráfico da Função x² + y² = {radius**2}')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True)                 # Adiciona uma grade ao gráfico
    plt.axhline(0, color='black',linewidth=0.5) # Eixo X em preto
    plt.axvline(0, color='black',linewidth=0.5) # Eixo Y em preto
    plt.gca().set_aspect('equal', adjustable='box') # Garante que os eixos tenham a mesma escala
    plt.show()

# Define o raio do círculo
raio = 4

# Chama a função para plotar o círculo
plot_circle(raio)