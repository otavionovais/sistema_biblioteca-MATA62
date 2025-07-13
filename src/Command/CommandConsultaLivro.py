# Importe as classes necessárias
from Command.Comando import Command
from Repositorio.repositorio import Repositorio

class ComandoConsultaLivros(Command):
    def __init__(self, codigo_livro: str):
        """
        Configura o comando com o código do livro a ser consultado.
        """
        self.codigo_livro = codigo_livro

    def executar(self):
        """
        Executa a consulta e exibe as informações formatadas no console.
        """
        repositorio = Repositorio()
        livro = repositorio.buscar_livro_por_codigo(self.codigo_livro)

        if livro is None:
            print(f"Livro com código {self.codigo_livro} não encontrado.")
            return

        # Monta a string de saída com base nos requisitos
        output = []
        
        # (i) Título do livro [cite: 62]
        output.append(f"Título: {livro.get_titulo()}")

        reservas = livro.get_reservas()
        
        # (ii) Quantidade de reservas e nomes dos usuários [cite: 62]
        output.append(f"Quantidade de reservas: {len(reservas)}")
        if len(reservas) > 0:
            output.append("Reservado por:")
            for reserva in reservas:
                output.append(f"  - {reserva.get_usuario().get_nome()}")

        # (iii) Informações de cada exemplar [cite: 62]
        output.append("Exemplares:")
        for exemplar in livro.get_exemplares():
            status = "Disponível" if exemplar.esta_disponivel() else "Emprestado"
            output.append(f"  - Código: {exemplar.get_codigo()} | Status: {status}")

            # Se o exemplar está emprestado, exibe os detalhes do empréstimo corrente [cite: 63]
            if not exemplar.esta_disponivel():
                emprestimo_corrente = exemplar.get_emprestimo_corrente()
                if emprestimo_corrente:
                    usuario_emprestimo = emprestimo_corrente.get_usuario()
                    data_emprestimo = emprestimo_corrente.get_data_emprestimo().strftime('%d/%m/%Y')
                    data_devolucao = emprestimo_corrente.get_data_devolucao().strftime('%d/%m/%Y')
                    
                    output.append(f"    | Emprestado para: {usuario_emprestimo.get_nome()}")
                    output.append(f"    | Data do empréstimo: {data_emprestimo}")
                    output.append(f"    | Data para devolução: {data_devolucao}")
        
        # Imprime o resultado final formatado
        print("\n".join(output))