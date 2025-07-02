class Exemplar:
    def __init__(self, codigo):
        self.codigo = codigo
        self._disponivel = True

    def esta_disponivel(self):
        return self._disponivel

    def marcar_emprestado(self):
        self._disponivel = False

    def marcar_disponivel(self):
        self._disponivel = True
