from vpython import sphere, vector, color, rate, canvas
import numpy as np

# Configuração da tela
scene = canvas(title='Animação de Esfera 3D', width=800, height=600, center=vector(0,0,0), background=color.black)

bola = sphere(pos=vector(0,0,0), radius=1, color=color.cyan, make_trail=True)