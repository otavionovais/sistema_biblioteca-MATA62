from Commands import IComando


class ComandoConsultaUsuarios(IComando):
    def __init__(self, id_usuario):
        self._id = id_usuario

    def executar(self):
        # lógica de exibição de dados do usuário
        print("Consultando usuário com ID:", self._id)