from vpython import sphere, vector, color, rate, canvas
import numpy as np

# Configuração da tela
scene = canvas(title='Animação de Esfera 3D', width=800, height=600, center=vector(0,0,0), background=color.black)

# Criando a esfera
# pos: posição inicial (x, y, z)
# radius: raio da esfera
# color: cor da esfera
bola = sphere(pos=vector(0,0,0), radius=1, color=color.cyan, make_trail=True)

# Variáveis para a animação
t = 0
dt = 0.01

print("Iniciando animação...")

while True:
    # Define a velocidade da animação (frames por segundo)
    rate(100)
    
    # Atualiza a posição vertical usando a função seno (oscilação)
    # y = amplitude * sin(frequencia * tempo)
    bola.pos.y = 2 * np.sin(2 * t)
    
    # Incrementa o tempo
    t += dt