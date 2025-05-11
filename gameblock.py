import pyglet
from pyglet.gl import *

class CuboSaltitante(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.largura = 800
        self.altura = 600
        self.set_caption("Cubo Saltitante 3D")
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)

        self.rotacao_x = 0
        self.rotacao_y = 0
        self.translacao_z = -5

        self.vertices = (
            -1, -1, -1,   1, -1, -1,   1,  1, -1,  -1,  1, -1,
            -1, -1,  1,   1, -1,  1,   1,  1,  1,  -1,  1,  1,
        )
        self.cores = (
            1, 1, 1,   1, 1, 1,   1, 1, 1,   1, 1, 1,
            1, 1, 1,   1, 1, 1,   1, 1, 1,   1, 1, 1,
        )
        self.indices = (
            0, 1, 2, 2, 3, 0,
            0, 4, 7, 7, 3, 0,
            4, 5, 6, 6, 7, 4,
            1, 5, 6, 6, 2, 1,
            2, 6, 7, 7, 3, 2,
            0, 1, 5, 5, 4, 0,
        )

        self.batch = pyglet.graphics.Batch()
        self.cubo = self.batch.add(8, GL_QUADS, None,
            ('v3f/static', self.vertices),
            ('c3f/static', self.cores),
            indices=self.indices
        )

        self.velocidade_y = 0
        self.posicao_y = 0
        self.gravidade = -0.1
        self.forca_pulo = 2

    def on_draw(self):
        self.clear()
        glLoadIdentity()
        glTranslatef(0, self.posicao_y, self.translacao_z)
        glRotatef(self.rotacao_x, 1, 0, 0)
        glRotatef(self.rotacao_y, 0, 1, 0)
        self.batch.draw()

    def update(self, dt):
        self.velocidade_y += self.gravidade
        self.posicao_y += self.velocidade_y

        if self.posicao_y < 0:
            self.posicao_y = 0
            self.velocidade_y = 0

        self.rotacao_y += 50 * dt

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE and self.posicao_y == 0:
            self.velocidade_y = self.forca_pulo

if __name__ == '__main__':
    window = CuboSaltitante(800, 600, caption='Cubo Saltitante 3D', resizable=True)
    pyglet.clock.schedule_interval(window.update, 1/60.0)
    pyglet.app.run()