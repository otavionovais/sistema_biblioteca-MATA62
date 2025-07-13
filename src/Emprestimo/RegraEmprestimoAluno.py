from Emprestimo.RegraEmprestimos import IRegraEmprestimos

from Livros.Livro import Livro as livro

class RegraEmprestimoAluno(IRegraEmprestimos):
    def __init__(self, limite_emprestimo, dias_emprestimo):
        self._limite = limite_emprestimo
        self._dias = dias_emprestimo

    def pode_emprestar(self, usuario, livro):
        if usuario.tem_emprestimo_ativo_do_livro(livro):
            # Exemplo de mensagem do documento [cite: 46]
            motivo = "o usuário já tem um exemplar deste mesmo livro em empréstimo no momento."
            return (False, motivo)

        # Regra 3: Limite de empréstimos em aberto (2 para graduação) [cite: 33, 37]
        if len(usuario.get_emprestimos_ativos()) >= 2: # Supondo 2 para graduação
            motivo = "o usuário atingiu o seu limite de empréstimos."
            return (False, motivo)
            
        # Regra 2: Usuário não pode ser devedor [cite: 32]
        if usuario.esta_devedor():
            motivo = "o usuário está em débito (possui livros em atraso)."
            return (False, motivo)

        #  Há exemplares disponíveis do livro?

        if livro.qtd_exemplares_disponiveis() == 0:
            return False, "Livro não disponível"
        
        # O usuário não estiver “devedor” com livros em atraso

        if usuario.get_esta_devendo():
            return False, "Usuário está devendo"
        
        # Atingiu o limite de empréstimos ativos?
        if len(usuario.get_emprestimos_ativos()) >= self._limite:
            return False, "Limite de empréstimos atingido"
        
        # O livro já possui emprestimo
        for emprestimo in usuario.get_emprestimos_ativos():
            if emprestimo.get_livro().get_id() == livro.get_id():
                return False, "Livro já emprestado para o usuário"
        
        # Quantidades de reservas e disponibilidade

        tem_reserva = livro.usuario_tem_reserva(usuario)
        qtd_reservas = len(livro.get_reservas())
        qtd_disponiveis = livro.qtd_exemplares_disponiveis()

        if not tem_reserva and qtd_reservas >= qtd_disponiveis  :
            return False, "Livro reservado por outro usuário"
        return (True, "Empréstimo permitido.")
    
    def prazo_emprestimo(self):
        return self._dias
