# em main.py ou app.py

# Importe suas classes de Comando e a Fachada

from BancoDeDados.Comandos import ComandoConsultaLivros, ComandoConsultaNotificacoes, ComandoConsultaUsuario, ComandoDevolver, ComandoEmprestar, ComandoRegistrarObservador, ComandoReservar, ComandoSair
from SistemaBiblioteca.BibliotecaFacade import BibliotecaFacade

class ConsoleUI:
    """
    Esta é a classe exigida pela Seção 5.5, responsável pela interação
    com o usuário via console.
    """
    def __init__(self):
        # A fachada é instanciada aqui para ser usada pelos comandos
        self.facade = BibliotecaFacade()

        # O mapeamento dos comandos para as classes que os executam
        self.comandos = {
            "emp": ComandoEmprestar,
            "dev": ComandoDevolver,
            "liv": ComandoConsultaLivros,
            "usu": ComandoConsultaUsuario,
            "res": ComandoReservar,
            "obs": ComandoRegistrarObservador,
            "ntf": ComandoConsultaNotificacoes,
            "sai": ComandoSair
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
                ClasseDoComando = self.comandos.get(comando_str)

                if not ClasseDoComando:
                    print(f"Erro: Comando '{comando_str}' não reconhecido.")
                    continue


                # Extrai os argumentos para o construtor do comando
                argumentos = partes[1:]
                
                # Cria a instância do comando com seus argumentos
                comando_obj = ClasseDoComando(*argumentos)
                
                # Executa o comando
                comando_obj.executar()

            except TypeError:
                print(f"Erro: Número incorreto de argumentos para o comando '{comando_str}': {e}")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

# Ponto de entrada do programa
if __name__ == "__main__":
    app = ConsoleUI()
    app.iniciar()