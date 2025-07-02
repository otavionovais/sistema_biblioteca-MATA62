from Livros.ILivro import ILivro

class Livro(ILivro):
    def __init__(self, id, titulo, autor, ano_publicacao, editora, edicao):
        super().__init__(id, titulo, autor, ano_publicacao, editora, edicao)
        self._reservas = []
        self._exemplares = []
        self._emprestimos = []
        self._observadores = []

    def qtd_exemplares_disponiveis(self):
        return sum(1 for exemplar in self._exemplares if exemplar.esta_disponivel())
    
    def usuario_tem_reserva(self, usuario):
        return any(reserva.get_usuario() == usuario for reserva in self._reservas)
    
    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_ano_publicacao(self):
        return self._ano_publicacao

    def adicionar_reserva(self, reserva):
        self._reservas.append(reserva)
        if len(self._reservas) > 2:
            self.notificar_observadores

    def adicionar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)
    
    def adicionar_exemplar(self, exemplar):
        self._exemplares.append(exemplar)
    
    def get_exemplares(self):
        return self._exemplares
    
    def adicionar_observador(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)
    
    def notificar_observadores(self):
        for observador in self._observadores:
            observador.notificar(self)