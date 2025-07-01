from Livros.ILivro import ILivro

class Livro(ILivro):
    def __init__(self, id, titulo, autor, ano_publicacao, editora, edicao):
        super().__init__(id, titulo, autor, ano_publicacao, editora, edicao)
        self._disponivel = True
        self._reservas = []
        self._emprestimos = []

    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_ano_publicacao(self):
        return self._ano_publicacao

    def is_disponivel(self):
        return self._disponivel

    def adicionar_reserva(self, reserva):
        self._reservas.append(reserva)

    def adicionar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)