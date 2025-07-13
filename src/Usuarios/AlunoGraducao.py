from datetime import datetime, timedelta
from Emprestimo.RegraEmprestimoAluno import RegraEmprestimoAluno
from Usuarios.IUsuario import IUsuario


class AlunoGraduacao(IUsuario):
    LIMITE_EMPRESTIMO = 2
    DIAS_EMPRESTIMO = 4
    
    def __init__(self, id, nome):
        super().__init__(id, nome)
        self._limite_emprestimo = self.LIMITE_EMPRESTIMO
        self._dias_emprestimo = self.DIAS_EMPRESTIMO
        self._regra = RegraEmprestimoAluno(limite_emprestimo=2, dias_emprestimo=4)
        self._historico_emprestimos = []
        self._reservas_ativas = []
    
    def get_id(self):
        return self._id

    def get_tipo_usuario(self):
        return "Aluno Graduação"
    
    def get_nome(self):
        
        return self._nome
    
    def get_esta_devendo(self):
        for emprestimo in self.get_emprestimos_ativos():
            if datetime.now() > emprestimo.get_data_devolucao_prevista():
                return True
        return False
      
    def get_emprestimos_ativos(self):
        ativos = []
        for emp in self._historico_emprestimos:
            if not emp.esta_finalizado():
                ativos.append(emp)
        return ativos
    
    def get_emprestimos(self):
        return self._emprestimos
    
    def get_reservas_ativas(self):
        return self._reservas_ativas
    
    def get_reservas(self):
        return self._reservas
    
    def mudar_situacao_devedor(self):
        self._esta_devendo = not self._esta_devendo

    def adicionar_reserva_ativa(self, reserva):
        self._reservas_ativas.append(reserva)

    def tem_reserva_para_livro(self, livro_a_verificar):
        
        for reserva in self._reservas_ativas:
            if reserva.get_livro().get_id() == livro_a_verificar.get_id():
                return True 
        
        return False 
    
    def adicionar_emprestimo_ativo(self, emprestimo):
        self._historico_emprestimos.append(emprestimo)
   
       
    def remover_reserva_ativa(self, reserva):
        if reserva in self._reservas_ativas:
            self._reservas_ativas.remove(reserva)
        else:
            raise ValueError("Reserva não encontrada nas reservas ativas.")
        
    def remover_emprestimo_ativo(self, emprestimo):
        if emprestimo in self._historico_emprestimos:
            self._historico_emprestimos.remove(emprestimo)
        else:
            raise ValueError("Empréstimo não encontrado nos empréstimos ativos.")           
    
    def get_regra_emprestimo(self):
        return self._regra

    def tem_emprestimo_ativo_do_livro(self, livro_a_verificar):
    
        for emprestimo in self._emprestimos_ativos:
            if emprestimo.get_livro().get_id() == livro_a_verificar.get_id():
                return True 
        
        return False 
    
  
    def get_historico_emprestimos(self):
        return self._historico_emprestimos
