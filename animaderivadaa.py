from manim import *

class ConceitoDeDerivada(Scene):
    def construct(self):
        # 1. Configuração do Cenário (Eixos e Função)
        # Criamos um sistema de coordenadas
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 9, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]},
        ).add_coordinates()
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Definimos a função para animar (uma parábola simples: y = 0.5 * x^2)
        def func_equation(x):
            return 0.5 * (x**2)

        # Plotamos a função no gráfico
        graph = axes.plot(func_equation, color=BLUE_C, x_range=[-0.5, 4.5])
        graph_label = axes.get_graph_label(graph, label="f(x) = 0.5x^2", x_val=4, direction=UP)

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # 2. Definindo os Pontos P (fixo) e Q (móvel)
        # Ponto fixo P onde queremos encontrar a derivada (vamos usar x=2)
        x_p = 2
        point_p_coords = axes.coords_to_point(x_p, func_equation(x_p))
        dot_p = Dot(point_p_coords, color=RED, radius=0.1)
        label_p = Text("P", font_size=24, color=RED).next_to(dot_p, UP+LEFT)

        # Ponto móvel Q. Usamos um ValueTracker para controlar sua posição x.
        # Começamos com Q em x=4.
        x_q_tracker = ValueTracker(4)
        
        # O ponto Q e seu rótulo precisam ser redesenhados sempre que o tracker mudar
        dot_q = always_redraw(lambda: Dot(
            axes.coords_to_point(x_q_tracker.get_value(), func_equation(x_q_tracker.get_value())),
            color=YELLOW, radius=0.1

        ))
        label_q = always_redraw(lambda: Text("Q", font_size=24, color=YELLOW).next_to(dot_q, UP+RIGHT))

        self.play(FadeIn(dot_p), Write(label_p))
        self.play(FadeIn(dot_q), Write(label_q))

        # 3. A Reta Secante e a Distância 'h'
        # A reta secante conecta P e Q dinamicamente
        secant_line = always_redraw(lambda: axes.get_secant_line_graph(
            function=graph,
            x_start=x_p,
            x_end=x_q_tracker.get_value(),
            dx=0.01, # Pequeno ajuste para evitar divisão por zero se x_start == x_end
            line_config={"color": GREEN_B, "stroke_width": 3},
            length_ratio=1.5 # Faz a linha se estender um pouco além dos pontos
        ))
        secant_label = Text("Reta Secante", font_size=20, color=GREEN_B).to_corner(UR)

        # A chave que mostra a distância horizontal 'h' (delta x)
        brace_h = always_redraw(lambda: BraceBetweenPoints(
            axes.coords_to_point(x_p, 0),
            axes.coords_to_point(x_q_tracker.get_value(), 0),
            color=ORANGE, buff=0.1
        ))
        label_h = always_redraw(lambda: brace_h.get_text("$h$", buff=0.1, font_size=24, color=ORANGE))
