# Importe as classes necessárias
from Command.Comando import Command
from Repositorio.repositorio import Repositorio

class ComandoConsultaNotificacoes(Command):
    def __init__(self, codigo_usuario: str):
        """
        Configura o comando com o código do usuário (observador) a ser consultado.
        """
        self.codigo_usuario = codigo_usuario

    def executar(self):
        """
        Busca o usuário e exibe o número total de notificações que ele recebeu.
        """
        repositorio = Repositorio()
        usuario = repositorio.buscar_usuario_por_codigo(self.codigo_usuario)

        if usuario is None:
            print(f"Usuário com código {self.codigo_usuario} não encontrado.")
            return

        # [cite_start]Conforme a Seção 3.7, o sistema deve retornar o número total de vezes que o usuário foi notificado. [cite: 72]
        # [cite_start]O documento também especifica que não é preciso validar se o usuário é um professor. [cite: 74]
        num_notificacoes = usuario.get_numero_notificacoes()
        
        print(f"O usuário {usuario.get_nome()} recebeu um total de {num_notificacoes} notificações.")