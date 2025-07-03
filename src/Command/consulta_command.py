import Command
from Repositorio import Repositorio

class ConsultaCommand(Command):

    def executar(self, id_usuario):
        repositorio = Repositorio()
        usuario = repositorio.get_usuario(id_usuario)

        if usuario is None:
            print(f"Usuário com ID {id_usuario} não encontrado.")
            return
        
        
        
