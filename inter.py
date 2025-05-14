import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation

# 1. Definir a função e o intervalo
def func(x):
  """A função a ser integrada."""
  return np.sin(x) + 1 # Exemplo: sin(x) + 1 para manter a área positiva em um intervalo

a = 0  # Limite inferior
b = 2 * np.pi # Limite superior
x_vals = np.linspace(a, b, 200)
y_vals = func(x_vals)

# 2. Configurar a figura e os eixos
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Aproximação de Área por Somas de Riemann')
ax.grid(True)
ax.set_ylim(0, max(y_vals) + 0.5) # Ajusta o limite Y para melhor visualização

# Plotar a função
line, = ax.plot(x_vals, y_vals, color='blue', label=f'f(x) = sin(x) + 1')

# Lista para armazenar os retângulos (para a animação)
rects = []

# 3. Função para atualizar a animação (desenhar retângulos)
def update(frame):
    """Atualiza os retângulos para cada frame da animação."""
    # Limpa os retângulos do frame anterior
    for rect in rects:
        rect.remove()
    rects[:] = [] # Esvazia a lista

    num_rectangles = frame + 5 # Começa com 5 retângulos e aumenta em 1 a cada frame
    if num_rectangles > 100: # Limita o número máximo de retângulos
        num_rectangles = 100

    delta_x = (b - a) / num_rectangles
    x_i = np.linspace(a, b, num_rectangles + 1)[:-1] # Pontos da esquerda para a soma de Riemann

    for i in range(num_rectangles):
        height = func(x_i[i])
        # Cria o retângulo: (posição_inicial_x, posição_inicial_y), largura, altura
        rect = patches.Rectangle((x_i[i], 0), delta_x, height, linewidth=1, edgecolor='red', facecolor='orange', alpha=0.5)
        ax.add_patch(rect)
        rects.append(rect)

    # Atualizar o título para mostrar o número de retângulos
    ax.set_title(f'Aproximação de Área com {num_rectangles} Retângulos')

    return rects

# 4. Criar a animação
# O número de frames determina quantas vezes a função 'update' será chamada
num_frames = 50 # Número de passos na animação (quantidade de retângulos aumentará até 5 + 50 = 55)
ani = FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=False)

# Adicionar legenda
ax.legend()

# 5. Mostrar a animação
plt.show()