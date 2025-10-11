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

    circle_turtle.goto(0,0) # Voltar para o centro
    circle_turtle.right(10) # Girar 10 graus
    circle_turtle.forward(radius) # Mover para a borda
    circle_turtle.dot(100, "red") # Desenhar um ponto grande no lugar do círculo
    circle_turtle.backward(radius) # Voltar ao centro
    
    