# sistema-exames

Este é o README do projeto "Sistema de Exames" desenvolvido utilizando Python Flask. Esta aplicação permite que professores apliquem exames para seus alunos.

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
   export FLASK_APP=aplication.app
   flask run
   ```

7. A aplicação estará disponível em http://localhost:5000.

8. Para fazer a seed do banco de dados use:

   ```
   flask seed users
   flask seed questoes
   flask seed exames
   ```

   Ao realizar esses comandos, você:
   - adiciona 3 usuários
   - adiciona 3 questões
   - adiciona 2 exames
   - faz o usuário de matrícula 2 realizar o exame 1

10. Para criar um usuário professor, deve-se marcar a checkbox e inserir o código

   ```
   debugmode
   ```

11. Caso queira utilizar algum usuário de teste, existem dois perfis previamente criados:
   - Ester (aluno): 
      - Matrícula: 1
      - Senha: asdfgh
   - Jorginho (aluno):
      - Matrícula: 2
      - Senha: asdfgh   
   - Pedro (professor):
      - Matrícula: 1234
      - Senha: asdfgh

Certifique-se de que as portas necessárias estejam liberadas e que não haja conflitos com outros serviços em execução.

