class Repositorio:
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Repositorio, cls).__new__(cls)
            print("Repositório criado com sucesso!")
        else:
            print("Repositório já existe!")
        return cls._instance
    
    def __init__(self, usuarios, livros):
        if not hasattr(self, '_inicializado'):
            self._inicializado = True
            self._usuarios = usuarios
            self._livros = livros
            print("Repositório inicializado com sucesso!")

    def get_usuario(self, id_usuario):
        for usuario in self._usuarios:
            if usuario.get_id() == id_usuario:
                return usuario
        return None
    
    def get_livro(self, id_livro):
        for livro in self._livros:
            if livro.get_id() == id_livro:
                return livro
        return None