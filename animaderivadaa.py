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

        self.play(Create(secant_line), Write(secant_label))
        self.play(Create(brace_h), Write(label_h))
        self.wait(2)

        # 4. A Animação do Limite (h tendendo a 0)
        title_anim = Text("O Limite: h tende a 0", font_size=30).to_edge(UP)
        self.play(Write(title_anim))

        # Animamos o valor de x de Q para se aproximar de x de P (de 4 até 2.001)
        # Não vamos exatamente até 2.0 para evitar problemas numéricos na reta secante dinâmica
        self.play(
            x_q_tracker.animate.set_value(x_p + 0.001),
            run_time=6,
            rate_func=easeInOutCubic
        )
        self.wait(1)

        # 5. Transformação para Reta Tangente (A Derivada)
        # Agora que Q está praticamente sobre P, a reta verde É visualmente a tangente.
        
        # Vamos criar a reta tangente "real" matematicamente no ponto P (x=2)
        # A derivada de 0.5x^2 é x. Em x=2, a inclinação é 2.
        tangent_line = axes.get_tangent_line(func_equation, x_p, length=6, line_config={"color": RED_E, "stroke_width": 4})
        tangent_label = Text("Reta Tangente (Derivada)", font_size=20, color=RED_E).to_corner(UR)

        # Limpamos os elementos móveis e mostramos a tangente final
        self.play(
            FadeOut(dot_q), FadeOut(label_q), 
            FadeOut(brace_h), FadeOut(label_h),
            FadeOut(secant_label), FadeOut(title_anim),
            # Substituímos visualmente a reta secante dinâmica pela tangente estática
            ReplacementTransform(secant_line, tangent_line),
            Write(tangent_label)
        )

        # Foco final no ponto P e sua tangente
        final_text = MarkupText(
            f"Inclinação em P = {2 * 0.5 * x_p:.1f}", 
            font_size=24
        ).next_to(dot_p, DOWN*2)
        self.play(Write(final_text))

        self.wait(3)