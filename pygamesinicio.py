class PygameSimulator:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.caption = "Pygame Simulator"
        self.is_initialized = False
        self.is_running = False
        self.drawn_shapes = [] # Para armazenar o que foi "desenhado"

    def init(self):
        """Simula a inicialização do Pygame."""
        print("PygameSimulator: Inicializando...")
        self.is_initialized = True
        print("PygameSimulator: Inicializado com sucesso!")

    def display_set_mode(self, width, height):
        """Simula a criação da janela (tela)."""
        if not self.is_initialized:
            print("Erro: PygameSimulator não inicializado. Chame .init() primeiro.")
            return None
        self.screen_width = width
        self.screen_height = height
        print(f"PygameSimulator: Tela configurada para {width}x{height} pixels.")
        return {"width": width, "height": height} # Retorna um objeto simulando a tela

    def display_set_caption(self, caption):
        """Simula a definição do título da janela."""
        if not self.is_initialized:
            print("Erro: PygameSimulator não inicializado. Chame .init() primeiro.")
            return
        self.caption = caption
        print(f"PygameSimulator: Título da janela definido para '{caption}'.")

    def event_get(self):
        """Simula a captura de eventos (teclado, mouse, fechar janela)."""
        # Em um Pygame real, isso retornaria uma lista de eventos.
        # Aqui, vamos simular alguns eventos básicos para demonstração.
        if self.is_running:
            print("PygameSimulator: Verificando eventos...")
            # Simula um evento de "fechar" após algumas iterações ou de forma aleatória
            import random
            if random.random() < 0.1: # 10% de chance de simular um evento de fechar
                print("PygameSimulator: Evento 'QUIT' simulado.")
                return [{"type": "QUIT"}]
            # Simula um evento de tecla pressionada
            if random.random() < 0.05: # 5% de chance de simular um evento de tecla
                key = random.choice(['k_SPACE', 'k_LEFT', 'k_RIGHT'])
                print(f"PygameSimulator: Evento 'KEYDOWN' simulado: {key}")
                return [{"type": "KEYDOWN", "key": key}]
        return []

    def draw_rect(self, color, rect_tuple):
        """Simula o desenho de um retângulo."""
        # color: (R, G, B)
        # rect_tuple: (x, y, width, height)
        print(f"PygameSimulator: Desenhando retângulo na cor {color} na posição {rect_tuple}.")
        self.drawn_shapes.append({"type": "rect", "color": color, "rect": rect_tuple})

    def draw_circle(self, color, center_pos, radius):
        """Simula o desenho de um círculo."""
        # color: (R, G, B)
        # center_pos: (x, y)
        print(f"PygameSimulator: Desenhando círculo na cor {color} no centro {center_pos} com raio {radius}.")
        self.drawn_shapes.append({"type": "circle", "color": color, "center": center_pos, "radius": radius})

    def fill(self, color):
        """Simula o preenchimento da tela com uma cor."""
        print(f"PygameSimulator: Preenchendo a tela com a cor {color}.")
        # Em um jogo real, isso limparia a tela para o próximo frame.
        self.drawn_shapes = [] # "Limpa" as formas desenhadas para simular novo frame
        self.drawn_shapes.append({"type": "fill", "color": color})

    def display_flip(self):
        """Simula a atualização da tela para mostrar o que foi desenhado."""
        print("PygameSimulator: Atualizando a tela (display.flip()).")
        # Em um jogo real, isso mostraria o buffer desenhado na tela.
        # Aqui, podemos imprimir o que supostamente foi desenhado neste frame.
        print("--- Conteúdo do Frame Atual (Simulado) ---")
        if not self.drawn_shapes:
            print("  Nenhuma forma desenhada neste frame.")
        else:
            for shape in self.drawn_shapes:
                print(f"  - {shape['type'].capitalize()}: {shape}")
        print("------------------------------------------")


    def time_delay(self, milliseconds):
        """Simula uma pausa no tempo."""
        import time
        print(f"PygameSimulator: Pausando por {milliseconds}ms.")
        time.sleep(milliseconds / 1000.0)

    def quit(self):
        """Simula o encerramento do Pygame."""
        print("PygameSimulator: Encerrando...")
        self.is_initialized = False
        self.is_running = False
        print("PygameSimulator: Encerrado.")

# --- Exemplo de Uso ---
if __name__ == "__main__":
    pygame_sim = PygameSimulator()

    # 1. Inicializar o "Pygame"
    pygame_sim.init()

    # 2. Configurar a tela
    screen = pygame_sim.display_set_mode(640, 480)
    pygame_sim.display_set_caption("Meu Jogo Simulado")

    # 3. Loop principal do jogo
    pygame_sim.is_running = True
    frame_count = 0
    while pygame_sim.is_running and frame_count < 10: # Limita a 10 frames para demonstração
        frame_count += 1
        print(f"\n--- Frame {frame_count} ---")

        # 4. Processar eventos
        for event in pygame_sim.event_get():
            if event and event.get("type") == "QUIT":
                print("PygameSimulator: Evento 'QUIT' detectado. Saindo do loop.")
                pygame_sim.is_running = False
            elif event and event.get("type") == "KEYDOWN":
                print(f"PygameSimulator: Tecla '{event['key']}' pressionada.")

        # 5. Desenhar na tela (limpar e redesenhar)
        pygame_sim.fill((0, 0, 0)) # Fundo preto
        pygame_sim.draw_rect((255, 0, 0), (50, 50, 100, 75)) # Retângulo vermelho
        pygame_sim.draw_circle((0, 255, 0), (300, 200), 50) # Círculo verde

        # 6. Atualizar a tela
        pygame_sim.display_flip()

        # 7. Controlar a taxa de quadros (simulado)
        pygame_sim.time_delay(500) # Pausa de 500ms (2 quadros por segundo)

    # 8. Encerrar o "Pygame"
    pygame_sim.quit()