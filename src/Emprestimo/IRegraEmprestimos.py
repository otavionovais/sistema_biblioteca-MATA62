from abc import ABC, abstractmethod

class IEmprestimos(ABC):

    @abstractmethod
    def emprestimo_permitido(self, usuario, livro) -> (bool,str):
        pass
    
    @abstractmethod
    def prazo_emprestimo(self) -> int:
        pass    

   