# Comandos_Refatorados.py

from abc import ABC, abstractmethod
import sys
from Gerenciadores.Gerenciadores import GerenciadorDeConsultas, GerenciadorDeEmprestimos, GerenciadorDeInteracoes

class Command(ABC):
    @abstractmethod
    def executar(self):
        pass

# --- Comandos de Ação ---

class ComandoEmprestar(Command):
    def __init__(self, gerenciador: GerenciadorDeEmprestimos, codigo_usuario: str, codigo_livro: str):
        self.gerenciador = gerenciador
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        resultado = self.gerenciador.emprestar_livro(self.codigo_usuario, self.codigo_livro)
        print(resultado)

class ComandoDevolver(Command):
    def __init__(self, gerenciador: GerenciadorDeEmprestimos, codigo_usuario: str, codigo_livro: str):
        self.gerenciador = gerenciador
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        resultado = self.gerenciador.devolver_livro(self.codigo_usuario, self.codigo_livro)
        print(resultado)

class ComandoReservar(Command):
    def __init__(self, gerenciador: GerenciadorDeInteracoes, codigo_usuario: str, codigo_livro: str):
        self.gerenciador = gerenciador
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        resultado = self.gerenciador.reservar_livro(self.codigo_usuario, self.codigo_livro)
        print(resultado)

class ComandoRegistrarObservador(Command):
    def __init__(self, gerenciador: GerenciadorDeInteracoes, codigo_usuario: str, codigo_livro: str):
        self.gerenciador = gerenciador
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro

    def executar(self):
        resultado = self.gerenciador.registrar_observador(self.codigo_usuario, self.codigo_livro)
        print(resultado)

# --- Comandos de Consulta ---

class ComandoConsultaUsuario(Command):
    def __init__(self, gerenciador: GerenciadorDeConsultas, codigo_usuario: str):
        self.gerenciador = gerenciador
        self.codigo_usuario = codigo_usuario

    def executar(self):
        resultado = self.gerenciador.consultar_usuario(self.codigo_usuario)
        print(resultado)

class ComandoConsultaLivro(Command):
    def __init__(self, gerenciador: GerenciadorDeConsultas, codigo_livro: str):
        self.gerenciador = gerenciador
        self.codigo_livro = codigo_livro

    def executar(self):
        resultado = self.gerenciador.consultar_livro(self.codigo_livro)
        print(resultado)

class ComandoConsultaNotificacoes(Command):
    def __init__(self, gerenciador: GerenciadorDeConsultas, codigo_usuario: str):
        self.gerenciador = gerenciador
        self.codigo_usuario = codigo_usuario

    def executar(self):
        resultado = self.gerenciador.consultar_notificacoes(self.codigo_usuario)
        print(resultado)

# --- Comando de Sistema ---

class ComandoSair(Command):
    def executar(self):
        print("Saindo do sistema de biblioteca...")
        sys.exit(0)