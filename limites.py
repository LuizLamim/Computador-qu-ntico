import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Definindo a função do limite
def f(x):
    return (x**2 - 1) / (x - 1)

# Gerando os dados para o gráfico da função
x_vals = np.linspace(0, 2, 200)
y_vals = f(x_vals)

# Configurando o gráfico
fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label='f(x) = (x^2 - 1) / (x - 1)', color='blue')
ax.axhline(y=2, color='red', linestyle='--', label='Limite (y=2)')
ax.axvline(x=1, color='green', linestyle='--', label='x se aproximando de 1')
ax.set_title('Conceito de Limites')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_ylim(0, 4)
ax.set_xlim(0, 2)
ax.grid(True)
ax.legend()
plt.tight_layout()

# Inicializando a animação com os pontos
point_left, = ax.plot([], [], 'o', color='purple', label='x < 1')
point_right, = ax.plot([], [], 'o', color='orange', label='x > 1')

# Função de inicialização da animação
def init():
    point_left.set_data([], [])
    point_right.set_data([], [])
    return point_left, point_right

# Função de atualização para cada frame
def update(frame):
    # Ponto vindo da esquerda (x < 1)
    x_left = 1 - 0.5 * np.exp(-frame / 50)
    y_left = f(x_left)
    point_left.set_data(x_left, y_left)
    
    # Ponto vindo da direita (x > 1)
    x_right = 1 + 0.5 * np.exp(-frame / 50)
    y_right = f(x_right)
    point_right.set_data(x_right, y_right)

    return point_left, point_right

# Criando e executando a animação
ani = FuncAnimation(fig, update, frames=np.arange(0, 90), init_func=init, blit=True)

# Salvando a animação como um arquivo GIF ou MP4 (opcional)
# Certifique-se de ter o ffmpeg ou ImageMagick instalado se quiser salvar como vídeo ou gif
# ani.save('limite_animacao.gif', writer='pillow', fps=20)
# ani.save('limite_animacao.mp4', writer='ffmpeg', fps=30)

# Exibindo o gráfico com a animação
plt.show()