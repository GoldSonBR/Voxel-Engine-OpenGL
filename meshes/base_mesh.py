import numpy as np


class BaseMesh:
    def __init__(self):
        # contexto OpenGL
        self.ctx = None
        # shader program
        self.program = None
        # vertex buffer, tipo de formato de dados "3f 3f"
        self.vbo_format = None
        # atribuir nomes de acorodo com o formato : ("in_position", "in_color")
        self.attrs: tuple[str, ...] = None
        # objeto vertex array
        self.vao = None

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors=True
        )
        return vao

    def render(self):
        self.vao.render()
