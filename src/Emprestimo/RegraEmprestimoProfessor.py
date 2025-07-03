from IRegraEmprestimos import IRegraEmprestimos

class RegraEmprestimoProfessor(IRegraEmprestimos):
    def __init__(self):
        self._dias = 8  # prazo fixo para professores

    def pode_emprestar(self, usuario, livro):
        # 1. Há exemplares disponíveis?
        if livro.qtd_exemplares_disponiveis() <= 0:
            return False, "Não há exemplares disponíveis para empréstimo."

        # 2. Usuário está devendo?
        if usuario.get_esta_devendo():
            return False, "Professor está com pendências e não pode realizar empréstimos."

        # Professores não têm limite de livros nem restrição por reserva
        return True, None

    def dias_emprestimo(self):
        return self._dias
