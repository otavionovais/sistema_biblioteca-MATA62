# Importe as classes necessárias
from Command.Comando import Command
from Repositorio.repositorio import Repositorio
from datetime import datetime

from Reserva import Reserva

# Supondo uma fachada para a lógica, como nos exemplos anteriores
facade = ... 

class ComandoReservar(Command):
    def __init__(self, codigo_usuario: str, codigo_livro: str):
        """
        Configura o comando com os códigos necessários para a reserva.
        """
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        """
        Executa a ação de reserva.
        [cite_start]A funcionalidade é descrita na Seção 3.3. [cite: 50]
        """
        # A boa prática é delegar a lógica para uma fachada.
        # Vamos supor que a fachada tenha um método realizar_reserva.
        # resultado = facade.realizar_reserva(self.codigo_usuario, self.codigo_livro)
        
        # Para este exemplo, implementaremos a lógica diretamente aqui para clareza.
        repositorio = Repositorio()
        usuario = repositorio.buscar_usuario_por_codigo(self.codigo_usuario)
        livro = repositorio.buscar_livro_por_codigo(self.codigo_livro)

        if usuario is None:
            print(f"Usuário com código {self.codigo_usuario} não encontrado.")
            return

        if livro is None:
            print(f"Livro com código {self.codigo_livro} não encontrado.")
            return

        # Lógica de negócio (pode ser movida para a fachada)
        # Validação 1: Usuário já não tem um empréstimo ativo do mesmo livro
        if usuario.tem_emprestimo_ativo_do_livro(livro):
            print(f"Não é possível reservar. O usuário '{usuario.get_nome()}' já possui um exemplar deste livro emprestado.")
            return

        # Validação 2: Usuário já não tem uma reserva para este livro
        if usuario.tem_reserva_para_livro(livro):
            print(f"Não é possível reservar. O usuário '{usuario.get_nome()}' já possui uma reserva para este livro.")
            return

        # Se as validações passarem, cria-se a reserva
        # [cite_start]O sistema deve registrar a reserva com a data em que ela foi realizada. [cite: 51]
        data_solicitacao = datetime.now()
        reserva = Reserva(usuario, livro, data_solicitacao)

        # Adiciona a reserva nas listas do usuário e do livro
        usuario.adicionar_reserva_ativa(reserva)
        livro.adicionar_reserva(reserva) # Este método irá disparar as notificações

        print(f"✅ Reserva do livro '{livro.get_titulo()}' realizada com sucesso para o usuário '{usuario.get_nome()}'.")