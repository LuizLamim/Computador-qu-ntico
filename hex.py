import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# --- Configurações da Animação ---
# Figura e eixo para a plotagem
fig, ax = plt.subplots()

# Remove a borda e os eixos
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

# Define os limites do eixo para manter o hexágono visível
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# --- Geração do Hexágono ---
# Define o número de lados (6 para um hexágono)
n_lados = 6

# Gera os ângulos para os vértices do hexágono
# np.linspace cria 6 pontos entre 0 e 2*pi
angulos = np.linspace(0, 2 * np.pi, n_lados, endpoint=False)

# Calcula as coordenadas x e y dos vértices
# cos(ângulo) para o eixo x e sen(ângulo) para o eixo y
x_base = np.cos(angulos)
y_base = np.sin(angulos)

# Cria o objeto de linha para o hexágono
# plt.plot retorna um objeto de lista, pegamos o primeiro elemento
linha_hex, = ax.plot(x_base, y_base, 'b-', lw=3)

# --- Função de Animação ---
# Esta função será chamada para cada quadro da animação
def animar(i):
    # A variável 'i' é o número do quadro
    
    # Calcula o ângulo de rotação para este quadro
    # (i * 1) cria uma rotação de 1 grau por quadro
    angulo_rotacao = np.deg2rad(i * 1)
    
    # Cria a matriz de rotação
    matriz_rotacao = np.array([[np.cos(angulo_rotacao), -np.sin(angulo_rotacao)],
                               [np.sin(angulo_rotacao), np.cos(angulo_rotacao)]])
    
    # Combina as coordenadas base x e y em uma matriz 2xN
    coords_base = np.vstack([x_base, y_base])
    
    # Aplica a rotação: multiplica a matriz de rotação pelas coordenadas base
    coords_rotacionadas = matriz_rotacao @ coords_base
    
    # Atualiza os dados da linha com as novas coordenadas rotacionadas
    linha_hex.set_data(coords_rotacionadas[0], coords_rotacionadas[1])
    
    # Retorna o objeto atualizado
    return linha_hex,

# --- Criação da Animação ---
# A função FuncAnimation é a que orquestra tudo
ani = animation.FuncAnimation(fig,                 # Figura que a animação será exibida
                              animar,              # Função que será chamada para cada quadro
                              frames=360,          # Número total de quadros (360 para uma volta completa)
                              interval=20,         # Intervalo de tempo entre os quadros em ms (20ms)
                              blit=True)           # Otimização para desenhar apenas o que muda

# Salva a animação como um arquivo GIF
# Você pode remover esta linha se quiser apenas exibir a animação
ani.save('hexagono_girando.gif', writer='pillow', fps=50)

# Exibe a animação na tela
plt.show()