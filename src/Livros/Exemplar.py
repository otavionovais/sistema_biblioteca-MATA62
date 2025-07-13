class Exemplar:
    def __init__(self, id, livro_pai): # <-- 1. Adicionado o parâmetro 'livro_pai'
        self._id = id
        self._livro_pai = livro_pai     # <-- 2. Armazenado o objeto Livro
        self._disponivel = True
        self._emprestimo_corrente = None # Necessário para a consulta de livros

    def get_id(self):
        return self._id

    def get_livro(self):
        """ Retorna o objeto Livro ao qual este exemplar pertence. """
        return self._livro_pai

    def esta_disponivel(self):
        return self._disponivel

    def marcar_emprestado(self, emprestimo):
        if not self._disponivel:
            raise Exception("Exemplar não está disponível.")
        self._disponivel = False
        self._emprestimo_corrente = emprestimo # Armazena o empréstimo atual
   

    def devolver(self): # Nome alterado para maior clareza
        self._disponivel = True
        self._emprestimo_corrente = None # Limpa a referência ao empréstimo

    def get_emprestimo_corrente(self):
        return self._emprestimo_corrente