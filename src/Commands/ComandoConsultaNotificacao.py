from Commands import IComando


class ComandoConsultaNotificacao(IComando):
    def __init__(self, notificacao):
        self._notificacao = notificacao

    def executar(self):
        # lógica de exibição de dados do usuário
        print("Consultando usuário com ID:", self._id)