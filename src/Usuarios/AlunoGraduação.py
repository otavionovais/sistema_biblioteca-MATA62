from datetime import datetime, timedelta
from Usuarios.IUsuario import IUsuario


class AlunoGraduação(IUsuario):
    LIMITE_EMPRESTIMO = 2
    DIAS_EMPRESTIMO = 4
    
    def __init__(self, id, nome):
        super().__init__(id, nome)
        self._limite_emprestimo = self.LIMITE_EMPRESTIMO
        self._dias_emprestimo = self.DIAS_EMPRESTIMO
        self._regra = RegraEmprestimoAluno(limite_emprestimos=2, dias_emprestimo=4)
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_esta_devendo(self):
        return self._esta_devendo 
      
    def get_emprestimos_ativos(self):
        return self._emprestimos_ativos
    
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

       if len(self._emprestimos_ativos) < self._limite_emprestimo:
           self._emprestimos_ativos.append(emprestimo)
       else:
            raise ValueError("Limite de empréstimos ativos atingido.")
       
    def remover_reserva_ativa(self, reserva):
        if reserva in self._reservas_ativas:
            self._reservas_ativas.remove(reserva)
        else:
            raise ValueError("Reserva não encontrada nas reservas ativas.")
        
    def remover_emprestimo_ativo(self, emprestimo):
        if emprestimo in self._emprestimos_ativos:
            self._emprestimos_ativos.remove(emprestimo)
        else:
            raise ValueError("Empréstimo não encontrado nos empréstimos ativos.")           
   