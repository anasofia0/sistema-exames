# sistema-exames

Este é o README do projeto "Sistema de Exames" desenvolvido utilizando Python Flask. Esta aplicação permite que professorem apliquem exames para seus alunos.

## Descrição da Aplicação

### Perfis de Usuário
### Fluxos e Funcionalidades Disponíveis
### Principais Decisões de Projeto
## Screenshots
## Instruções para Executar o Projeto

Siga as instruções abaixo para executar a aplicação em um sistema limpo:

1. Certifique-se de ter o Python instalado em seu sistema. Recomenda-se a versão Python 3.7 ou superior.

2. Instale o gerenciador de dependências Poetry. Você pode encontrar instruções de instalação em https://python-poetry.org/docs/#installation.

3. Faça o download ou clone este repositório para o seu sistema.

4. No diretório raiz do projeto, execute o seguinte comando para instalar as dependências:

   ```
   poetry install
   ```

5. Após a conclusão da instalação das dependências, ative o ambiente virtual criado pelo Poetry:

   ```
   poetry shell
   ```

6. Execute o seguinte comando para iniciar a aplicação:

   ```
   export FLASK_APP=app.app
   flask run
   ```

7. A aplicação estará disponível em http://localhost:5000.

Certifique-se de que as portas necessárias estejam liberadas e que não haja conflitos com outros serviços em execução.

Nota: Lembre-se de configurar corretamente as informações de conexão com o banco de dados no arquivo de configuração do projeto, caso seja necessário.

