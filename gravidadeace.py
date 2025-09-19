import numpy as np
import matplotlib.pyplot as plt

# Definindo constantes
G = 6.67430e-11  # Constante gravitacional universal em m^3 kg^-1 s^-2
M = 5.972e24     # Massa da Terra em kg
R = 6.371e6      # Raio médio da Terra em m

# Criando um array de distâncias do centro da Terra (em metros)
# A faixa vai de 0 (centro) a 3 * R (três vezes o raio da Terra)
distancia = np.linspace(0, 3 * R, 1000)

# Criando um array para a aceleração da gravidade
aceleracao_gravidade = np.zeros_like(distancia)

# Loop para calcular a aceleração da gravidade
for i, r in enumerate(distancia):
    if r < R:
        # Aceleração da gravidade dentro da Terra
        # A gravidade aumenta linearmente com a distância do centro
        aceleracao_gravidade[i] = (G * M * r) / (R**3)
    else:
        # Aceleração da gravidade fora da Terra
        # A gravidade diminui com o inverso do quadrado da distância
        aceleracao_gravidade[i] = (G * M) / (r**2)