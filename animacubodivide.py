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