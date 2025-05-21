import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Definir a função e sua derivada
def f(x):
    """A função que queremos plotar."""
    return x**2

def f_prime(x):
    """A derivada da função f(x)."""
    return 2*x

# 2. Configurar a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_title('Animação da Reta Tangente', fontsize=16)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 9)
ax.grid(True)
ax.set_aspect('equal', adjustable='box') # Garante que os eixos tenham a mesma escala

# Gerar pontos para a função
x_vals = np.linspace(-3, 3, 400)
y_vals = f(x_vals)

# Plotar a função
line_function, = ax.plot(x_vals, y_vals, label='$f(x) = x^2$', color='blue', linewidth=2)

# Inicializar o ponto e a reta tangente
point, = ax.plot([], [], 'ro', markersize=8, label='Ponto na Curva')
tangent_line, = ax.plot([], [], 'r--', label='Reta Tangente', linewidth=2)

# Adicionar legendas
ax.legend(loc='upper left', fontsize=10)

# 3. Função de inicialização para a animação
def init():
    point.set_data([], [])
    tangent_line.set_data([], [])
    return point, tangent_line

# 4. Função de atualização para cada quadro da animação
def update(frame):
    # Escolher um ponto x para o quadro atual
    x_current = x_vals[frame]
    y_current = f(x_current)

    # Coordenadas do ponto
    point.set_data(x_current, y_current)

    # Calcular a inclinação da reta tangente (derivada no ponto)
    slope = f_prime(x_current)

    # Calcular a equação da reta tangente: y - y1 = m(x - x1)
    # y = m*x - m*x1 + y1
    # Para plotar a reta, precisamos de dois pontos.
    # Vamos usar um pequeno intervalo ao redor de x_current
    tangent_x = np.array([x_current - 1, x_current + 1]) # Intervalo para a reta tangente
    tangent_y = slope * (tangent_x - x_current) + y_current

    tangent_line.set_data(tangent_x, tangent_y)

    return point, tangent_line

# 5. Criar a animação
# `frames` define o número de quadros. Usamos o número de pontos em x_vals.
# `interval` é o atraso entre os quadros em milissegundos.
# `blit=True` otimiza o desenho (apenas redesenha o que mudou).
ani = FuncAnimation(fig, update, frames=len(x_vals),
                    init_func=init, blit=True, interval=20)

# 6. Exibir a animação
plt.show()
