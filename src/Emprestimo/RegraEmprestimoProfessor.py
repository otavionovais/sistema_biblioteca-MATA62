from Emprestimo.RegraEmprestimos import IRegraEmprestimos

class RegraEmprestimoProfessor(IRegraEmprestimos):
    def __init__(self):
        self._dias = 8  
    def pode_emprestar(self, usuario, livro):
        if livro.qtd_exemplares_disponiveis() <= 0:
            return False, "Não há exemplares disponíveis para empréstimo."

        if usuario.get_esta_devendo():
            return False, "Professor está com pendências e não pode realizar empréstimos."

        return True, None

    def dias_emprestimo(self):
        return self._dias
