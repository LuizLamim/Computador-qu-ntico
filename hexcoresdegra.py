import turtle
import time
import colorsys

# --- Configuração Inicial ---
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.colormode(255) # Define o modo de cor para usar valores RGB de 0 a 255
screen.tracer(0)      # Desativa a atualização automática da tela para animação mais suave
screen.title("Hexágono Animado com Gradiente de Cor")

t = turtle.Turtle()
t.speed(0) # Velocidade máxima
t.hideturtle() # Esconde a tartaruga