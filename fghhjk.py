import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 1. Configuração da Figura e Eixos ---
fig, ax = plt.subplots()

# Defina o intervalo para x e o valor base da exponencial (a > 1 para crescimento)
x = np.linspace(0, 5, 500)
base_exponencial = 1.5

# Calcula os valores de y para toda a curva (para configurar os limites do eixo y)
y_max = base_exponencial**5 

# Configura os limites dos eixos
ax.set_xlim(x.min(), x.max())
ax.set_ylim(0, y_max * 1.1) # Um pouco mais alto que o valor máximo
ax.grid(True)
ax.set_title(f'Animação da Curva Exponencial: y = {base_exponencial}^x')
ax.set_xlabel('x')
ax.set_ylabel('y')


line, = ax.plot([], [], color='blue', lw=2)


time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes) 

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    
    x_data = x[:i+1]
    y_data = base_exponencial**x_data

    # 2. Atualize os dados da linha.
    line.set_data(x_data, y_data)
    
    # 3. Atualize o texto (opcional)
    time_text.set_text(f'x atual: {x[i]:.2f}')
    
    # Retorne os objetos (artistas) modificados que precisam ser redesenhados
    return line, time_text

# --- 4. Criação do Objeto Animação ---
# FuncAnimation(figura, função de animação, função de inicialização, frames, intervalo, blit)
num_frames = len(x)

ani = animation.FuncAnimation(
    fig, 
    animate, 
    init_func=init,
    frames=num_frames, 
    interval=20, # Intervalo entre frames em milissegundos (20ms = 50 FPS)
    blit=True    # Otimiza o desenho, desenhando apenas o que mudou
)

# --- 5. Exibir ou Salvar a Animação ---

# Para exibir em uma janela interativa:
plt.show() 


