import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t_max = 10.0
dt = 0.05
t = np.arange(0, t_max, dt)

P0 = 100.0   # Potência Inicial (ex: 100 Watts ou %)
k = 0.5

potencia = P0 * np.exp(-k * t)

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, t_max)
ax.set_ylim(0, P0 + 10)