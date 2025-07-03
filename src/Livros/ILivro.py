from abc import ABC, abstractmethod

class ILivro(ABC):
    def __init__(self, id, titulo, autor, ano_publicacao,editora, edicao):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        self._editora = editora
        self._edicao = edicao
    
    

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_titulo(self):
        pass

    @abstractmethod
    def get_autor(self):
        pass

    @abstractmethod
    def get_ano_publicacao(self):
        pass

    @abstractmethod
    def is_disponivel(self):
        pass

    @abstractmethod
    def adicionar_reserva(self):
        pass

    @abstractmethod
    def adicionar_emprestimo(self):
        pass