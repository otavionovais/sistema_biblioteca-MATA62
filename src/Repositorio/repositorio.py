# --- classe Repositorio (ex: em repositorio.py) ---



from Livros.Exemplar import Exemplar
from Livros.Livro import Livro
from Usuarios.AlunoGraducao import AlunoGraduacao
from Usuarios.Professor import Professor
from Usuarios.AlunoPosGraduacao import AlunoPosGraduacao


class Repositorio:
    _instance = None

    def __new__(cls):
     
        if cls._instance is None:
            print("Criando uma nova instância do Repositorio.")
            cls._instance = super(Repositorio, cls).__new__(cls)
            cls._instance._inicializar_dados()
        return cls._instance

    def _inicializar_dados(self):
        
        self._usuarios = {}
        self._livros = {}
        self._emprestimos = []
        self._carregar_usuarios()
        self._carregar_livros_e_exemplares()
        print("Dados de teste carregados no repositório.")

    def _carregar_usuarios(self):
        dados_usuarios = [
            {"codigo": "123", "tipo": "Aluno Graduação", "nome": "João da Silva"}, 
            {"codigo": "456", "tipo": "Aluno Pós-Graduação", "nome": "Luiz Fernando Rodrigues"},
            {"codigo": "789", "tipo": "Aluno Graduação", "nome": "Pedro Paulo"}, 
            {"codigo": "100", "tipo": "Professor", "nome": "Carlos Lucena"} 
        ]

        for dados in dados_usuarios:
            if dados["tipo"] == "Aluno Graduação":
                usuario = AlunoGraduacao(dados["codigo"], dados["nome"])
            elif dados["tipo"] == "Aluno Pós-Graduação":
                usuario = AlunoPosGraduacao(dados["codigo"], dados["nome"])
            elif dados["tipo"] == "Professor":
                usuario = Professor(dados["codigo"], dados["nome"])
            self._usuarios[usuario.get_id()] = usuario

    def _carregar_livros_e_exemplares(self):
        dados_livros = [
            {"codigo": "100", "titulo": "Engenharia de Software", "editora": "Addison Wesley", "autores": "Ian Sommervile", "edicao": "6a", "ano": "2000"}, 
            {"codigo": "101", "titulo": "UML Guia do Usuário", "editora": "Campus", "autores": "Grady Booch, James Rumbaugh, Ivar Jacobson", "edicao": "7a", "ano": "2000"}, 
            {"codigo": "200", "titulo": "Code Complete", "editora": "Microsoft Press", "autores": "Steve McConnell", "edicao": "2a", "ano": "2014"}, 
            {"codigo": "300", "titulo": "Refactoring: Improving the Design of Existing Code", "editora": "Addison Wesley Professional", "autores": "Martin Fowler", "edicao": "1a", "ano": "1999"}, 
            {"codigo": "400", "titulo": "Design Patterns: Element of Reusable Object-Oriented Software", "editora": "Addison Wesley Professional", "autores": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", "edicao": "1a", "ano": "1994"}, 
        ]
        for dados in dados_livros:
            livro = Livro(dados["codigo"], dados["titulo"], dados["editora"], dados["autores"], dados["edicao"], dados["ano"])
            self._livros[livro.get_id()] = livro

        dados_exemplares = [
            {"cod_livro": "100", "cod_exemplar": "01"}, 
            {"cod_livro": "100", "cod_exemplar": "02"}, 
            {"cod_livro": "101", "cod_exemplar": "03"}, 
            {"cod_livro": "200", "cod_exemplar": "04"}, 
            {"cod_livro": "300", "cod_exemplar": "06"}, 
            {"cod_livro": "300", "cod_exemplar": "07"}, 
            {"cod_livro": "400", "cod_exemplar": "08"}, 
            {"cod_livro": "400", "cod_exemplar": "09"}  
        ]
        
        for dados in dados_exemplares:
            livro = self.buscar_livro_por_codigo(dados["cod_livro"])
            if livro:
                exemplar = Exemplar(dados["cod_exemplar"], livro)
                livro.adicionar_exemplar(exemplar)
    def registrar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)

    def buscar_usuario_por_codigo(self, codigo_usuario):
       
        return self._usuarios.get(codigo_usuario)

    def buscar_livro_por_codigo(self, codigo_livro):
       
        return self._livros.get(codigo_livro)
        
    def listar_todos_livros(self):
        return self._livros.values()

    def listar_todos_usuarios(self):
        return self._usuarios.values()

if __name__ == '__main__':
    repo1 = Repositorio()
    repo2 = Repositorio()

    print(f"Repo1 e Repo2 são a mesma instância? {repo1 is repo2}")

    usuario = repo1.buscar_usuario_por_codigo("123")
    if usuario:
        print(f"\nUsuário encontrado: {usuario.nome} ({usuario.tipo})")

    livro = repo1.buscar_livro_por_codigo("100")
    if livro:
        print(f"Livro encontrado: {livro.titulo}")
        print(f"Total de exemplares: {len(livro.exemplares)}")
        for ex in livro.exemplares:
            print(f"  - Exemplar {ex.codigo} ({ex.status})")
