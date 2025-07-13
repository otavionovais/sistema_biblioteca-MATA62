from Command.Comando import Command
from datetime import datetime

from Repositorio.repositorio import Repositorio

class ComandoDevolver(Command):
    def __init__(self, codigo_usuario, codigo_livro):
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        repositorio = Repositorio()

        usuario = repositorio.buscar_usuario_por_codigo(self.codigo_usuario)
        livro = repositorio.buscar_livro_por_codigo(self.codigo_livro)

        if usuario is None:
            print(f"Usuário {self.codigo_usuario} não encontrado.")
            return

        if livro is None:
            print(f"Livro {self.codigo_livro} não encontrado.")
            return

        # Encontra o empréstimo ativo do usuário para esse livro
        emprestimo_encontrado = None
        for emprestimo in usuario.get_emprestimos_ativos():
            if emprestimo.get_livro().get_id() == livro.get_id():
                emprestimo_encontrado = emprestimo
                break

        if emprestimo_encontrado is None:
            print("Nenhum empréstimo ativo encontrado para esse livro e usuário.")
            return

        # Marcar como devolvido
        data_hoje = datetime.now()
        emprestimo_encontrado.marcar_como_devolvido(data_hoje)

        # Remover dos empréstimos ativos
        usuario.remover_emprestimo_ativo(emprestimo_encontrado)

        print("✅ Devolução realizada com sucesso.")
