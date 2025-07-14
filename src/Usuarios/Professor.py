from Usuarios.IUsuario import IUsuario
from Emprestimo.RegraEmprestimoProfessor import RegraEmprestimoProfessor

class Professor(IUsuario):
    def __init__(self, id, nome):
        super().__init__(id, nome)
        self._limite_emprestimo = 5
        self._dias_emprestimo = 8
        self._notificacoes = 0
        self._regra = RegraEmprestimoProfessor()
        self._historico_emprestimos = []

    def get_id(self):
        return self._id
    
    def get_tipo_usuario(self):
        return "Professor"
    
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
        
    def get_reservas(self):
        return self._reservas
    
    def mudar_situacao_devedor(self):
        self._esta_devendo = not self._esta_devendo

    def adicionar_reserva_ativa(self, reserva):
        self._reservas_ativas.append(reserva)

    def adicionar_emprestimo_ativo(self, emprestimo):
        self._historico_emprestimos.append(emprestimo) 

    def remover_reserva_ativa(self, reserva):
        if reserva in self._reservas_ativas:
            self._reservas_ativas.remove(reserva)   
            
    def notificar(self, livro):
        self._notificacoes += 1
        
    def get_numero_notificacoes(self):
        return self._notificacoes
    
    def remover_emprestimo_ativo(self, emprestimo):
        if emprestimo in self._historico_emprestimos:
            self._historico_emprestimos.remove(emprestimo)
        else:
            raise ValueError("Empréstimo não encontrado nos empréstimos ativos.") 
        
    def get_regra_emprestimo(self):
        return self._regra
    
    def tem_emprestimo_ativo(self):
        return len(self._historico_emprestimos) > 0
    
    def tem_reserva_para_livro(self, livro_a_verificar):
       
        for reserva in self._reservas_ativas:
            if reserva.get_livro().get_id() == livro_a_verificar.get_id():
                return True 
        
        return False 

    def tem_emprestimo_ativo_do_livro(self, livro_a_verificar):
    
        for emprestimo in self._emprestimos_ativos:
            if emprestimo.get_livro().get_id() == livro_a_verificar.get_id():
                return True 
        
        return False 
    
    def get_historico_emprestimos(self):
        return self._historico_emprestimos


