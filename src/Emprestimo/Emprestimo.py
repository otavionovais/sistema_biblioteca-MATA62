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

        # A linha abaixo foi REMOVIDA. A responsabilidade de chamar este método
        # é do ComandoEmprestar ou da BibliotecaFacade.
        # self._exemplar.marcar_emprestado() 

    def finalizar(self): # Nome alterado para maior clareza
        """Finaliza o empréstimo, registrando a data de devolução."""
        self._data_devolucao_real = datetime.now()
        self._finalizado = True
        
        # O método agora apenas verifica se o usuário deve ser marcado como devedor.
        if self._data_devolucao_real > self._data_devolucao_prevista:
            # É mais seguro ter um método que apenas marca como devedor,
            # em vez de um que inverte o status.
            self._usuario.marcar_como_devedor() 
    
    # --- Métodos "getter" para acessar as informações ---
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
        """
        Finaliza o empréstimo, marcando-o como devolvido na data especificada.
        Esta função é o coração da operação de devolução.
        """
        # 1. Registra a data em que a devolução foi feita
        self._data_devolucao_real = data_devolucao_real
        self._finalizado = True

        # 2. Libera o exemplar, que agora está disponível novamente
        self._exemplar.devolver()

        # 3. Verifica se a devolução está em atraso para marcar o usuário como "devedor".
        # [cite_start]Esta é a implementação da regra de negócio das Seções 3.1.1 e 3.1.1. [cite: 32, 42]
        if self._data_devolucao_real > self._data_devolucao_prevista:
            self._usuario.marcar_como_devedor()

        
        
    def get_data_devolucao_real(self):
        return self._data_devolucao_real
    def get_data_devolucao(self):
        """Retorna a data de devolução real ou prevista."""
        return self._data_devolucao_real if self._data_devolucao_real else self._data_devolucao_prevista
    def get_usuario(self):
        return self._usuario
    def esta_finalizado(self):
        """
        Retorna True se o empréstimo foi finalizado (devolvido),
        e False caso contrário.
        """
        return self._finalizado