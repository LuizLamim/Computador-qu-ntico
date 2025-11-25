import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Configurações da Simulação ---
N_PARTICULAS = 150       # Número de partículas
TAM_CAIXA = 10.0         # Tamanho do recipiente (quadrado)
DT = 0.05                # Passo de tempo da simulação
FRAMES = 300             # Total de quadros da animação
TAXA_AUMENTO_VEL = 1.005 # Fator de multiplicação da velocidade por quadro (aumenta a "temperatura")
FRAME_PARADA_AUMENTO = 200 # Quadro em que a pressão para de subir para não ficar caótico demais

# --- Inicialização do Estado ---
# Posições iniciais aleatórias dentro da caixa (X e Y)
pos = np.random.rand(N_PARTICULAS, 2) * TAM_CAIXA

# Velocidades iniciais aleatórias (distribuição normal centrada em 0)
# Começamos com velocidades baixas para representar baixa pressão inicial
vel = np.random.randn(N_PARTICULAS, 2) * 0.5

# --- Configuração do Matplotlib ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, TAM_CAIXA)
ax.set_ylim(0, TAM_CAIXA)

# Remove os eixos para focar na "caixa"
ax.set_xticks([])
ax.set_yticks([])