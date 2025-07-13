from abc import ABC, abstractmethod

class Command(ABC):
    
    @abstractmethod
    def executar(self):
        """Executa o comando."""
        pass