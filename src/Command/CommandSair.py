import sys
from Command.Comando import Command

class ComandoSair(Command):
    def __init__(self):
        """
        O comando 'sai' não requer argumentos.
        """
        pass

    def executar(self):
        """
        Exibe uma mensagem de despedida e encerra a execução do programa.
        Esta funcionalidade é descrita na Seção 6 do documento de trabalho. 
        """
        print("Saindo do sistema de biblioteca...")
        sys.exit(0) # Termina o programa com status de sucesso (0)