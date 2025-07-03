# sistema_biblioteca-MATA62

# Sistema de Gerenciamento de Biblioteca Acadêmica

Este projeto implementa um sistema simples para gerenciamento e manutenção de livros em uma biblioteca acadêmica. O objetivo é aplicar conhecimentos em projeto e programação orientada a objetos, incluindo princípios de projeto e padrões de projeto.

## Funcionalidades

O sistema permite que três tipos de usuários (alunos de graduação, alunos de pós-graduação e professores) realizem as seguintes operações:

* **Empréstimo de Livros**: Os usuários podem emprestar livros informando o código do usuário e o código do livro. Regras específicas de empréstimo se aplicam a cada tipo de usuário. [cite_start]Reservas são canceladas ao efetivar o empréstimo para o usuário que a possuía. 
    * **Regras de Empréstimo para Alunos (Graduação e Pós-Graduação)**:
        1.  [cite_start]Disponibilidade de exemplares. 
        2.  [cite_start]Usuário não "devedor" (livros em atraso). 
        3.  [cite_start]Respeito ao limite máximo de livros emprestados simultaneamente (2 para graduação, 3 para pós-graduação). 
        4.  [cite_start]Quantidade de reservas menor que a quantidade de exemplares disponíveis, *a menos que o usuário tenha uma reserva para o livro*. 
        5.  [cite_start]Usuário não pode ter outro exemplar do mesmo livro emprestado. 
    * **Regras de Empréstimo para Professores**:
        1.  [cite_start]Disponibilidade de exemplares. 
        2.  [cite_start]Usuário não "devedor" (livros em atraso). 
        * [cite_start]Professores não têm o empréstimo negado por reservas existentes e não possuem limite de quantidade de livros emprestados. 
    * [cite_start]**Mensagens de Erro**: Se o empréstimo não for possível, uma mensagem informativa será exibida no console. 
* [cite_start]**Devolução de Livros**: Usuários podem devolver livros informando o código do usuário e o código do livro emprestado. 
* **Reserva de Livros**: Usuários podem reservar livros, garantindo prioridade no empréstimo entre alunos. [cite_start]A data da reserva é registrada. 
* **Registro de Observação de Livros (Professores)**: Professores podem se registrar para receber notificações quando um livro tiver mais de duas reservas simultâneas. [cite_start]O sistema contabiliza as notificações recebidas por cada observador. 
* [cite_start]**Consulta de Informações de Livro**: Dado o código de um livro, o sistema exibe: título, quantidade de reservas (e nomes dos usuários que as fizeram, se houver), e para cada exemplar: código, status (disponível/emprestado), nome do usuário (se emprestado), data de empréstimo e data prevista de devolução. 
* **Consulta de Informações de Usuário**: Dado um usuário, o sistema lista todos os seus empréstimos (correntes e passados) e reservas. Para empréstimos: título do livro, data do empréstimo, status (em curso/finalizado), data de devolução (realizada ou prevista). [cite_start]Para reservas: título do livro e data da solicitação. 
* [cite_start]**Consulta de Notificações Recebidas (Professores)**: Dado o código de um professor, o sistema retorna o número total de notificações recebidas sobre livros observados com mais de duas reservas simultâneas. 
* [cite_start]**Sair do Sistema**: Opção para finalizar o programa. 

## Modelo Conceitual

O diagrama de classes abaixo representa o modelo conceitual do sistema, definindo o relacionamento entre as entidades de negócio. [cite_start]A classe `Repositorio` não é uma entidade de negócio, mas foi incluída para auxiliar no projeto. 

![Modelo Conceitual do Programa](https://i.imgur.com/your-image-link-here.png)
[cite_start]*Figura 1. Modelo Conceitual do Programa. *

## Exigências do Projeto

* **Sem Persistência de Dados**: O sistema **não** utiliza banco de dados. [cite_start]Os dados de teste são instanciados na memória ao iniciar o sistema. 
* **Classe `Repositorio` (Singleton)**: Deve haver uma classe `Repositorio` responsável por manter listas de usuários e livros, além de métodos de busca. [cite_start]Esta classe deve ser implementada seguindo o padrão de projeto Singleton. 
* [cite_start]**Sem Funcionalidades de Cadastro**: O sistema **não** oferece funcionalidades de cadastro de livros, usuários ou exemplares. 
* **Interface de Linha de Comando**: O sistema **não** possui interface gráfica. [cite_start]Todos os comandos são fornecidos via linha de comando, e as respostas são exibidas no console. 
* [cite_start]**Classe de Interação com Usuário**: Uma classe dedicada deve ser responsável por ler comandos do console e exibir respostas. 
* [cite_start]**Padrão Command**: A classe de interação com o usuário deve se comunicar com as classes de negócio (incluindo `Repositorio`) usando um esquema de comandos, projetado de acordo com o padrão de projeto "Command". 
* **Estratégia para Regras de Empréstimo**: Evitar o uso de `if` ou `switch` para determinar o tipo de usuário. [cite_start]Implementar um padrão de projeto que permita selecionar a regra de empréstimo (Regra 1 ou Regra 2) sem condicionais. 
* [cite_start]**Extensibilidade de Observadores**: A funcionalidade de registro de observação para professores deve ser implementada usando um padrão que facilite a inclusão futura de outros tipos de usuários como observadores. 

## Dados de Teste

[cite_start]Os seguintes dados de teste devem ser instanciados na memória ao iniciar o programa: 

### [cite_start]Usuários 

| Código | Tipo Usuário        | Nome                  |
| ------ | ------------------- | --------------------- |
| 123    | Aluno Graduação     | João da Silva         |
| 456    | Aluno Pós-Graduação | Luiz Fernando Rodrigues |
| 789    | Aluno Graduação     | Pedro Paulo           |
| 100    | Professor           | Carlos Lucena         |

### [cite_start]Livros 

| Código | Título                                         | Editora                         | Autores                                        | Edição     | Ano Publicação |
| ------ | ---------------------------------------------- | ------------------------------- | ---------------------------------------------- | ---------- | -------------- |
| 100    | Engenharia de Software                         | Addison Wesley                  | Ian Sommervile                                 | 6ª         | 2000           |
| 101    | UML Guia do Usuário                            | Campus                          | Grady Booch, James Rumbaugh, Ivar Jacobson     | 7ª         | 2000           |
| 200    | Code Complete                                  | Microsoft Press                 | Steve McConnell                                | 2ª         | 2014           |
| 201    | Agile Software Development, Principles, Patterns and Practices | Prentice Hall                   | Robert Martin                                  | 1ª         | 2002           |
| 300    | Refactoring: Improving the Design of Existing Code | Addison Wesley Professional     | Martin Fowler                                  | 1ª         | 1999           |
| 301    | Software Metrics: A rigorous and Practical Approach | CRC Press                       | Norman Fenton, James Bieman                    | 3ª         | 2014           |
| 400    | Design Patterns: Element of Reusable Object-Oriented Software | Addison Wesley Professional     | Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides | 1ª         | 1994           |
| 401    | UML Distilled: A Brief Guide to the Standard Object Modeling Language | Addison Wesley Professional     | Martin Fowler                                  | 3ª         | 2003           |

### [cite_start]Exemplares 

| Código do Livro | Código Exemplar | Status Exemplar |
| --------------- | --------------- | --------------- |
| 100             | 01              | Disponível      |
| 100             | 02              | Disponível      |
| 101             | 03              | Disponível      |
| 200             | 04              | Disponível      |
| 201             | 05              | Disponível      |
| 300             | 06              | Disponível      |
| 300             | 07              | Disponível      |
| 400             | 08              | Disponível      |
| 400             | 09              | Disponível      |

## Como Rodar

(Instruções sobre como compilar e executar o projeto, por exemplo, em Java, Python, etc.)

```bash
# Exemplo para Java
git clone <URL_DO_SEU_REPOSITORIO>
cd <nome_do_diretorio>
javac -d bin src/*.java
java -cp bin Main
