from Emprestimo.RegraEmprestimoAlunoPos import RegraEmprestimoAlunoPos
from Usuarios.IUsuario import IUsuario

class AlunoPosGraduacao(IUsuario):
    LIMITE_EMPRESTIMO = 3
    DIAS_EMPRESTIMO = 5
    
    def __init__(self, id, nome):
        super().__init__(id, nome)
        self._limite_emprestimo = self.LIMITE_EMPRESTIMO
        self._dias_emprestimo = self.DIAS_EMPRESTIMO
        self._regra = RegraEmprestimoAlunoPos(limite_emprestimo=3, dias_emprestimo=5)
        self._historico_emprestimos = []

    def get_id(self):
        return self._id
    def get_tipo_usuario(self):
        return "Aluno PosGraduação"
    
    def get_nome(self):
        return self._nome
    
    def get_esta_devendo(self):
        return self._esta_devendo 
    
    def get_emprestimos_ativos(self):
        return self._historico_emprestimos
    
    def get_emprestimos(self):
        return self._emprestimos
    
    def get_reservas_ativas(self):
        return self._reservas_ativas
    def get_historico_emprestimos(self):
        return self._historico_emprestimos
    
    def get_reservas(self):
        return self._reservas
    
    def mudar_situacao_devedor(self):
        self._esta_devendo = not self._esta_devendo
    
    def adicionar_reserva_ativa(self, reserva):
        self._reservas_ativas.append(reserva)

    def adicionar_emprestimo_ativo(self, emprestimo):
        if len(self._historico_emprestimos) < self._limite_emprestimo:
            self._historico_emprestimos.append(emprestimo)
        else:
            raise ValueError("Limite de empréstimos ativos atingido.")
    def remover_reserva_ativa(self, reserva):
        if reserva in self._reservas_ativas:
            self._reservas_ativas.remove(reserva)
        else:
            raise ValueError("Reserva não encontrada nas reservas ativas.") 
        
    def remover_emprestimo_ativo(self, emprestimo):
        if emprestimo in self._historico_emprestimos:
            self._historico_emprestimos.remove(emprestimo)
        else:
            raise ValueError("Empréstimo não encontrado nas reservas ativas.")
    def get_regra_emprestimo(self):
        return self._regra
    def tem_emprestimo_ativo(self):
        return len(self._historico_emprestimos) > 0
    def tem_emprestimo_ativo_do_livro(self, livro_a_verificar):
    
        for emprestimo in self._emprestimos_ativos:
            if emprestimo.get_livro().get_id() == livro_a_verificar.get_id():
                return True 
        
        return False 

    def tem_reserva_para_livro(self, livro_a_verificar):
        
        for reserva in self._reservas_ativas:
            if reserva.get_livro().get_id() == livro_a_verificar.get_id():
                return True 
        
        return False 
    