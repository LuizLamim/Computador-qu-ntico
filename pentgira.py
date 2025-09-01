import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Função para calcular as coordenadas dos vértices de um pentágono regular
def calcular_pentagono(centro_x, centro_y, raio, angulo_rotacao):
    """
    Calcula os vértices de um pentágono regular.
    
    Args:
        centro_x (float): Coordenada X do centro.
        centro_y (float): Coordenada Y do centro.
        raio (float): Raio do círculo circunscrito ao pentágono.
        angulo_rotacao (float): Ângulo de rotação em graus.
        
    Returns:
        tuple: Tupla com duas listas, uma para as coordenadas X e outra para as Y dos vértices.
    """
    # A base do pentágono é construída em um círculo
    # O ângulo entre os vértices é 2*pi/5
    angulos_rad = np.linspace(0, 2 * np.pi, 6) + np.deg2rad(angulo_rotacao)
    
    # Adiciona o primeiro ponto no final para fechar a figura
    angulos_rad = np.append(angulos_rad, angulos_rad[0])
    
    # Calcula as coordenadas X e Y
    x = centro_x + raio * np.cos(angulos_rad)
    y = centro_y + raio * np.sin(angulos_rad)
    
    return x, y

# Configuração da figura e dos eixos
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Garante que os eixos tenham a mesma escala
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Desabilita os eixos para uma visualização mais limpa
ax.axis('off')

# Cria um objeto de linha para o pentágono. Inicialmente ele é vazio.
linha, = ax.plot([], [], lw=2, color='r')

# Função de inicialização para a animação
def init():
    linha.set_data([], [])
    return linha,

# Função que será chamada a cada frame da animação
def animar(i):
    """
    Função de animação que atualiza os dados do pentágono para cada quadro.
    
    Args:
        i (int): O número do frame (passado automaticamente pela Animação).
    """
    # O ângulo de rotação é baseado no número do frame
    angulo_rotacao = i * 2.0
    
    # Calcula os novos vértices do pentágono
    x_pentagono, y_pentagono = calcular_pentagono(0, 0, 1.5, angulo_rotacao)
    
    # Atualiza os dados da linha para o novo pentágono
    linha.set_data(x_pentagono, y_pentagono)
    
    return linha,

# Cria a animação
ani = animation.FuncAnimation(
    fig, 
    animar, 
    frames=180, 
    init_func=init, 
    interval=20, 
    blit=True
)

# Salvar a animação como um arquivo de vídeo (opcional)
# Certifique-se de ter um "writer" instalado, como 'ffmpeg'.
# Exemplo: `pip install ffmpeg-python`
# ani.save('pentagono_girando.mp4', writer='ffmpeg', fps=30)

# Exibe a animação
plt.show()