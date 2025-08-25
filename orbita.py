import matplotlib.pyplot as plt
import numpy as np

# A classe Círculo representa um círculo com centro (x, y) e raio r.
class Circulo:
    def __init__(self, x, y, r, cor='blue'):
        self.x = x
        self.y = y
        self.r = r
        self.cor = cor

    def desenhar(self, ax):
        """
        Desenha o círculo no plano 2D.
        ax: objeto Axes do matplotlib.
        """
        circulo = plt.Circle((self.x, self.y), self.r, color=self.cor)
        ax.add_artist(circulo)

# --- Criando os objetos ---
# Criando uma figura e um conjunto de eixos.
fig, ax = plt.subplots()

# Criando dois objetos do tipo Circulo com diferentes posições e raios.
circulo1 = Circulo(x=2, y=3, r=1.5, cor='red')
circulo2 = Circulo(x=7, y=5, r=2, cor='green')

# --- Desenhando os círculos ---
circulo1.desenhar(ax)
circulo2.desenhar(ax)

# --- Configurando o plano 2D ---
# Ajustando os limites do eixo para que os círculos sejam visíveis.
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Adicionando uma grade para melhor visualização.
ax.grid(True)

# Adicionando rótulos aos eixos.
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')

# Adicionando um título ao gráfico.
ax.set_title('Exemplo de Objetos Redondos em um Plano 2D')

# Mantendo a proporção dos eixos para que os círculos não fiquem distorcidos.
ax.set_aspect('equal', adjustable='box')

# Exibindo o gráfico.
plt.show()