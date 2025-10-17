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

# --- Parâmetros ---
tamanho_lado = 100
num_frames = 300 # Número de passos na animação
velocidade_animacao = 0.02 # Pequeno atraso para controlar a velocidade da animação

# --- Funções ---

def desenhar_hexagono(t, lado, cor_preenchimento, cor_caneta):
    """Desenha um hexágono com a cor de preenchimento e caneta especificadas."""
    t.penup()
    # Move a tartaruga para uma posição inicial para centralizar o hexágono
    t.goto(-lado / 2, lado * (3**0.5) / 2) # Exemplo de ponto inicial
    t.pendown()
    t.color(cor_caneta, cor_preenchimento)
    t.begin_fill()
    for _ in range(6):
        t.forward(lado)
        t.right(60)
    t.end_fill()