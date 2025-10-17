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

def obter_cor_gradiente(passo, total_passos):
    """
    Gera uma cor RGB no formato (r, g, b) para um determinado passo da animação.
    Usa o modelo de cores HSL (Hue, Saturation, Lightness) para um gradiente suave.
    """
    # O matiz (Hue) vai de 0.0 a 1.0 (ou de 0 a 360 graus)
    # Variamos o matiz com base no passo da animação
    h = (passo / total_passos)
    s = 1.0  # Saturação máxima
    l = 0.5  # Luminosidade média para cores vibrantes

    # Converte de HSL para RGB (com valores de 0 a 1)
    r, g, b = colorsys.hls_to_rgb(h, l, s)

    # Converte para o formato RGB de 0 a 255 (inteiros)
    r_int = int(r * 255)
    g_int = int(g * 255)
    b_int = int(b * 255)

    return (r_int, g_int, b_int)

# --- Loop de Animação ---

try:
    for i in range(num_frames):
        t.clear() # Limpa o desenho anterior
        
        # 1. Obtém a cor atual para o gradiente
        cor_rgb = obter_cor_gradiente(i, num_frames)
        
        # 2. Desenha o hexágono com a nova cor
        # Usamos a mesma cor para o preenchimento e a borda para um efeito mais limpo
        desenhar_hexagono(t, tamanho_lado, cor_rgb, cor_rgb)
        
        # 3. Atualiza a tela e aguarda
        screen.update()
        time.sleep(velocidade_animacao)

except turtle.Terminator:
    # A exceção Terminator é lançada quando a janela é fechada
    pass

finally:
    # Certifica-se de fechar a janela do turtle corretamente se o loop terminar
    if screen.getcanvas().winfo_exists():
        screen.mainloop()