import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = np.linspace(0, 4 * np.pi, 500)

y_data = np.abs(np.sin(x_data))