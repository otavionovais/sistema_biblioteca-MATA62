# Importe as classes necessárias
from Command.Comando import Command
from Repositorio.repositorio import Repositorio

class ComandoConsultaUsuario(Command):
    def __init__(self, codigo_usuario: str):
        """
        Configura o comando com o código do usuário a ser consultado.
        """
        self.codigo_usuario = codigo_usuario

    def executar(self):
        """
        Executa a consulta e exibe as informações formatadas do usuário no console.
        """
        repositorio = Repositorio()
        usuario = repositorio.buscar_usuario_por_codigo(self.codigo_usuario)

        if usuario is None:
            print(f"Usuário com código {self.codigo_usuario} não encontrado.")
            return

        print(f"--- Consulta de Usuário: {usuario.get_nome()} ---")

        # Exibe a lista de todos os empréstimos, correntes e passados 
        print("\nHistórico de Empréstimos:")
        historico_emprestimos = usuario.get_historico_emprestimos()

        if not historico_emprestimos:
            print("  Nenhum empréstimo no histórico.")
        else:
            for emprestimo in historico_emprestimos:
                # Para cada empréstimo, apresenta o título, data, status e data de devolução [cite: 68]
                titulo_livro = emprestimo.get_livro().get_titulo()
                data_emprestimo = emprestimo.get_data_emprestimo().strftime('%d/%m/%Y')
                status = emprestimo.get_status() # "Em curso" ou "Finalizado"
                
                if status == "Finalizado":
                    data_devolucao = emprestimo.get_data_devolucao_real().strftime('%d/%m/%Y')
                    print(f"  - Livro: '{titulo_livro}'")
                    print(f"    | Emprestado em: {data_emprestimo} | Status: {status} | Devolvido em: {data_devolucao}")
                else: # Em curso
                    data_devolucao_prevista = emprestimo.get_data_devolucao_prevista().strftime('%d/%m/%Y')
                    print(f"  - Livro: '{titulo_livro}'")
                    print(f"    | Emprestado em: {data_emprestimo} | Status: {status} | Devolver até: {data_devolucao_prevista}")

        # Exibe a lista de reservas do usuário 
        print("\nReservas Ativas:")
        reservas_ativas = usuario.get_reservas_ativas()

        if not reservas_ativas:
            print("  Nenhuma reserva ativa.")
        else:
            for reserva in reservas_ativas:
                # Para cada reserva, apresenta o título do livro e a data da solicitação 
                titulo_reservado = reserva.get_livro().get_titulo()
                data_solicitacao = reserva.get_data_solicitacao().strftime('%d/%m/%Y')
                print(f"  - Livro: '{titulo_reservado}' | Reservado em: {data_solicitacao}")