from vpython import sphere, vector, color, rate, canvas, arrow

scene = canvas(title='Movimento de um Elétron em Campo Magnético', 
               width=800, height=600, background=color.black)

q = -1.6e-19  # Carga do elétron
m = 9.1e-31   # Massa do elétron
B_field = vector(0, 0, 5e-11) # Campo magnético apontando para "fora" da tela (eixo Z)

eletron = sphere(pos=vector(-5, 0, 0), radius=0.2, color=color.yellow, make_trail=True)
eletron.v = vector(2, 1, 0) # Velocidade inicial (componente em Y gera o movimento helicoidal)

for x in range(-5, 6, 2):
    for y in range(-3, 4, 2):
        arrow(pos=vector(x, y, 0), axis=vector(0, 0, 0.5), color=color.blue, shaftwidth=0.05)

dt = 0.01

while True:
    rate(100)
    
    # Cálculo da Força de Lorentz: F = q * (v produto vetorial B)
    F_lorentz = q * cross(eletron.v, B_field)
    
    # Segunda Lei de Newton: a = F / m
    aceleracao = F_lorentz / m
    
    # Atualização da velocidade e posição (Método de Euler)
    eletron.v = eletron.v + aceleracao * dt
    eletron.pos = eletron.pos + eletron.v * dt