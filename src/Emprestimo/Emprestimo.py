from datetime import timedelta


class Emprestimo:
    def __init__(self, id, usuario, livro, exemplar, data_emprestimo, dias_emprestimo):
        self._id = id
        self._usuario = usuario
        self._livro = livro
        self._exemplar = exemplar
        self._data_emprestimo = data_emprestimo
        self._data_devolucao_prevista = data_emprestimo + timedelta(days=dias_emprestimo)
        self._data_devolucao_real = None
        self._finalizado = False

        self._exemplar.marcar_emprestado()

    def marcar_como_devolvido(self, data_real):
        self._data_devolucao_real = data_real
        self._finalizado = True
        self._exemplar.marcar_disponivel()

        if data_real > self._data_devolucao_prevista:
            self._usuario.mudar_situacao_devedor()
