import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


N_PENDULUMS = 15    
T_SYSTEM = 60.0     
N_CYCLES_MIN = 51   
AMPLITUDE = 1.5     

FPS = 10
NUM_FRAMES = int(T_SYSTEM * FPS)

cycles = N_CYCLES_MIN + np.arange(N_PENDULUMS)[::-1]

frequencies = cycles / T_SYSTEM 
angular_frequencies = 2 * np.pi * frequencies # ω = 2πf

fig, ax = plt.subplots(figsize=(10, 3), facecolor='black')

ax.set_xlim(-N_PENDULUMS/2 - AMPLITUDE, N_PENDULUMS/2 + AMPLITUDE)

ax.set_ylim(-AMPLITUDE/3, AMPLITUDE/3) 
ax.set_aspect('equal', adjustable='box')
ax.axis('off') 


