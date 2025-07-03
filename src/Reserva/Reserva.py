class Reserva:
    def __init__(self, usuario, livro, data_reserva=None):
        self._usuario = usuario
        self._livro = livro
        self._data_reserva = data_reserva 

    def get_usuario(self):
        return self._usuario

    def get_livro(self):
        return self._livro

    def get_data_reserva(self):
        return self._data_reserva

    def get_info(self):
        return {
            "Usuário": self._usuario.get_nome(),
            "Livro": self._livro.get_titulo(),
            "Data da reserva": self._data_reserva.strftime('%d/%m/%Y'),
        }
