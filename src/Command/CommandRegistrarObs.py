# Importe as classes necessárias
from Command.Comando import Command
from Repositorio.repositorio import Repositorio

class ComandoRegistrarObservador(Command):
    def __init__(self, codigo_usuario: str, codigo_livro: str):
        """
        Configura o comando com os códigos do usuário (observador) e do livro (sujeito).
        """
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        """
        Executa a ação de registrar o usuário como observador do livro.
        Esta funcionalidade é descrita na Seção 3.4.
        """
        repositorio = Repositorio()
        usuario = repositorio.buscar_usuario_por_codigo(self.codigo_usuario)
        livro = repositorio.buscar_livro_por_codigo(self.codigo_livro)

        if usuario is None:
            print(f"Usuário com código {self.codigo_usuario} não encontrado.")
            return

        if livro is None:
            print(f"Livro com código {self.codigo_livro} não encontrado.")
            return

        # A lógica principal é simplesmente adicionar o usuário à lista de observadores do livro.
        # O documento especifica que não é preciso validar se o usuário é de fato um professor[cite: 58].
        livro.adicionar_observador(usuario)

        print(f"✅ O usuário '{usuario.get_nome()}' agora é um observador do livro '{livro.get_titulo()}'.")