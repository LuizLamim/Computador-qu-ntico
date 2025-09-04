import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
circle, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return circle,

def animate(i):
    y = 0.5 * (1 - (i % 200) / 100)
    circle.set_data(0, y)
    return circle,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=100, interval=20, blit=True)

plt.show()