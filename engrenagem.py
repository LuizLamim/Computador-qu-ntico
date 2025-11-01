import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def create_gear_points(num_teeth=12, outer_radius=1.0, inner_radius=0.7, tooth_width_factor=0.5):
    """
    Gera os pontos para desenhar uma engrenagem.
    """
    angles = np.linspace(0, 2 * np.pi, num_teeth * 4, endpoint=False)
    points = []
    for i, angle in enumerate(angles):
        # A cada 4 pontos, alternamos entre raio externo e interno para criar os dentes
        if i % 4 == 0 or i % 4 == 1:
            r = outer_radius
        else:
            r = inner_radius
        
        # Ajusta ligeiramente a largura do dente
        if i % 2 == 0:
            current_angle = angle
        else:
            current_angle = angle + (2 * np.pi / (num_teeth * 4)) * tooth_width_factor