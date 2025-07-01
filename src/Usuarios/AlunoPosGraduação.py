from Usuarios.IUsuario import IUsuario

class AlunoPosGraduacao(IUsuario):
    LIMITE_EMPRESTIMO = 3
    DIAS_EMPRESTIMO = 5
    
    def __init__(self, id, nome):
        super().__init__(id, nome)
        self._limite_emprestimo = self.LIMITE_EMPRESTIMO
        self._dias_emprestimo = self.DIAS_EMPRESTIMO
    
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