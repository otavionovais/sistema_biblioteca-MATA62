from abc import ABC, abstractmethod

class IRegraEmprestimos(ABC):

    @abstractmethod
    def pode_emprestar(self, usuario, livro) -> (bool,str): # type: ignore
        pass
    
    @abstractmethod
    def dias_emprestimo(self) -> int:
        pass    

   