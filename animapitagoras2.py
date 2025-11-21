import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np

# --- 1. Parâmetros e Configurações ---
# Terna Pitagórica (3, 4, 5)
a = 3
b = 4
c = np.sqrt(a**2 + b**2) # 5

# Cores
color_a = '#2ecc71'  # Verde Esmeralda (a^2)
color_b = '#3498db'  # Azul Petra (b^2)
color_c = '#e74c3c'  # Vermelho Alizarina (c^2)
color_bg = '#f0f0f0' # Fundo (Claro)

# Configurações do plot: Foco na área de reconfiguração.
# Para a demonstração (Cenas 3 e 4), movemos o triângulo de base para o centro.
offset_x = 5
offset_y = 5

fig, ax = plt.subplots(figsize=(10, 10), facecolor=color_bg)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-1, offset_x + b + 2)
ax.set_ylim(-1, offset_y + b + 2)
ax.axis('off')

# Posições dos vértices do triângulo base (com offset para o centro)
P1 = np.array([offset_x, offset_y])
P2 = np.array([offset_x + a, offset_y])
P3 = np.array([offset_x, offset_y + b])

# --- 2. Funções de Desenho ---

def draw_triangle(ax, P1, P2, P3, color='k', zorder=3):
    """Desenha o triângulo retângulo e as etiquetas."""
    triangle_coords = np.array([P1, P2, P3, P1])
    line, = ax.plot(triangle_coords[:, 0], triangle_coords[:, 1], color=color, linewidth=2, zorder=zorder)
    
    # Marca o ângulo reto (pequeno quadrado)
    rect_angle = patches.Rectangle((P1[0], P1[1]), 0.3, 0.3, edgecolor=color, facecolor='none', linewidth=1, zorder=zorder)
    ax.add_patch(rect_angle)
    
    # Etiquetas (simples na função base)
    label_a = ax.text(P1[0] + a/2, P1[1] - 0.5, '$a$', fontsize=18, ha='center', va='top', color=color, zorder=zorder+1)
    label_b = ax.text(P1[0] - 0.5, P1[1] + b/2, '$b$', fontsize=18, ha='right', va='center', color=color, zorder=zorder+1)
    
    # Ponto médio da hipotenusa
    mid_c_x = (P2[0] + P3[0]) / 2
    mid_c_y = (P2[1] + P3[1]) / 2
    rotation_c = np.degrees(np.arctan2(b, a))
    label_c = ax.text(mid_c_x + 0.3, mid_c_y - 0.2, '$c$', fontsize=18, ha='center', va='center', color=color, zorder=zorder+1, rotation=rotation_c)
    
    return [line, rect_angle, label_a, label_b, label_c]

def draw_square(ax, xy, side, color, label, alpha=1.0, zorder=1):
    """Desenha um quadrado genérico."""
    square = patches.Rectangle(xy, side, side, edgecolor=color, facecolor=color, alpha=0.3*alpha, linewidth=3, zorder=zorder)
    ax.add_patch(square)
    area_label = ax.text(xy[0] + side/2, xy[1] + side/2, label, fontsize=20, ha='center', va='center', color='k', zorder=zorder+1, alpha=alpha)
    return [square, area_label]

def draw_square_c_rotated(ax, P2, P3, alpha=1.0, zorder=1):
    """Desenha o quadrado sobre a hipotenusa 'c' (rotacionado)."""
    vector_c = P3 - P2
    perp_vector = np.array([-vector_c[1], vector_c[0]]) # Veto rotacionado 90 graus
    
    V1, V2 = P2, P3
    V3 = V2 - perp_vector
    V4 = V1 - perp_vector

    square_c_coords = np.array([V1, V2, V3, V4])
    
    square_c = patches.Polygon(square_c_coords, closed=True, edgecolor=color_c, facecolor=color_c, alpha=0.3*alpha, linewidth=3, zorder=zorder)
    ax.add_patch(square_c)
    
    center_x = (V1[0] + V3[0]) / 2
    center_y = (V1[1] + V3[1]) / 2
    area_label_c = ax.text(center_x, center_y, '$c^2$', fontsize=20, ha='center', va='center', color='k', zorder=zorder+1, alpha=alpha)
    
    return [square_c, area_label_c]

# --- 3. Lógica da Animação (Init e Update) ---
total_frames = 400
frames_per_stage = 70

def init():
    """Inicializa a animação (limpa o eixo)."""
    ax.clear()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1, offset_x + b + 2)
    ax.set_ylim(-1, offset_y + b + 2)
    ax.axis('off')
    return []

def update(frame):
    """Atualiza o quadro da animação com base no tempo."""
    ax.clear()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1, offset_x + b + 2)
    ax.set_ylim(-1, offset_y + b + 2)
    ax.axis('off')
    elements = []
    
    # --- Cena 1: Introdução ao Triângulo Retângulo (Frames 0 a 70) ---
    if frame < frames_per_stage:
        elements.extend(draw_triangle(ax, P1, P2, P3))
        ax.set_title('Cena 1: Introdução ao Triângulo Retângulo $a, b, c$', fontsize=16, pad=10)
        
    # --- Cena 2: Construção dos Quadrados (Frames 70 a 140) ---
    elif frame < 2 * frames_per_stage:
        f = frame - frames_per_stage
        alpha = min(1.0, f / (frames_per_stage * 0.5))
        
        elements.extend(draw_triangle(ax, P1, P2, P3))
        
        # Quadrado a
        elements.extend(draw_square(ax, (P1[0], P1[1] - a), a, color_a, '$a^2$', alpha))
        
        # Quadrado b
        elements.extend(draw_square(ax, (P1[0] - b, P1[1]), b, color_b, '$b^2$', alpha))
        
        # Quadrado c
        elements.extend(draw_square_c_rotated(ax, P2, P3, alpha))

        ax.set_title('Cena 2: Construção dos Quadrados $a^2$, $b^2$, $c^2$', fontsize=16, pad=10)

    # --- Cena 3: Demonstração da Área (Reconfiguração de Peças) (Frames 140 a 330) ---
    elif frame < 3 * frames_per_stage + 50:
        f = frame - 2 * frames_per_stage
        
        # Desenha Triângulo (Fundo) e Quadrado C (Alvo)
        elements.extend(draw_triangle(ax, P1, P2, P3, color='gray', zorder=0))
        elements.extend(draw_square_c_rotated(ax, P2, P3, alpha=0.1, zorder=0)) # C Alvo
        
        # A. Preparação: Quadrados A e B Originais (Fade-out ou Transparência)
        alpha_orig = max(0.2, 1.0 - f / 50)
        elements.extend(draw_square(ax, (P1[0], P1[1] - a), a, color_a, '$a^2$', alpha_orig, zorder=0))
        elements.extend(draw_square(ax, (P1[0] - b, P1[1]), b, color_b, '$b^2$', alpha_orig, zorder=0))
        
        # B. As Peças: Reconfiguração geométrica (Simulando o derramamento/encaixe)
        
        # O quadrado C está sobre a hipotenusa. Os quadrados A e B serão reconfigurados.
        
        # Definindo as peças de A (Para este método, é mais fácil usar 4 triângulos de a, b, c e 1 quadrado central)
        # Vamos reconfigurar A e B como 4 triângulos e 1 quadrado central (Método de Perigal/Bhaskara adaptado)
        
        # Os 4 triângulos que formam o $c^2$ (girados)
        triangle_color = 'k'
        fill_alpha = 0.5
        
        # Para simplificar a animação: Movemos a área $a^2$ e $b^2$ para preencher $c^2$.
        
        # 1. Desenha o quadrado C (Preenchimento)
        elements.extend(draw_square_c_rotated(ax, P2, P3, alpha=1.0, zorder=0)) # C como fundo
        
        # 2. Deslocamento das Peças
        # (Este é o ponto onde o derramamento seria simulado, mas faremos com o reposicionamento das áreas)
        
        # Vértices do quadrado C (Alvo) - Posição final para as peças
        vector_c = P3 - P2
        perp_vector = np.array([-vector_c[1], vector_c[0]])
        V1, V2 = P2, P3
        V3 = V2 - perp_vector
        V4 = V1 - perp_vector
        
        # 2.1. Quadrado A (Movemos A para a parte interna de C)
        # Posição inicial: (P1[0], P1[1] - a)
        # Posição final (aproximada, simplificada para visualização): centro do C
        
        start_pos_a = np.array([P1[0], P1[1] - a])
        target_center_a = (V1 + V3)/2 - [0, a/4] # Deslocamento aproximado
        
        # Animação de movimento (f)
        movement_factor = min(1.0, (f - 10) / 70) 
        current_center_a_x = start_pos_a[0] + (target_center_a[0] - start_pos_a[0]) * movement_factor
        current_center_a_y = start_pos_a[1] + (target_center_a[1] - start_pos_a[1]) * movement_factor
        
        elements.extend(draw_square(ax, (current_center_a_x, current_center_a_y), a, color_a, '$a^2$', alpha=1.0, zorder=2))
        
        # 2.2. Quadrado B (Movemos B para a parte interna de C)
        # Posição inicial: (P1[0] - b, P1[1])
        start_pos_b = np.array([P1[0] - b, P1[1]])
        target_center_b = (V1 + V3)/2 + [0, b/4] # Deslocamento aproximado

        movement_factor_b = min(1.0, (f - 30) / 70)
        current_center_b_x = start_pos_b[0] + (target_center_b[0] - start_pos_b[0]) * movement_factor_b
        current_center_b_y = start_pos_b[1] + (target_center_b[1] - start_pos_b[1]) * movement_factor_b
        
        elements.extend(draw_square(ax, (current_center_b_x, current_center_b_y), b, color_b, '$b^2$', alpha=1.0, zorder=2))

        ax.set_title('Cena 3: Demonstração - Áreas $a^2$ e $b^2$ preenchem $c^2$', fontsize=16, pad=10)
        
    # --- Cena 4: Conclusão Visual (Frames 330 a 400) ---
    else:
        f = frame - (3 * frames_per_stage + 50)
        
        # Mantém Triângulo (Fundo) e Quadrado C (Alvo preenchido)
        elements.extend(draw_triangle(ax, P1, P2, P3, color='gray', zorder=0))
        elements.extend(draw_square_c_rotated(ax, P2, P3, alpha=1.0, zorder=0))
        
        # Simula o preenchimento (Mantemos as peças no centro de C)
        center_c = (V1 + V3)/2
        
        # Quadrado A (Meio do C)
        elements.extend(draw_square(ax, (center_c[0] - a/2, center_c[1] - a/2), a, color_a, '$a^2$', alpha=0.5, zorder=1))
        # Quadrado B (Meio do C)
        elements.extend(draw_square(ax, (center_c[0] - b/2, center_c[1] - b/2), b, color_b, '$b^2$', alpha=0.5, zorder=1))

        
        # Fórmula: Surge e Pulsa
        alpha_formula = min(1.0, f / 30)
        scale = 1 + 0.1 * np.sin(np.pi * f / 30) # Pulsar sutil
        
        formula_text = ax.text(offset_x + b + 1.5, offset_y + b + 1.5, 
                               '$a^2 + b^2 = c^2$', 
                               fontsize=int(30 * scale), 
                               fontweight='bold', 
                               ha='center', va='center', 
                               color='purple', 
                               zorder=5, 
                               alpha=alpha_formula)
        elements.append(formula_text)

        ax.set_title('Cena 4: Conclusão - Teorema de Pitágoras Provado', fontsize=16, pad=10)


    return elements

# --- 4. Geração e Execução da Animação ---
print("Gerando a animação...")
# Intervalo em ms (30ms ~ 33 FPS)
ani = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=False, interval=30, repeat=True)

# Exibe a animação
plt.show()
print("Animação concluída.")