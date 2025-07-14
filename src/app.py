# app.py (Corrigido)

# 1. Importar os gerenciadores e o repositório, além dos comandos
from Repositorio.repositorio import Repositorio
from Gerenciadores.Gerenciadores import GerenciadorDeConsultas, GerenciadorDeEmprestimos, GerenciadorDeInteracoes
from Comandos.Comandos import * # Usando os comandos refatorados

class ConsoleUI:
    """
    Interface de console adaptada para a arquitetura com Gerenciadores.
    """
    def __init__(self):
        # 2. Obter a instância do repositório e criar os gerenciadores
        repositorio = Repositorio()
        self.gerenciador_emprestimos = GerenciadorDeEmprestimos(repositorio)
        self.gerenciador_interacoes = GerenciadorDeInteracoes(repositorio)
        self.gerenciador_consultas = GerenciadorDeConsultas(repositorio)

        # 3. Mapear comandos para uma tupla: (ClasseDoComando, GerenciadorNecessario)
        self.comandos = {
            "emp": (ComandoEmprestar, self.gerenciador_emprestimos),
            "dev": (ComandoDevolver, self.gerenciador_emprestimos),
            "res": (ComandoReservar, self.gerenciador_interacoes),
            "obs": (ComandoRegistrarObservador, self.gerenciador_interacoes),
            "liv": (ComandoConsultaLivro, self.gerenciador_consultas),
            "usu": (ComandoConsultaUsuario, self.gerenciador_consultas),
            "ntf": (ComandoConsultaNotificacoes, self.gerenciador_consultas),
            "sai": (ComandoSair, None) # 'sai' não precisa de gerenciador
        }

    def iniciar(self):
        """
        Inicia o loop principal da aplicação, lendo e processando comandos.
        """
        print("--- Sistema de Biblioteca Acadêmica ---")
        print("Digite um comando ou 'sai' para terminar.")

        while True:
            try:
                entrada = input("> ")
                partes = entrada.strip().split()

                if not partes:
                    continue

                comando_str = partes[0].lower()
                
                if comando_str not in self.comandos:
                    print(f"Erro: Comando '{comando_str}' não reconhecido.")
                    continue
                
                # 4. Desempacotar a classe e o gerenciador do mapeamento
                ClasseDoComando, gerenciador = self.comandos.get(comando_str)
                argumentos = partes[1:]
                
                # Tratamento especial para comandos sem gerenciador
                if gerenciador:
                    # 5. Injetar o gerenciador ao criar a instância do comando
                    comando_obj = ClasseDoComando(gerenciador, *argumentos)
                else:
                    # Caso do 'sai', que não tem argumentos nem gerenciador
                    comando_obj = ClasseDoComando(*argumentos)
                
                # Executa o comando
                comando_obj.executar()

            except TypeError:
                print(f"Erro: Número incorreto de argumentos para o comando '{comando_str}'. Verifique a entrada.")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

# Ponto de entrada do programa
if __name__ == "__main__":
    app = ConsoleUI()
    app.iniciar()