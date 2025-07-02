from abc import ABC, abstractmethod

class IComando(ABC):
    
    @abstractmethod
    def executar(self):
        """Executa o comando."""
        pass