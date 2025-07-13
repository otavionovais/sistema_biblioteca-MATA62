from datetime import datetime
from Command.Comando import Command
from Emprestimo import Emprestimo
from Repositorio.repositorio import Repositorio

class ComandoEmprestar(Command):
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

        regra = usuario.get_regra_emprestimo()
        permitido, motivo = regra.pode_emprestar(usuario, livro)

        if not permitido:
            print(f"Empréstimo não permitido: {motivo}")
            return

        # Pega o primeiro exemplar disponível
        exemplar = next((ex for ex in livro.get_exemplares() if ex.esta_disponivel()), None)

        if exemplar is None:
            print("Não há exemplares disponíveis no momento.")
            return

        # Calcula datas
        data_hoje = datetime.now()
        dias = regra.dias_emprestimo()

        # Cria o empréstimo
        emprestimo = Emprestimo(
            id=len(repositorio.emprestimos) + 1,
            usuario=usuario,
            livro=livro,
            exemplar=exemplar,
            data_emprestimo=data_hoje,
            dias_emprestimo=dias
        )

        # Atualiza o estado
        exemplar.marcar_emprestado()
        usuario.adicionar_emprestimo_ativo(emprestimo)
        livro.adicionar_emprestimo(emprestimo)
        repositorio.registrar_emprestimo(emprestimo)

        # Remove reserva se existir
        for reserva in livro.get_reservas():
            if reserva.get_usuario() == usuario:
                livro.get_reservas().remove(reserva)
                usuario.remover_reserva_ativa(reserva)
                break

        print("✅ Empréstimo realizado com sucesso!")
