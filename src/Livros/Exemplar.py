class Exemplar:
    def __init__(self, id, livro_pai): 
        self._id = id
        self._livro_pai = livro_pai     
        self._disponivel = True
        self._emprestimo_corrente = None 
        
    def get_id(self):
        return self._id

    def get_livro(self):
        return self._livro_pai

    def esta_disponivel(self):
        return self._disponivel

    def marcar_emprestado(self, emprestimo):
        if not self._disponivel:
            raise Exception("Exemplar não está disponível.")
        self._disponivel = False
        self._emprestimo_corrente = emprestimo 
   

    def devolver(self): 
        self._disponivel = True
        self._emprestimo_corrente = None 
        
    def get_emprestimo_corrente(self):
        return self._emprestimo_corrente
