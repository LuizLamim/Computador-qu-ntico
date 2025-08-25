import matplotlib.pyplot as plt
import numpy as np

# A classe Circulo representa um círculo com centro (x, y) e raio r.
class Circulo:
    def __init__(self, x, y, r, cor='blue'):
        self.x = np.array([x, y], dtype=float)
        self.r = r
        self.cor = cor

    def desenhar(self, ax):
        """
        Desenha o círculo no plano 2D.
        ax: objeto Axes do matplotlib.
        """
        circulo = plt.Circle(self.x, self.r, color=self.cor)
        ax.add_artist(circulo)

# --- Parâmetros da simulação ---
G = 6.67430e-11  # Constante de gravitação universal
m1 = 1.0e12      # Massa do círculo vermelho (maior)
m2 = 1.0e5       # Massa do círculo verde (menor)
dt = 0.1         # Passo de tempo da simulação

# --- Criando os objetos ---
# Círculo 1 (maior, central)
circulo1 = Circulo(x=5, y=5, r=1.3, cor='blue')

# Círculo 2 (menor, em órbita)
circulo2 = Circulo(x=5, y=7, r=0.5, cor='green')

# A velocidade inicial é crucial para a órbita.
# Ela deve ser perpendicular ao vetor de posição inicial para uma órbita circular.
# A magnitude é calculada para equilibrar a força centrípeta com a gravitacional.
distancia_inicial = np.linalg.norm(circulo1.x - circulo2.x)
velocidade_orbita = np.sqrt(G * m1 / distancia_inicial)
circulo2_velocidade = np.array([-velocidade_orbita, 0])

# --- Configurando o gráfico para a animação ---
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.grid(True)
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_title('Órbita do Objeto Menor')
ax.set_aspect('equal', adjustable='box')

# Desenha os círculos iniciais.
circulo1.desenhar(ax)
circulo2_patch = plt.Circle(circulo2.x, circulo2.r, color=circulo2.cor)
ax.add_artist(circulo2_patch)

# --- Loop de animação ---
for i in range(500):
    plt.pause(0.01)  # Pausa para visualização da animação

    # Vetor de distância entre os círculos
    r_vetor = circulo1.x - circulo2.x
    distancia = np.linalg.norm(r_vetor)

    # Força gravitacional (F = G * m1 * m2 / r^2)
    forca_gravitacional_modulo = G * m1 * m2 / (distancia**2)

    # Força gravitacional como vetor
    forca_gravitacional_vetor = forca_gravitacional_modulo * (r_vetor / distancia)

    # Aceleração do círculo 2 (a = F / m)
    aceleracao = forca_gravitacional_vetor / m2

    # Atualiza a velocidade e a posição do círculo 2
    circulo2_velocidade += aceleracao * dt
    circulo2.x += circulo2_velocidade * dt

    circulo2_patch.set_center(circulo2.x)

plt.show()