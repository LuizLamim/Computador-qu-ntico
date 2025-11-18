import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Dados para o crescimento exponencial
x = np.linspace(0, 5, 100) # De 0 a 5 com 100 pontos
y = np.exp(x) # Crescimento exponencial (e^x)

# Configurar a figura e o eixo
fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(0, 150) # Ajuste o limite Y conforme a sua função exponencial
ax.set_title("Crescimento Exponencial")
ax.set_xlabel("Tempo")
ax.set_ylabel("Valor")
line, = ax.plot([], [], 'r-') # Linha vermelha para a animação

# Função de inicialização: plotar um fundo vazio
def init():
    line.set_data([], [])
    return line,

# Função de animação: atualizar os dados
def animate(i):
    # 'i' representa o índice do frame, controlando quantos pontos mostrar
    line.set_data(x[:i], y[:i])
    return line,