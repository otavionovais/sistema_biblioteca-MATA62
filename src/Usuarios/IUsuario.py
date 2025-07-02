from abc import ABC, abstractmethod

class IUsuario(ABC):

    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
        self.tipo_usuario = self.__class__.__name__
        self._esta_devendo = False
        self._emprestimos_ativos = []
        self._reservas_ativas = []
        self._emprestimos = []
        self._reservas = []
    
    @abstractmethod
    def get_id(self):
        pass
    
    @abstractmethod
    def get_tipo_usuario(self):
        return self.tipo_usuario
    
    @abstractmethod
    def get_nome(self):
        pass
      
    
    @abstractmethod
    def get_esta_devendo(self):
        pass


    @abstractmethod
    def get_emprestimos_ativos(self):
        pass

    
    @abstractmethod
    def get_emprestimos(self):
        pass

    @abstractmethod
    def get_reservas_ativas(self):
        pass

    @abstractmethod
    def get_reservas(self):
        pass

    
    @abstractmethod
    def mudar_situacao_devedor(self):
        pass
        
    @abstractmethod
    def adicionar_reserva_ativa(self):
        pass

    @abstractmethod
    def adicionar_emprestimo_ativo(self):
        pass

    @abstractmethod
    def remover_reserva_ativa(self):
        pass

    @abstractmethod    
    def remover_emprestimo_ativo(self):
        pass
  