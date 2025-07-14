
from Repositorio.repositorio import Repositorio
from Gerenciadores.Gerenciadores import GerenciadorDeConsultas, GerenciadorDeEmprestimos, GerenciadorDeInteracoes
from Comandos.Comandos import * 

class ConsoleUI:
    
    def __init__(self):
        repositorio = Repositorio()
        self.gerenciador_emprestimos = GerenciadorDeEmprestimos(repositorio)
        self.gerenciador_interacoes = GerenciadorDeInteracoes(repositorio)
        self.gerenciador_consultas = GerenciadorDeConsultas(repositorio)

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
                
                ClasseDoComando, gerenciador = self.comandos.get(comando_str)
                argumentos = partes[1:]
                
                if gerenciador:
                    comando_obj = ClasseDoComando(gerenciador, *argumentos)
                else:
                    comando_obj = ClasseDoComando(*argumentos)
                
                comando_obj.executar()

            except TypeError:
                print(f"Erro: Número incorreto de argumentos para o comando '{comando_str}'. Verifique a entrada.")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    app = ConsoleUI()
    app.iniciar()
