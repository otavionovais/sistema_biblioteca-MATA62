import Command
from Repositorio import Repositorio

class EmprestimoCommand(Command):
    def executar(self, id_usuario, id_livro):
        repositorio = Repositorio()
        usuario = repositorio.get_usuario(id_usuario)
        livro = repositorio.get_livro(id_livro)

        if usuario is None:
            print(f"Usuário com ID {id_usuario} não encontrado.")
            return

        if livro is None:
            print(f"Livro com ID {id_livro} não encontrado.")
            return

        print(f"Livro '{livro.titulo}' emprestado para o usuário '{usuario.nome}'.")