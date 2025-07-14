from datetime import timedelta, datetime

class Emprestimo:
    def __init__(self, id, usuario, livro, exemplar, data_emprestimo, dias_emprestimo):
        self._id = id
        self._usuario = usuario
        self._livro = livro
        self._exemplar = exemplar
        self._data_emprestimo = data_emprestimo
        self._data_devolucao_prevista = data_emprestimo + timedelta(days=dias_emprestimo)
        self._data_devolucao_real = None
        self._finalizado = False


    def finalizar(self): 
        self._data_devolucao_real = datetime.now()
        self._finalizado = True
        
        if self._data_devolucao_real > self._data_devolucao_prevista:
           
            self._usuario.marcar_como_devedor() 
    
    def get_status(self):
        return "Finalizado" if self._finalizado else "Em curso"
        
    def get_livro(self):
        return self._livro

    def get_exemplar(self):
        return self._exemplar
    
    def get_data_emprestimo(self):
        return self._data_emprestimo

    def get_data_devolucao_prevista(self):
        return self._data_devolucao_prevista
    def finalizar(self, data_devolucao_real):
        
        self._data_devolucao_real = data_devolucao_real
        self._finalizado = True

        self._exemplar.devolver()

     
        if self._data_devolucao_real > self._data_devolucao_prevista:
            self._usuario.marcar_como_devedor()

        
        
    def get_data_devolucao_real(self):
        return self._data_devolucao_real
    def get_data_devolucao(self):
        return self._data_devolucao_real if self._data_devolucao_real else self._data_devolucao_prevista
    def get_usuario(self):
        return self._usuario
    def esta_finalizado(self):
       
        return self._finalizado
