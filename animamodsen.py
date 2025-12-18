import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = np.linspace(0, 4 * np.pi, 500)

y_data = np.abs(np.sin(x_data))

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(0, 1.2)  # Um pouco acima de 1 para melhor visualização
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title(r'Animação da Função $y = |\sin(x)|$', fontsize=16)
ax.set_xlabel('x (radianos)')
ax.set_ylabel('y')

line, = ax.plot([], [], lw=2, color='blue', label=r'$|\sin(x)|$')
# Um ponto vermelho na "ponta" do desenho
point, = ax.plot([], [], 'ro') 

ax.legend(loc='upper right')

# 3. Função de Inicialização (estado inicial do gráfico)
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# 4. Função de Atualização (chamada a cada frame)
def update(frame):
    # Pega os dados do início até o frame atual
    x_current = x_data[:frame]
    y_current = y_data[:frame]
    
    # Atualiza a linha com o histórico
    line.set_data(x_current, y_current)
    
    # Atualiza o ponto para a posição atual (último elemento)
    if len(x_current) > 0:
        point.set_data([x_current[-1]], [y_current[-1]])
    
    return line, point

# 5. Criação da Animação
# frames: quantidade de passos (igual ao tamanho do array x)
# interval: tempo em milissegundos entre cada frame
anim = FuncAnimation(fig, update, frames=len(x_data), 
                     init_func=init, interval=10, blit=True)

# Exibe o gráfico
plt.show()