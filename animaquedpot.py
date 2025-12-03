import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t_max = 10.0
dt = 0.05
t = np.arange(0, t_max, dt)

P0 = 100.0   # Potência Inicial (ex: 100 Watts ou %)
k = 0.5

potencia = P0 * np.exp(-k * t)

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, t_max)
ax.set_ylim(0, P0 + 10)

ax.set_title("Simulação de Queda de Potência (Decaimento Exponencial)")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Potência (W)")
ax.grid(True, linestyle='--', alpha=0.6)

# Elementos que serão animados
# A linha do gráfico (começa vazia)
line, = ax.plot([], [], lw=2, color='blue', label='P(t)')
# Um ponto vermelho para indicar o valor atual
point, = ax.plot([], [], 'ro') 
# Texto mostrando o valor atual
text_value = ax.text(0.7, 0.8, '', transform=ax.transAxes, 
                     bbox=dict(facecolor='white', alpha=0.5))

ax.legend()

# --- 3. Funções de Animação ---

def init():
    """Inicializa o fundo da animação (quadro vazio)."""
    line.set_data([], [])
    point.set_data([], [])
    text_value.set_text('')
    return line, point, text_value

def update(frame):
    """Atualiza o gráfico a cada frame."""
    # frame é o índice atual do array de tempo
    x_data = t[:frame]
    y_data = potencia[:frame]
    
    # Atualiza a linha com todo o histórico até agora
    line.set_data(x_data, y_data)
    
    # Atualiza o ponto apenas na posição atual
    if len(x_data) > 0:
        point.set_data([t[frame-1]], [potencia[frame-1]])
        text_value.set_text(f'Potência: {potencia[frame-1]:.2f} W')
    
    return line, point, text_value

ani = FuncAnimation(fig, update, frames=len(t), 
                    init_func=init, blit=True, interval=30, repeat=False)



[Image of exponential decay graph]


plt.show()