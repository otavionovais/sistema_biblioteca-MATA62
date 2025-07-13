# --- classe Repositorio (ex: em repositorio.py) ---

# Importe as classes do modelo se estiverem em outro arquivo
# from modelos import Livro, Exemplar, Usuario, AlunoGraduacao, AlunoPosGraduacao, Professor

from Livros.Exemplar import Exemplar
from Livros.Livro import Livro
from Usuarios.AlunoGraducao import AlunoGraduacao
from Usuarios.Professor import Professor
from Usuarios.AlunoPosGraduacao import AlunoPosGraduacao


class Repositorio:
    _instance = None

    def __new__(cls):
        # O método __new__ é chamado antes do __init__
        # e é aqui que controlamos a criação da instância.
        if cls._instance is None:
            print("Criando uma nova instância do Repositorio.")
            cls._instance = super(Repositorio, cls).__new__(cls)
            # Inicializa os dados apenas na primeira criação
            cls._instance._inicializar_dados()
        return cls._instance

    def _inicializar_dados(self):
        """
        Método privado para carregar os dados de teste na memória,
        conforme exigido pela Seção 5.1 e 8 do documento. 
        """
        # Usar dicionários para busca rápida por código é mais eficiente
        self._usuarios = {}
        self._livros = {}
        self._emprestimos = []
        self._carregar_usuarios()
        self._carregar_livros_e_exemplares()
        print("Dados de teste carregados no repositório.")

    def _carregar_usuarios(self):
        """ Carrega os usuários de teste [cite: 135] """
        dados_usuarios = [
            {"codigo": "123", "tipo": "Aluno Graduação", "nome": "João da Silva"}, # [cite: 134]
            {"codigo": "456", "tipo": "Aluno Pós-Graduação", "nome": "Luiz Fernando Rodrigues"}, # [cite: 134]
            {"codigo": "789", "tipo": "Aluno Graduação", "nome": "Pedro Paulo"}, # [cite: 134]
            {"codigo": "100", "tipo": "Professor", "nome": "Carlos Lucena"} # [cite: 134]
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
        """ Carrega os livros de teste [cite: 136] e seus exemplares [cite: 138] """
        dados_livros = [
            {"codigo": "100", "titulo": "Engenharia de Software", "editora": "Addison Wesley", "autores": "Ian Sommervile", "edicao": "6a", "ano": "2000"}, # [cite: 137]
            {"codigo": "101", "titulo": "UML Guia do Usuário", "editora": "Campus", "autores": "Grady Booch, James Rumbaugh, Ivar Jacobson", "edicao": "7a", "ano": "2000"}, # [cite: 137]
            {"codigo": "200", "titulo": "Code Complete", "editora": "Microsoft Press", "autores": "Steve McConnell", "edicao": "2a", "ano": "2014"}, # [cite: 137]
            {"codigo": "300", "titulo": "Refactoring: Improving the Design of Existing Code", "editora": "Addison Wesley Professional", "autores": "Martin Fowler", "edicao": "1a", "ano": "1999"}, # [cite: 137]
            {"codigo": "400", "titulo": "Design Patterns: Element of Reusable Object-Oriented Software", "editora": "Addison Wesley Professional", "autores": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", "edicao": "1a", "ano": "1994"}, # [cite: 137]
        ]

        for dados in dados_livros:
            livro = Livro(dados["codigo"], dados["titulo"], dados["editora"], dados["autores"], dados["edicao"], dados["ano"])
            self._livros[livro.get_id()] = livro

        dados_exemplares = [
            {"cod_livro": "100", "cod_exemplar": "01"}, # [cite: 139]
            {"cod_livro": "100", "cod_exemplar": "02"}, # [cite: 139]
            {"cod_livro": "101", "cod_exemplar": "03"}, # [cite: 139]
            {"cod_livro": "200", "cod_exemplar": "04"}, # [cite: 139]
            {"cod_livro": "300", "cod_exemplar": "06"}, # [cite: 139]
            {"cod_livro": "300", "cod_exemplar": "07"}, # [cite: 139]
            {"cod_livro": "400", "cod_exemplar": "08"}, # [cite: 139]
            {"cod_livro": "400", "cod_exemplar": "09"}  # [cite: 139]
        ]
        
        for dados in dados_exemplares:
            livro = self.buscar_livro_por_codigo(dados["cod_livro"])
            if livro:
                exemplar = Exemplar(dados["cod_exemplar"], livro)
                livro.adicionar_exemplar(exemplar)
    def registrar_emprestimo(self, emprestimo):
        """Adiciona um novo empréstimo à lista de histórico do sistema."""
        self._emprestimos.append(emprestimo)

    def buscar_usuario_por_codigo(self, codigo_usuario):
        """
        Busca um usuário pelo seu código. 
        Retorna o objeto Usuario ou None se não for encontrado.
        """
        return self._usuarios.get(codigo_usuario)

    def buscar_livro_por_codigo(self, codigo_livro):
        """
        Busca um livro pelo seu código. 
        Retorna o objeto Livro ou None se não for encontrado.
        """
        return self._livros.get(codigo_livro)
        
    def listar_todos_livros(self):
        """ Método auxiliar para verificar os dados carregados """
        return self._livros.values()

    def listar_todos_usuarios(self):
        """ Método auxiliar para verificar os dados carregados """
        return self._usuarios.values()

# --- Exemplo de Uso ---
if __name__ == '__main__':
    # Você obterá a mesma instância todas as vezes
    repo1 = Repositorio()
    repo2 = Repositorio()

    print(f"Repo1 e Repo2 são a mesma instância? {repo1 is repo2}")

    # Exemplo de busca de usuário 
    usuario = repo1.buscar_usuario_por_codigo("123")
    if usuario:
        print(f"\nUsuário encontrado: {usuario.nome} ({usuario.tipo})")

    # Exemplo de busca de livro 
    livro = repo1.buscar_livro_por_codigo("100")
    if livro:
        print(f"Livro encontrado: {livro.titulo}")
        print(f"Total de exemplares: {len(livro.exemplares)}")
        for ex in livro.exemplares:
            print(f"  - Exemplar {ex.codigo} ({ex.status})")