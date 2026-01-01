import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# --- Configurações Físicas ---
GRAVITY = -9.8  # m/s^2
DT = 0.05       # Passo de tempo (delta t)
BOUNCE_FACTOR = 0.6  # Quanto de energia é conservada ao quicar
SPLIT_FORCE = 2.0    # Força horizontal da separação

class Cube:
    def __init__(self, x, y, z, size, color, is_fragment=False):
        self.pos = np.array([x, y, z], dtype=float)
        self.vel = np.array([0.0, 0.0, 0.0], dtype=float)
        self.size = size
        self.color = color
        self.is_fragment = is_fragment
        self.active = True

        def update(self):
        # Aplicar gravidade (apenas no eixo Z)
        self.vel[2] += GRAVITY * DT
        
        # Atualizar posição
        self.pos += self.vel * DT

        # Checar colisão com o chão (z=0)
        if self.pos[2] <= 0:
            self.pos[2] = 0
            # Se for fragmento, ele quica. Se for o cubo principal, ele divide.
            if self.is_fragment:
                self.vel[2] *= -BOUNCE_FACTOR # Inverte velocidade e perde energia
                # Atrito simples para parar de deslizar eventualmente
                self.vel[0] *= 0.95
                self.vel[1] *= 0.95
            else:
                return "SPLIT"
        return "OK"

    def get_draw_data(self):
        # Lógica para desenhar um cubo 3D (wireframe)
        r = self.size / 2
        # Definir os 8 vértices relativos ao centro
        corners = np.array([
            [-r, -r, -r], [r, -r, -r], [r, r, -r], [-r, r, -r],
            [-r, -r, r], [r, -r, r], [r, r, r], [-r, r, r]
        ])
        # Transladar para a posição atual
        corners += self.pos
        return corners

# --- Configuração da Cena ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Altura (Z)')
ax.set_title('Simulação: Cubo Caindo e Dividindo')

# Lista de objetos na cena
cubes = [Cube(x=0, y=0, z=9, size=2.0, color='blue')]

def draw_cube(ax, cube):
    corners = cube.get_draw_data()
    # Ordem de conexão dos vértices para formar as arestas do cubo
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0], # Base inferior
        [4, 5], [5, 6], [6, 7], [7, 4], # Base superior
        [0, 4], [1, 5], [2, 6], [3, 7]  # Colunas verticais
    ]
    for edge in edges:
        p1, p2 = corners[edge[0]], corners[edge[1]]
        ax.plot3D([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color=cube.color)

def update_scene(frame):
    global cubes
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(0, 10)
    
    new_cubes = []
    
    for cube in cubes:
        status = cube.update()
        
        if status == "SPLIT":
            # Lógica de Divisão: Cria 4 cubos menores
            offsets = [
                (1, 1), (1, -1), (-1, 1), (-1, -1)
            ]
            
            for ox, oy in offsets:
                # Posição ligeiramente deslocada do centro
                new_c = Cube(
                    x=cube.pos[0] + ox*0.5, 
                    y=cube.pos[1] + oy*0.5, 
                    z=0.5, # Começa um pouco acima do chão
                    size=cube.size / 2, 
                    color='red', 
                    is_fragment=True
                )
                # Adiciona velocidade de explosão para fora + um pouco para cima
                new_c.vel = np.array([ox * SPLIT_FORCE, oy * SPLIT_FORCE, 3.0])
                new_cubes.append(new_c)
        else:
            new_cubes.append(cube)
            draw_cube(ax, cube)
            
    cubes = new_cubes