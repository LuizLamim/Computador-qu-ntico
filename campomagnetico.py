import numpy as np
import matplotlib.pyplot as plt

def plot_magnetic_field():
    nx, ny = 100, 100
    x = np.linspace(-2, 2, nx)
    y = np.linspace(-2, 2, ny)
    X, Y = np.meshgrid(x, y)

    m_vector = np.array([0, 1])
    
    R[R == 0] = 1e-10

    dot_mr = m_vector[0] * X + m_vector[1] * Y
    
    constante = 1.0

    vec_term_x = 3 * dot_mr * X
    vec_term_y = 3 * dot_mr * Y