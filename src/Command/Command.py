from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for commands.
    All commands should inherit from this class and implement the execute method.
    """

    def __init__(self, repositorio: Repositorio):
        self.repositorio = repositorio # O Receiver principal

    @abstractmethod
    def execute(self, *args):
        pass