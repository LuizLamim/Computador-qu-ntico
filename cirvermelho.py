import turtle
import time

# Configurar a tela
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # Desativa a atualização automática para melhor controle

# Criar a tartaruga para o círculo
circle_turtle = turtle.Turtle()
circle_turtle.shape("circle")
circle_turtle.color("red")
circle_turtle.shapesize(stretch_wid=5, stretch_len=5) # Ajusta o tamanho do círculo
circle_turtle.penup()
circle_turtle.goto(0, -100) # Posição inicial do círculo (abaixo do centro)
circle_turtle.pendown()

# Esconder a tartaruga original
circle_turtle.hideturtle()

# Variáveis para a rotação
angle = 0
radius = 100 # Raio do círculo da rotação

# Função para animar o círculo
def animate_circle():
    global angle
    circle_turtle.clear() # Limpa o desenho anterior
    
    # Calcula a nova posição para o círculo
    x = radius * (1 - abs(angle / 360)) * (1 if angle < 180 else -1) # Simples aproximação para girar em torno do centro
    y = radius * (1 - abs(angle / 360)) * (1 if angle < 90 or angle > 270 else -1)
    
    # Para uma rotação mais precisa e simples:
    # circle_turtle.setx(radius * math.cos(math.radians(angle)))
    # circle_turtle.sety(radius * math.sin(math.radians(angle)))
    
    # A maneira mais fácil de fazer um círculo girar é simplesmente girar a própria tartaruga se ela fosse visível
    # Para mover o círculo ao redor de um ponto central:
    # Comece no centro, vá para a posição, desenhe o círculo, volte para o centro
    
    # Uma forma mais direta para o efeito de "círculo girando" é fazer a tartaruga desenhar um círculo enquanto gira sobre si mesma:
    circle_turtle.goto(0,0) # Voltar para o centro
    circle_turtle.right(10) # Girar 10 graus
    circle_turtle.forward(radius) # Mover para a borda
    circle_turtle.dot(100, "red") # Desenhar um ponto grande no lugar do círculo
    circle_turtle.backward(radius) # Voltar ao centro
    
    
    # Uma forma mais simples para o efeito de "círculo vermelho girando" (o círculo em si gira em torno de um ponto)
    # circle_turtle.goto(0, 0) # Volta para o centro
    # circle_turtle.setheading(angle) # Define a direção da tartaruga
    # circle_turtle.forward(radius) # Move para a posição no círculo de rotação
    # circle_turtle.dot(100, "red") # Desenha o círculo vermelho
    # circle_turtle.backward(radius) # Volta para o centro
    
    
    # ** Vamos simplificar para um círculo que se move em órbita **
    import math
    circle_turtle.clear()
    
    center_x, center_y = 0, 0
    
    # Calcula a posição x, y do círculo em sua órbita
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    
    circle_turtle.penup()
    circle_turtle.goto(x, y)
    circle_turtle.pendown()
    
    # Desenha o círculo vermelho na nova posição
    circle_turtle.dot(50, "red") # Tamanho do ponto/círculo
    
    angle += 5 # Incrementa o ângulo para a próxima atualização
    if angle >= 360:
        angle = 0
        
    screen.update() # Atualiza a tela
    screen.ontimer(animate_circle, 20) # Chama a função novamente após 20 ms

# Iniciar a animação
animate_circle()

# Manter a janela aberta até que seja fechada manualmente
screen.mainloop()