from Emprestimo.RegraEmprestimos import IRegraEmprestimos

from Livros.Livro import Livro as livro

class RegraEmprestimoAlunoPos(IRegraEmprestimos):
    def __init__(self, limite_emprestimo, dias_emprestimo):
        self._limite = limite_emprestimo
        self._dias = dias_emprestimo

    def pode_emprestar(self, usuario, livro):
        if usuario.tem_emprestimo_ativo_do_livro(livro):
            motivo = "o usuário já tem um exemplar deste mesmo livro em empréstimo no momento."
            return (False, motivo)

        if len(usuario.get_emprestimos_ativos()) >= 3: 
            motivo = "o usuário atingiu o seu limite de empréstimos."
            return (False, motivo)
            
        if usuario.get_esta_devendo():
            motivo = "o usuário está em débito (possui livros em atraso)."
            return (False, motivo)


        if livro.qtd_exemplares_disponiveis() == 0:
            return False, "Livro não disponível"
        

        if usuario.get_esta_devendo():
            return False, "Usuário está devendo"
        
        if len(usuario.get_emprestimos_ativos()) >= self._limite:
            return False, "Limite de empréstimos atingido"
        
        for emprestimo in usuario.get_emprestimos_ativos():
            if emprestimo.get_livro().get_id() == livro.get_id():
                return False, "Livro já emprestado para o usuário"
        

        tem_reserva = livro.usuario_tem_reserva(usuario)
        qtd_reservas = len(livro.get_reservas())
        qtd_disponiveis = livro.qtd_exemplares_disponiveis()

        if not tem_reserva and qtd_reservas >= qtd_disponiveis  :
            return False, "Livro reservado por outro usuário"
        return (True, "Empréstimo permitido.")
    
    def dias_emprestimo(self):
        return self._dias
