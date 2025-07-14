
from datetime import datetime, timedelta
from Repositorio.repositorio import Repositorio
from Emprestimo import Emprestimo
from Reserva import Reserva

class BibliotecaFacade:
    def __init__(self):
        
        self.repo = Repositorio()

    def realizar_emprestimo(self, codigo_usuario: str, codigo_livro: str) -> str:
        
        usuario = self.repo.buscar_usuario_por_codigo(codigo_usuario)
        livro = self.repo.buscar_livro_por_codigo(codigo_livro)

        if not usuario:
            return f"Erro: Usuário {codigo_usuario} não encontrado."
        if not livro:
            return f"Erro: Livro {codigo_livro} não encontrado."

        regra = usuario.get_regra_emprestimo()
        permitido, motivo = regra.pode_emprestar(usuario, livro)

        if not permitido:
            return f"Não foi possível realizar o empréstimo, pois {motivo}"

        exemplar = livro.obter_exemplar_disponivel()

        if usuario.tem_reserva_para_livro(livro):
            usuario.remover_reserva_para_livro(livro)
            livro.remover_reserva_de_usuario(usuario)
            print(f"INFO: A reserva existente para '{usuario.get_nome()}' foi utilizada para este empréstimo.")
            
        prazo_dias = regra.dias_emprestimo()
        data_emprestimo = datetime.now()
        data_devolucao = data_emprestimo + timedelta(days=prazo_dias)
        
        novo_emprestimo = Emprestimo(usuario, exemplar, data_emprestimo, data_devolucao)
        
        exemplar.emprestar(novo_emprestimo)
        usuario.adicionar_emprestimo(novo_emprestimo)

        return f"✅ Empréstimo do livro '{livro.get_titulo()}' realizado com sucesso para '{usuario.get_nome()}'."

    def realizar_devolucao(self, codigo_usuario: str, codigo_livro: str) -> str:
        
        usuario = self.repo.buscar_usuario_por_codigo(codigo_usuario)
        if not usuario:
            return f"Erro: Usuário {codigo_usuario} não encontrado."
            
        emprestimo_ativo = usuario.buscar_emprestimo_ativo(codigo_livro)
        if not emprestimo_ativo:
            return f"Erro: Nenhum empréstimo ativo do livro {codigo_livro} encontrado para este usuário."
        
        data_hoje = datetime.now()
        emprestimo_ativo.finalizar(data_hoje) 
        
        exemplar = emprestimo_ativo.get_exemplar()
        exemplar.devolver()
        
        return f"✅ Devolução do livro '{emprestimo_ativo.get_livro().get_titulo()}' realizada com sucesso."

    def realizar_reserva(self, codigo_usuario: str, codigo_livro: str) -> str:
        
        usuario = self.repo.buscar_usuario_por_codigo(codigo_usuario)
        livro = self.repo.buscar_livro_por_codigo(codigo_livro)

        if not usuario or not livro:
            return "Erro: Usuário ou Livro não encontrado."
        
        if usuario.tem_emprestimo_ativo_do_livro(livro) or usuario.tem_reserva_para_livro(livro):
            return "Não é possível reservar: o usuário já possui este livro emprestado ou reservado."

        nova_reserva = Reserva(usuario, livro, datetime.now())
        
        usuario.adicionar_reserva(nova_reserva)
        livro.adicionar_reserva(nova_reserva) 

        return f"✅ Reserva para o livro '{livro.get_titulo()}' realizada com sucesso."

    def registrar_observador(self, codigo_usuario: str, codigo_livro: str) -> str:
        
        observador = self.repo.buscar_usuario_por_codigo(codigo_usuario)
        livro = self.repo.buscar_livro_por_codigo(codigo_livro)
        
        if not observador or not livro:
            return "Erro: Usuário ou Livro não encontrado."
            
        livro.adicionar_observador(observador)
        return f"✅ Usuário '{observador.get_nome()}' agora é um observador do livro '{livro.get_titulo()}'."

    def consultar_livro(self, codigo_livro: str) -> str:
      
        livro = self.repo.buscar_livro_por_codigo(codigo_livro)
        if not livro:
            return f"Erro: Livro {codigo_livro} não encontrado."
        
        output = [f"Título: {livro.get_titulo()}"] 
        output.append(f"Reservas: {livro.get_numero_reservas()}") 
        
        if livro.get_numero_reservas() > 0:
            for reserva in livro.get_reservas():
                output.append(f"  - {reserva.get_usuario().get_nome()}") 

        output.append("Exemplares:")
        for exemplar in livro.get_exemplares():
            status = "Disponível" if exemplar.esta_disponivel() else "Emprestado"
            output.append(f"  - Código: {exemplar.get_id()} | Status: {status}") 
            if not exemplar.esta_disponivel():
                emp = exemplar.get_emprestimo_corrente()
                output.append(f"    | Emprestado para: {emp.get_usuario().get_nome()}") 
                output.append(f"    | Data Empréstimo: {emp.get_data_emprestimo().strftime('%d/%m/%Y')}") 
                output.append(f"    | Data Devolução: {emp.get_data_devolucao().strftime('%d/%m/%Y')}") 
        
        return "\n".join(output)

    def consultar_usuario(self, codigo_usuario: str) -> str:
       
        usuario = self.repo.buscar_usuario_por_codigo(codigo_usuario)
        if not usuario:
            return f"Erro: Usuário {codigo_usuario} não encontrado."

        output = [f"--- Consulta de Usuário: {usuario.get_nome()} ---"]
        
        output.append("\nHistórico de Empréstimos:")
        emprestimos = usuario.get_historico_emprestimos()
        if not emprestimos:
            output.append("  Nenhum empréstimo no histórico.")
        else:
            for emp in emprestimos:
                output.append(f"  - Livro: '{emp.get_livro().get_titulo()}'") 
                output.append(f"    | Emprestado em: {emp.get_data_emprestimo().strftime('%d/%m/%Y')} | Status: {emp.get_status()}") 

        output.append("\nReservas Ativas:")
        reservas = usuario.get_reservas_ativas()
        if not reservas:
            output.append("  Nenhuma reserva ativa.")
        else:
            for res in reservas:
                output.append(f"  - Livro: '{res.get_livro().get_titulo()}' | Reservado em: {res.get_data_solicitacao().strftime('%d/%m/%Y')}") 

        return "\n".join(output)

    def consultar_notificacoes(self, codigo_usuario: str) -> str:
        
        usuario = self.repo.buscar_usuario_por_codigo(codigo_usuario)
        if not usuario:
            return f"Erro: Usuário {codigo_usuario} não encontrado."
            
        num_notificacoes = usuario.get_numero_notificacoes()
        return f"O usuário {usuario.get_nome()} recebeu {num_notificacoes} notificações." 
