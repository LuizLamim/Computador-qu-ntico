import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np

# 1. Parâmetros e Configurações
# Escolhemos valores inteiros simples para os catetos que formam uma terna pitagórica (3, 4, 5)
a = 3
b = 4
c = np.sqrt(a**2 + b**2) # Deve ser 5

# Configurações do plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-1, a + b + 2)
ax.set_ylim(-1, b + a + 2)
ax.axis('off') # Remove os eixos para um visual mais limpo

# Posições dos vértices do triângulo (começando na origem)
P1 = np.array([0, 0])
P2 = np.array([a, 0])
P3 = np.array([0, b])

# Cores para os quadrados
color_a = '#2ecc71'  # Verde Esmeralda
color_b = '#3498db'  # Azul Petra
color_c = '#e74c3c'  # Vermelho Alizarina

# 2. Funções de Desenho
def draw_triangle(ax, P1, P2, P3):
    """Desenha o triângulo retângulo e as etiquetas."""
    # Desenha o triângulo
    triangle_coords = np.array([P1, P2, P3, P1])
    line, = ax.plot(triangle_coords[:, 0], triangle_coords[:, 1], color='k', linewidth=2, zorder=3)
    
    # Marca o ângulo reto (pequeno quadrado)
    rect_angle = patches.Rectangle((0, 0), 0.3, 0.3, edgecolor='k', facecolor='none', linewidth=1, zorder=3)
    ax.add_patch(rect_angle)
    
    # Etiquetas dos lados (catetos e hipotenusa)
    label_a = ax.text(a/2, -0.5, '$a$', fontsize=18, ha='center', va='top', color='k', zorder=4)
    label_b = ax.text(-0.5, b/2, '$b$', fontsize=18, ha='right', va='center', color='k', zorder=4)
    
    # Ponto médio da hipotenusa para a etiqueta 'c'
    mid_c_x = (P2[0] + P3[0]) / 2
    mid_c_y = (P2[1] + P3[1]) / 2
    label_c = ax.text(mid_c_x + 0.3, mid_c_y - 0.2, '$c$', fontsize=18, ha='center', va='center', color='k', zorder=4, rotation=np.degrees(np.arctan2(b, a)))
    
    return [line, rect_angle, label_a, label_b, label_c]

def draw_square_a(ax, alpha=1.0):
    """Desenha o quadrado sobre o cateto 'a'."""
    # Vértices: (0, 0), (a, 0), (a, -a), (0, -a) -> deslocamos para evitar sobreposição
    square_a = patches.Rectangle((0, 0), a, a, edgecolor=color_a, facecolor=color_a, alpha=0.3*alpha, linewidth=3, zorder=1)
    ax.add_patch(square_a)
    area_label_a = ax.text(a/2, a/2, '$a^2$', fontsize=20, ha='center', va='center', color='k', zorder=2, alpha=alpha)
    return [square_a, area_label_a]

def draw_square_b(ax, alpha=1.0):
    """Desenha o quadrado sobre o cateto 'b'."""
    # Vértices: (0, 0), (0, b), (-b, b), (-b, 0)
    square_b = patches.Rectangle((0, 0), -b, b, edgecolor=color_b, facecolor=color_b, alpha=0.3*alpha, linewidth=3, zorder=1)
    ax.add_patch(square_b)
    area_label_b = ax.text(-b/2, b/2, '$b^2$', fontsize=20, ha='center', va='center', color='k', zorder=2, alpha=alpha)
    return [square_b, area_label_b]

def draw_square_c(ax, alpha=1.0):
    """Desenha o quadrado sobre a hipotenusa 'c'."""
    
    # 1. Encontrar o vetor na direção da hipotenusa
    vector_c = P3 - P2 # (-a, b)
    
    # 2. Encontrar o vetor perpendicular (rotação de 90 graus: (x, y) -> (-y, x))
    perp_vector = np.array([-vector_c[1], vector_c[0]]) # (-b, -a)
    
    # 3. Normalizar o vetor perpendicular para ter comprimento 'c'
    # Embora não seja estritamente necessário para o deslocamento, ajuda na visualização
    unit_perp_vector = perp_vector / np.linalg.norm(perp_vector)
    offset_vector = unit_perp_vector * c
    
    # 4. Vértices do quadrado (Começando em P2 e indo no sentido horário)
    # V1: P2 (a, 0)
    # V2: P3 (0, b)
    # V3: P3 + offset_vector (ou V2 + (P3 - P2) rotacionado 90 graus)
    # V4: P2 + offset_vector (ou V1 + (P3 - P2) rotacionado 90 graus)
    
    # Uma forma mais fácil de obter os 4 vértices (partindo de P2 e P3)
    # V2 = P3
    # V3 = P3 - perp_vector (pois perp_vector tem comprimento 'c')
    # V4 = P2 - perp_vector
    V1 = P2
    V2 = P3
    V3 = V2 - perp_vector
    V4 = V1 - perp_vector

    square_c_coords = np.array([V1, V2, V3, V4, V1])
    
    # Desenha o quadrado
    square_c = patches.Polygon(square_c_coords[:-1], edgecolor=color_c, facecolor=color_c, alpha=0.3*alpha, linewidth=3, zorder=1)
    ax.add_patch(square_c)
    
    # Ponto central para a etiqueta
    center_x = (V1[0] + V3[0]) / 2
    center_y = (V1[1] + V3[1]) / 2
    area_label_c = ax.text(center_x, center_y, '$c^2$', fontsize=20, ha='center', va='center', color='k', zorder=2, alpha=alpha)
    
    return [square_c, area_label_c]


# 3. Lógica da Animação (Init e Update)
# Número total de quadros (frames)
total_frames = 300
frames_per_stage = 60

def init():
    """Inicializa a animação (limpa o eixo)."""
    ax.clear()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1, a + b + 2)
    ax.set_ylim(-1, b + a + 2)
    ax.axis('off')
    return []

def update(frame):
    """Atualiza o quadro da animação com base no tempo."""
    ax.clear()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1, a + b + 2)
    ax.set_ylim(-1, b + a + 2)
    ax.axis('off')
    elements = []
    
    # --- Cena 1: Introdução ao Triângulo Retângulo (Frames 0 a 60) ---
    if frame < frames_per_stage:
        # Desenha o triângulo estaticamente
        elements.extend(draw_triangle(ax, P1, P2, P3))
        
        # Título da Cena
        ax.set_title('Cena 1: Introdução ao Triângulo Retângulo $a, b, c$', fontsize=16, pad=10)
        
    # --- Cena 2: Aparecimento dos Quadrados nos Catetos 'a' e 'b' (Frames 60 a 120) ---
    elif frame < 2 * frames_per_stage:
        f = frame - frames_per_stage
        
        # Mantém o triângulo estático
        elements.extend(draw_triangle(ax, P1, P2, P3))
        
        # Animação de fade-in (alpha crescente) dos quadrados
        alpha = min(1.0, f / frames_per_stage)
        
        # Quadrado a (Deslocamos temporariamente para a direita para evitar sobreposição)
        # Quadrado a é desenhado estaticamente no lugar (0,0) - (a,a)
        elements.extend(draw_square_a(ax, alpha))
        
        # Quadrado b (Deslocamos temporariamente para cima para evitar sobreposição)
        # Quadrado b é desenhado estaticamente no lugar (0,0) - (-b, b)
        elements.extend(draw_square_b(ax, alpha))

        # Título da Cena
        ax.set_title('Cena 2: Quadrados dos Catetos $a^2$ e $b^2$', fontsize=16, pad=10)
        
    # --- Cena 3: Aparecimento do Quadrado na Hipotenusa 'c' (Frames 120 a 180) ---
    elif frame < 3 * frames_per_stage:
        f = frame - 2 * frames_per_stage
        
        # Mantém o triângulo e os quadrados de 'a' e 'b'
        elements.extend(draw_triangle(ax, P1, P2, P3))
        elements.extend(draw_square_a(ax))
        elements.extend(draw_square_b(ax))
        
        # Animação de fade-in do quadrado de 'c'
        alpha = min(1.0, f / frames_per_stage)
        elements.extend(draw_square_c(ax, alpha))
        
        # Título da Cena
        ax.set_title('Cena 3: Quadrado da Hipotenusa $c^2$', fontsize=16, pad=10)

    # --- Cena 4: Demonstração da Soma das Áreas (Frames 180 a 300) ---
    else:
        f = frame - 3 * frames_per_stage
        
        # Mantém o triângulo e os 3 quadrados estáticos
        elements.extend(draw_triangle(ax, P1, P2, P3))
        elements.extend(draw_square_a(ax))
        elements.extend(draw_square_b(ax))
        elements.extend(draw_square_c(ax))
        
        # Demonstração: Foco na Fórmula e Soma das Áreas
        
        # Fase 1: Enfatizar a soma (Cresce e Desaparece)
        if f < 60:
            scale = 1 + 0.1 * np.sin(np.pi * f / 30) # Pulsar
            alpha = 1
        
        # Fase 2: Mostrar a fórmula final
        else:
            scale = 1.0
            alpha = 1.0
            
        formula_text = ax.text(a + b/2, b + a/2, 
                               '$a^2 + b^2 = c^2$', 
                               fontsize=30, 
                               fontweight='bold', 
                               ha='center', va='center', 
                               color='purple', 
                               transform=ax.transData, 
                               zorder=5, 
                               alpha=alpha)
        
        # Animação do Pulsar (Não funciona bem com FuncAnimation, mas deixamos o código)
        # A escala é aplicada apenas ao texto.
        formula_text.set_size(30 * scale)
        elements.append(formula_text)

        # Título da Cena
        ax.set_title('Cena 4: Teorema de Pitágoras $a^2 + b^2 = c^2$', fontsize=16, pad=10)

    return elements

# 4. Geração e Execução da Animação
print("Gerando a animação...")
# Intervalo em ms (30ms ~ 33 FPS)
ani = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=False, interval=30, repeat=True)

# Recomenda-se salvar a animação em um formato que você possa visualizar (e.g., mp4, gif)
# Nota: Para salvar, você pode precisar do 'ffmpeg' instalado no seu sistema.
# ani.save('teorema_de_pitagoras.mp4', writer='ffmpeg', fps=30)

# Exibe a animação
plt.show()
print("Animação concluída.")