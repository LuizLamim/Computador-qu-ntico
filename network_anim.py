from manim import *
import random

# Configurações visuais para ficar com a "cara" do 3b1b
config.background_color = "#1e1e1e" # Um cinza escuro agradável
NODE_RADIUS = 0.15
NODE_COLOR = WHITE
EDGE_COLOR = GREY
EDGE_OPACITY = 0.3
HIGHLIGHT_COLOR_1 = YELLOW  # Cor para a entrada
HIGHLIGHT_COLOR_2 = BLUE    # Cor para as camadas ocultas
HIGHLIGHT_COLOR_3 = GREEN   # Cor para a saída

class NeuralNetworkFlow(Scene):
    def construct(self):
        # ==========================================
        # 1. DEFINIR A ARQUITETURA DA REDE
        # ==========================================
        # Define quantas camadas e quantos neurônios por camada
        # Ex: [Entrada, Oculta 1, Oculta 2, Saída]
        layer_sizes = [4, 6, 6, 2]
        
        layers = VGroup() # Grupo para guardar todas as camadas

        # --- Criar os Nós (Neurônios) ---
        for size in layer_sizes:
            # Cria uma camada vertical de círculos
            layer = VGroup(*[
                Circle(radius=NODE_RADIUS, color=NODE_COLOR, stroke_width=2) 
                for _ in range(size)
            ])
            layer.arrange(DOWN, buff=0.4) # Espaçamento vertical entre nós
            layers.add(layer)

        # Organiza as camadas horizontalmente
        layers.arrange(RIGHT, buff=2.5) # Espaçamento horizontal entre camadas
        layers.move_to(ORIGIN) # Centraliza tudo na tela

        # --- Criar as Arestas (Sinapses/Pesos) ---
        edges = VGroup()
        # Itera entre pares de camadas adjacentes
        for i in range(len(layers) - 1):
            layer_current = layers[i]
            layer_next = layers[i+1]
            # Conecta cada nó da camada atual a todos da próxima
            for u in layer_current:
                for v in layer_next:
                    edge = Line(
                        u.get_center(), 
                        v.get_center(), 
                        color=EDGE_COLOR, 
                        stroke_width=1,
                        stroke_opacity=EDGE_OPACITY
                    )
                    edges.add(edge)

        # Coloca as arestas "atrás" dos nós na ordem de desenho
        network_group = VGroup(edges, layers)
        
        # ==========================================
        # 2. ANIMAÇÃO DA CONSTRUÇÃO (Ato 1)
        # ==========================================
        self.play(LaggedStartMap(Create, layers, lag_ratio=0.5), run_time=2)
        self.wait(0.5)
        # Mostra as conexões aparecendo suavemente
        self.play(Create(edges), run_time=3, rate_func=smooth)
        self.wait(1)

        # --- Rotulagem ---
        input_label = Text("Camada de\nEntrada", font_size=20).next_to(layers[0], UP)
        hidden_label = Text("Camadas\nOcultas", font_size=20).move_to(layers[1:3].get_top() + UP*0.5)
        output_label = Text("Camada de\nSaída", font_size=20).next_to(layers[-1], UP)
        labels = VGroup(input_label, hidden_label, output_label)

        self.play(Write(labels), run_time=1.5)
        self.wait(1)

        # ==========================================
        # 3. ANIMAÇÃO DO FLUXO DE DADOS (Ato 2 - Forward Pass)
        # ==========================================
        
        # --- Passo 1: Ativar a Entrada ---
        # Vamos simular que o 1º e o 3º neurônio de entrada foram ativados
        input_layer = layers[0]
        active_inputs_indices = [0, 2] 
        active_inputs = VGroup(*[input_layer[i] for i in active_inputs_indices])

        self.play(
            active_inputs.animate.set_fill(HIGHLIGHT_COLOR_1, opacity=1).set_stroke(HIGHLIGHT_COLOR_1),
            run_time=0.8
        )
        self.wait(0.3)

        # Loop para propagar o sinal pelas camadas ocultas até a saída
        current_active_nodes = active_inputs
        active_color = HIGHLIGHT_COLOR_1

        # Itera da primeira camada até a penúltima
        for i in range(len(layers) - 1):
            next_layer = layers[i+1]
            
            # Define a cor da próxima ativação
            if i == len(layers) - 2:
                 next_active_color = HIGHLIGHT_COLOR_3 # Cor final para saída
            else:
                 next_active_color = HIGHLIGHT_COLOR_2 # Cor para ocultas

            # 1. Criar linhas de sinal que piscam (ShowPassingFlash)
            signals = VGroup()
            for source_node in current_active_nodes:
                for target_node in next_layer:
                    # Cria uma linha temporária grossa e colorida
                    signal = Line(
                        source_node.get_center(),
                        target_node.get_center(),
                        color=active_color,
                        stroke_width=5
                    )
                    signals.add(signal)
            
            # Anima o "pulso" viajando pelas linhas
            self.play(ShowPassingFlash(signals, time_width=0.3, lag_ratio=0.1), run_time=1.5)

            # 2. Ativar nós da próxima camada
            # (Na vida real é um cálculo, aqui escolhemos aleatoriamente para ilustrar)
            if i < len(layers) - 2:
                # Para camadas ocultas, ativa alguns aleatórios
                num_to_activate = max(2, len(next_layer) // 2)
                active_indices = random.sample(range(len(next_layer)), num_to_activate)
                next_active_nodes = VGroup(*[next_layer[idx] for idx in active_indices])
            else:
                # Para a camada de saída, ativa apenas UM (a previsão final)
                # Vamos ativar o neurônio de cima (índice 0)
                next_active_nodes = VGroup(next_layer[0])
                # Efeito extra na saída final: aumenta de tamanho
                self.play(next_active_nodes.animate.scale(1.3), run_time=0.2)

            # Ilumina os nós da próxima camada
            self.play(
                next_active_nodes.animate.set_fill(next_active_color, opacity=1).set_stroke(next_active_color),
                run_time=0.5
            )

            # 3. Desativar ("esfriar") os nós anteriores para limpar a visualização
            self.play(
                current_active_nodes.animate.set_fill(opacity=0).set_stroke(NODE_COLOR),
                run_time=0.3
            )
            
            # Atualiza para o próximo loop
            current_active_nodes = next_active_nodes
            active_color = next_active_color

        self.wait(2)
        # Fade out final para encerrar a cena elegante
        self.play(FadeOut(VGroup(network_group, labels, current_active_nodes)))