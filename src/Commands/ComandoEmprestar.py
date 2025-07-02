from Commands import IComando


class ComandoEmprestar(IComando):
    def __init__(self, codigo_usuario, codigo_livro):
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        # lógica de empréstimo aqui
        print("Executando empréstimo")