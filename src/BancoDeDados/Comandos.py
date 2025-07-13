from abc import ABC, abstractmethod
from Repositorio.repositorio import Repositorio
from Emprestimo.Emprestimo import Emprestimo
from datetime import datetime
from Reserva.Reserva import Reserva
import sys

class Command(ABC):
    @abstractmethod
    def executar(self):
        pass

class ComandoConsultaUsuario(Command):
    def __init__(self, codigo_usuario: str):
        self.codigo_usuario = codigo_usuario

    def executar(self):
        repositorio = Repositorio()
        usuario = repositorio.buscar_usuario_por_codigo(self.codigo_usuario)

        if usuario is None:
            print(f"Usuário com código {self.codigo_usuario} não encontrado.")
            return

        print(f"--- Consulta de Usuário: {usuario.get_nome()} ---")

        print("\nHistórico de Empréstimos:")
        historico_emprestimos = usuario.get_historico_emprestimos()

        if not historico_emprestimos:
            print("  Nenhum empréstimo no histórico.")
        else:
            for emprestimo in historico_emprestimos:
                titulo_livro = emprestimo.get_livro().get_titulo()
                data_emprestimo = emprestimo.get_data_emprestimo().strftime('%d/%m/%Y')
                status = emprestimo.get_status()
                
                if status == "Finalizado":
                    data_devolucao = emprestimo.get_data_devolucao_real().strftime('%d/%m/%Y')
                    print(f"  - Livro: '{titulo_livro}'")
                    print(f"    | Emprestado em: {data_emprestimo} | Status: {status} | Devolvido em: {data_devolucao}")
                else:
                    data_devolucao_prevista = emprestimo.get_data_devolucao_prevista().strftime('%d/%m/%Y')
                    print(f"  - Livro: '{titulo_livro}'")
                    print(f"    | Emprestado em: {data_emprestimo} | Status: {status} | Devolver até: {data_devolucao_prevista}")

        print("\nReservas Ativas:")
        reservas_ativas = usuario.get_reservas_ativas()

        if not reservas_ativas:
            print("  Nenhuma reserva ativa.")
        else:
            for reserva in reservas_ativas:
                titulo_reservado = reserva.get_livro().get_titulo()
                data_solicitacao = reserva.get_data_solicitacao().strftime('%d/%m/%Y')
                print(f"  - Livro: '{titulo_reservado}' | Reservado em: {data_solicitacao}")

class ComandoConsultaLivros(Command):
    def __init__(self, codigo_livro: str):
        self.codigo_livro = codigo_livro

    def executar(self):
        repositorio = Repositorio()
        livro = repositorio.buscar_livro_por_codigo(self.codigo_livro)

        if livro is None:
            print(f"Livro com código {self.codigo_livro} não encontrado.")
            return

        output = []
        
        output.append(f"Título: {livro.get_titulo()}")

        reservas = livro.get_reservas()
        
        output.append(f"Quantidade de reservas: {len(reservas)}")
        if len(reservas) > 0:
            output.append("Reservado por:")
            for reserva in reservas:
                output.append(f"  - {reserva.get_usuario().get_nome()}")

        output.append("Exemplares:")
        for exemplar in livro.get_exemplares():
            status = "Disponível" if exemplar.esta_disponivel() else "Emprestado"
            output.append(f"  - Código: {exemplar.get_id()} | Status: {status}")

            if not exemplar.esta_disponivel():
                emprestimo_corrente = exemplar.get_emprestimo_corrente()
                if emprestimo_corrente:
                    usuario_emprestimo = emprestimo_corrente.get_usuario()
                    data_emprestimo = emprestimo_corrente.get_data_emprestimo().strftime('%d/%m/%Y')
                    data_devolucao = emprestimo_corrente.get_data_devolucao().strftime('%d/%m/%Y')
                    
                    output.append(f"    | Emprestado para: {usuario_emprestimo.get_nome()}")
                    output.append(f"    | Data do empréstimo: {data_emprestimo}")
                    output.append(f"    | Data para devolução: {data_devolucao}")
        
        print("\n".join(output))

class ComandoConsultaNotificacoes(Command):
    def __init__(self, codigo_usuario: str):
        self.codigo_usuario = codigo_usuario

    def executar(self):
        repositorio = Repositorio()
        usuario = repositorio.buscar_usuario_por_codigo(self.codigo_usuario)

        if usuario is None:
            print(f"Usuário com código {self.codigo_usuario} não encontrado.")
            return

        num_notificacoes = usuario.get_numero_notificacoes()
        
        print(f"O {usuario.get_nome()} recebeu um total de {num_notificacoes} notificações.")

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

        emprestimo_encontrado = None
        for emprestimo in usuario.get_emprestimos_ativos():
            if emprestimo.get_livro().get_id() == livro.get_id():
                emprestimo_encontrado = emprestimo
                break

        if emprestimo_encontrado is None:
            print("Nenhum empréstimo ativo encontrado para esse livro e usuário.")
            return

        data_hoje = datetime.now()
        emprestimo_encontrado.finalizar(data_hoje)

        usuario.remover_emprestimo_ativo(emprestimo_encontrado)

        print("✅ Devolução realizada com sucesso.")

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

        exemplar = next((ex for ex in livro.get_exemplares() if ex.esta_disponivel()), None)

        if exemplar is None:
            print("Não há exemplares disponíveis no momento.")
            return

        data_hoje = datetime.now()
        dias = regra.dias_emprestimo()

        emprestimo = Emprestimo(
            id=len(repositorio._emprestimos) + 1,
            usuario=usuario,
            livro=livro,
            exemplar=exemplar,
            data_emprestimo=data_hoje,
            dias_emprestimo=dias
        )

        exemplar.marcar_emprestado(emprestimo)
        usuario.adicionar_emprestimo_ativo(emprestimo)
        livro.adicionar_emprestimo(emprestimo)
        repositorio.registrar_emprestimo(emprestimo)

        for reserva in livro.get_reservas():
            if reserva.get_usuario() == usuario:
                livro.get_reservas().remove(reserva)
                usuario.remover_reserva_ativa(reserva)
                break

        print("✅ Empréstimo realizado com sucesso!")

class ComandoRegistrarObservador(Command):
    def __init__(self, codigo_usuario: str, codigo_livro: str):
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        repositorio = Repositorio()
        usuario = repositorio.buscar_usuario_por_codigo(self.codigo_usuario)
        livro = repositorio.buscar_livro_por_codigo(self.codigo_livro)

        if usuario is None:
            print(f"Usuário com código {self.codigo_usuario} não encontrado.")
            return

        if livro is None:
            print(f"Livro com código {self.codigo_livro} não encontrado.")
            return

        livro.adicionar_observador(usuario)

        print(f"✅ O usuário '{usuario.get_nome()}' agora é um observador do livro '{livro.get_titulo()}'.")

        facade = ... 

class ComandoReservar(Command):
    def __init__(self, codigo_usuario: str, codigo_livro: str):
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        repositorio = Repositorio()
        usuario = repositorio.buscar_usuario_por_codigo(self.codigo_usuario)
        livro = repositorio.buscar_livro_por_codigo(self.codigo_livro)

        if usuario is None:
            print(f"Usuário com código {self.codigo_usuario} não encontrado.")
            return

        if livro is None:
            print(f"Livro com código {self.codigo_livro} não encontrado.")
            return

        if usuario.tem_emprestimo_ativo_do_livro(livro):
            print(f"Não é possível reservar. O usuário '{usuario.get_nome()}' já possui um exemplar deste livro emprestado.")
            return

        if usuario.tem_reserva_para_livro(livro):
            print(f"Não é possível reservar. O usuário '{usuario.get_nome()}' já possui uma reserva para este livro.")
            return

        data_solicitacao = datetime.now()
        reserva = Reserva(usuario, livro, data_solicitacao)

        usuario.adicionar_reserva_ativa(reserva)
        livro.adicionar_reserva(reserva)

        print(f"✅ Reserva do livro '{livro.get_titulo()}' realizada com sucesso para o usuário '{usuario.get_nome()}'.")

class ComandoSair(Command):
    def __init__(self):
        pass

    def executar(self):
        print("Saindo do sistema de biblioteca...")
        sys.exit(0)