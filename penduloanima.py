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

x_rest = np.linspace(-N_PENDULUMS/2, N_PENDULUMS/2, N_PENDULUMS)

pendulum_dots, = ax.plot(
    x_rest, np.zeros(N_PENDULUMS), 
    'o', markersize=15, 
    color='deepskyblue',
    markeredgecolor='white',
    markeredgewidth=1.5
)

time_text = ax.text(
    0.01, 0.05, 
    '', 
    transform=ax.transAxes, 
    ha='left', 
    fontsize=12, 
    color='white'
)

def animate(frame):
    """Calcula a posição dos pêndulos a cada quadro (frame) e atualiza a plotagem."""
    
    t = frame / FPS 
    
    displacement = AMPLITUDE * np.cos(angular_frequencies * t)
    
    new_x = x_rest + displacement
    
    new_y = np.zeros(N_PENDULUMS) 

    pendulum_dots.set_data(new_x, new_y)
    
    time_text.set_text(f'Tempo: {t:.2f}s (Ciclo: {(t / T_SYSTEM) * 100:.1f}%)')
    
    return pendulum_dots, time_text

ani = animation.FuncAnimation(
    fig,                 
    animate,            
    frames=NUM_FRAMES,   
    interval=1000/FPS,   
    blit=True,           
    repeat=True         
)

plt.show()

