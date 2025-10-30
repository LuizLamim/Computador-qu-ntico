import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Parâmetros da Simulação ---
NUM_PARTICULAS = 50
GRAVIDADE = np.array([0, -0.05])  # Força da gravidade (em y negativo)
FATOR_AMORTECIMENTO = 0.95        # Fator de perda de velocidade (viscosidade/ar)
FATOR_COLISAO_PAREDE = 0.8        # Fator de 'salto' ao colidir com a parede
TEMPO_PASSO = 0.1                 # Delta de tempo para a integração
LIMITE_X = (0, 10)                # Limites da área de simulação (x)
LIMITE_Y = (0, 10)                # Limites da área de simulação (y)
TAMANHO_PARTICULA = 0.1           # Tamanho (raio) da partícula para colisões