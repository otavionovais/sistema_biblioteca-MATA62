# Gerenciadores.py

from datetime import datetime
from Repositorio.repositorio import Repositorio
from Emprestimo.Emprestimo import Emprestimo
from Reserva.Reserva import Reserva

class GerenciadorDeEmprestimos:
    """Gerencia a lógica de negócio para empréstimos e devoluções."""
    def __init__(self, repositorio: Repositorio):
        self.repositorio = repositorio

    def emprestar_livro(self, codigo_usuario: str, codigo_livro: str) -> str:
        usuario = self.repositorio.buscar_usuario_por_codigo(codigo_usuario)
        if not usuario:
            return f"Usuário {codigo_usuario} não encontrado."

        livro = self.repositorio.buscar_livro_por_codigo(codigo_livro)
        if not livro:
            return f"Livro {codigo_livro} não encontrado."

        regra = usuario.get_regra_emprestimo()
        permitido, motivo = regra.pode_emprestar(usuario, livro)
        if not permitido:
            return f"Empréstimo não permitido: {motivo}"

        exemplar = next((ex for ex in livro.get_exemplares() if ex.esta_disponivel()), None)
        if not exemplar:
            return "Não há exemplares disponíveis no momento."

        emprestimo = Emprestimo(
            id=len(self.repositorio._emprestimos) + 1,
            usuario=usuario,
            livro=livro,
            exemplar=exemplar,
            data_emprestimo=datetime.now(),
            dias_emprestimo=regra.dias_emprestimo()
        )

        exemplar.marcar_emprestado(emprestimo)
        usuario.adicionar_emprestimo_ativo(emprestimo)
        livro.adicionar_emprestimo(emprestimo)
        self.repositorio.registrar_emprestimo(emprestimo)

        for reserva in livro.get_reservas():
            if reserva.get_usuario() == usuario:
                livro.get_reservas().remove(reserva)
                usuario.remover_reserva_ativa(reserva)
                break
        
        return "✅ Empréstimo realizado com sucesso!"

    def devolver_livro(self, codigo_usuario: str, codigo_livro: str) -> str:
        usuario = self.repositorio.buscar_usuario_por_codigo(codigo_usuario)
        if not usuario:
            return f"Usuário {codigo_usuario} não encontrado."

        livro = self.repositorio.buscar_livro_por_codigo(codigo_livro)
        if not livro:
            return f"Livro {codigo_livro} não encontrado."

        emprestimo_encontrado = next((emp for emp in usuario.get_emprestimos_ativos() if emp.get_livro().get_id() == livro.get_id()), None)
        if not emprestimo_encontrado:
            return "Nenhum empréstimo ativo encontrado para esse livro e usuário."

        emprestimo_encontrado.finalizar(datetime.now())
        usuario.remover_emprestimo_ativo(emprestimo_encontrado)
        return "✅ Devolução realizada com sucesso."


class GerenciadorDeInteracoes:
    """Gerencia reservas e registros de observadores."""
    def __init__(self, repositorio):
        # CORREÇÃO: Armazena o repositório como um atributo de instância.
        self.repositorio = repositorio

    def reservar_livro(self, codigo_usuario: str, codigo_livro: str) -> str:
        # CORREÇÃO: Usa 'self.repositorio' para acessar os métodos.
        usuario = self.repositorio.buscar_usuario_por_codigo(codigo_usuario)
        if not usuario:
            return f"Usuário com código {codigo_usuario} não encontrado."

        livro = self.repositorio.buscar_livro_por_codigo(codigo_livro)
        if not livro:
            return f"Livro com código {codigo_livro} não encontrado."

        if usuario.tem_emprestimo_ativo_do_livro(livro):
            return f"Não é possível reservar. O usuário '{usuario.get_nome()}' já possui um exemplar deste livro emprestado."

        if usuario.tem_reserva_para_livro(livro):
            return f"Não é possível reservar. O usuário '{usuario.get_nome()}' já possui uma reserva para este livro."

        reserva = Reserva(usuario, livro, datetime.now())
        usuario.adicionar_reserva_ativa(reserva)
        livro.adicionar_reserva(reserva)
        return f"✅ Reserva do livro '{livro.get_titulo()}' realizada com sucesso para o usuário '{usuario.get_nome()}'."

    def registrar_observador(self, codigo_usuario: str, codigo_livro: str) -> str:
        # CORREÇÃO: Usa 'self.repositorio' para acessar os métodos.
        usuario = self.repositorio.buscar_usuario_por_codigo(codigo_usuario)
        if not usuario:
            return f"Usuário com código {codigo_usuario} não encontrado."

        livro = self.repositorio.buscar_livro_por_codigo(codigo_livro)
        if not livro:
            return f"Livro com código {codigo_livro} não encontrado."

        livro.adicionar_observador(usuario)
        return f"✅ O usuário '{usuario.get_nome()}' agora é um observador do livro '{livro.get_titulo()}'."


class GerenciadorDeConsultas:
    """Gerencia a formatação e exibição de informações do sistema."""
    def __init__(self, repositorio: Repositorio):
        self.repositorio = repositorio

    def consultar_usuario(self, codigo_usuario: str) -> str:
        usuario = self.repositorio.buscar_usuario_por_codigo(codigo_usuario)
        def __init__(self, repositorio: Repositorio):
            self.repositorio = repositorio
        
        output = [f"--- Consulta de Usuário: {usuario.get_nome()} ---"]
        output.append("\nHistórico de Empréstimos:")
        if not usuario.get_historico_emprestimos():
            output.append("  Nenhum empréstimo no histórico.")
        else:
            for emp in usuario.get_historico_emprestimos():
                output.append(f"  - Livro: '{emp.get_livro().get_titulo()}'")
                if emp.get_status() == "Finalizado":
                    output.append(f"    | Emprestado em: {emp.get_data_emprestimo():%d/%m/%Y} | Status: {emp.get_status()} | Devolvido em: {emp.get_data_devolucao_real():%d/%m/%Y}")
                else:
                    output.append(f"    | Emprestado em: {emp.get_data_emprestimo():%d/%m/%Y} | Status: {emp.get_status()} | Devolver até: {emp.get_data_devolucao_prevista():%d/%m/%Y}")

        output.append("\nReservas Ativas:")
        if not usuario.get_reservas_ativas():
            output.append("  Nenhuma reserva ativa.")
        else:
            for res in usuario.get_reservas_ativas():
                output.append(f"  - Livro: '{res.get_livro().get_titulo()}' | Reservado em: {res.get_data_solicitacao():%d/%m/%Y}")
        return "\n".join(output)

    def consultar_livro(self, codigo_livro: str) -> str:
        livro = self.repositorio.buscar_livro_por_codigo(codigo_livro)
        if not livro:
            return f"Livro com código {codigo_livro} não encontrado."

        output = [f"Título: {livro.get_titulo()}"]
        reservas = livro.get_reservas()
        output.append(f"Quantidade de reservas: {len(reservas)}")
        if len(reservas) > 0:
            output.append("Reservado por:")
            for res in reservas:
                output.append(f"  - {res.get_usuario().get_nome()}")

        output.append("\nExemplares:")
        for ex in livro.get_exemplares():
            status = "Disponível" if ex.esta_disponivel() else "Emprestado"
            output.append(f"  - Código: {ex.get_id()} | Status: {status}")
            if not ex.esta_disponivel() and ex.get_emprestimo_corrente():
                emp = ex.get_emprestimo_corrente()
                output.append(f"    | Emprestado para: {emp.get_usuario().get_nome()}")
                output.append(f"    | Data do empréstimo: {emp.get_data_emprestimo():%d/%m/%Y}")
                output.append(f"    | Data para devolução: {emp.get_data_devolucao_prevista():%d/%m/%Y}")
        return "\n".join(output)

    def consultar_notificacoes(self, codigo_usuario: str) -> str:
        """
        Consulta o número total de notificações que um usuário recebeu.
        Esta é a implementação da funcionalidade 'ntf'.
        """
        usuario = self.repositorio.buscar_usuario_por_codigo(codigo_usuario)
        if not usuario:
            return f"Usuário com código {codigo_usuario} não encontrado."

        # Supondo que a classe Usuario tenha o método 'get_numero_notificacoes'
        try:
            num_notificacoes = usuario.get_numero_notificacoes()
            return f"O usuário {usuario.get_nome()} recebeu um total de {num_notificacoes} notificações."
        except AttributeError:
            return f"Erro: O usuário {usuario.get_nome()} não tem a capacidade de receber notificações."
            