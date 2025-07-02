from Usuarios.IUsuario import IUsuario
from Emprestimo.RegraEmprestimoProfessor import RegraEmprestimoProfessor

class Professor(IUsuario):
    def __init__(self, id, nome):
        super().__init__(id, nome)
        self._limite_emprestimo = 5
        self._dias_emprestimo = 8
        self._regra = RegraEmprestimoProfessor()
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
        self._emprestimos_ativos.append(emprestimo) 

    def remover_reserva_ativa(self, reserva):
        if reserva in self._reservas_ativas:
            self._reservas_ativas.remove(reserva)   




