import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation

def animate_line_creation():
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'r-') # 'r-' for red line

    def init():
        ax.set_xlim(-5, 5)
        ax.set_ylim(-8, 12)
        ax.set_title("Gráfico de y = 2x + 2")
        ax.set_xlabel("Eixo X")
        ax.set_ylabel("Eixo Y")
        ax.grid(True)
        return ln,

    def update(frame):
        x = frame
        y = 2 * x + 2
        xdata.append(x)
        ydata.append(y)
        ln.set_data(xdata, ydata)
        return ln,

    # Gerar os frames de -5 a 5 com um passo pequeno
    frames = np.arange(-5, 5.1, 0.1) # Vai de -5 a 5 com passos de 0.1

    ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)
    plt.show()

if __name__ == "__main__":
    animate_line_creation()