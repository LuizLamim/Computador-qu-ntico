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