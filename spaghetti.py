from manim import *

class Spaghettification(Scene):
    def construct(self):
        # 1. Configurar o Buraco Negro
        black_hole = Circle(radius=1, color=BLACK, fill_opacity=1)
        black_hole.set_stroke(color=WHITE, width=2) # Borda branca para ver no fundo preto
        event_horizon = Circle(radius=1.2, color=ORANGE, fill_opacity=0.3).set_stroke(width=0)
        
        # Agrupar buraco negro e horizonte
        bh_group = VGroup(black_hole, event_horizon)
        bh_group.move_to(DOWN * 2) # Posicionar na parte de baixo da tela

        # 2. Configurar o "Astronauta" (representado por um círculo)
        astronaut = Circle(radius=0.5, color=BLUE, fill_opacity=0.5)
        astronaut.move_to(UP * 3) # Começa no topo

        # Adicionar objetos na cena
        self.add(bh_group, astronaut)
        self.wait(0.5)

        # 3. Animação da Queda e Estiramento (Espaguetificação)
        self.play(
            # Move para o centro do buraco negro
            astronaut.animate.move_to(bh_group.get_center()),
            
            # Estica no eixo Y (altura) e achata no eixo X (largura)
            astronaut.animate.stretch(4, dim=1).stretch(0.2, dim=0),
            
            # Muda a cor para vermelho (Redshift/Efeito Doppler)
            astronaut.animate.set_color(RED),
            
            run_time=3, # Duração da animação
            rate_func=linear # Velocidade constante
        )

        self.wait(1)