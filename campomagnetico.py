import numpy as np
import matplotlib.pyplot as plt

def plot_magnetic_field():
    nx, ny = 100, 100
    x = np.linspace(-2, 2, nx)
    y = np.linspace(-2, 2, ny)
    X, Y = np.meshgrid(x, y)