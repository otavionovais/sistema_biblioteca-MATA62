class Exemplar:
    def __init__(self, id):
        self._id = id
        self._disponivel = True

    def get_id(self):
        return self._id

    def esta_disponivel(self):
        return self._disponivel

    def marcar_emprestado(self):
        if not self._disponivel:
            raise Exception("Exemplar não está disponível.")
        self._disponivel = False

    def marcar_disponivel(self):
        self._disponivel = True
