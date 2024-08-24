# Sistema de Gerenciamento de Usuários
O sistema desenvolvido é uma aplicação web simples que permite o cadastro, login, e gerenciamento de usuários e clientes. Ele foi construído utilizando o framework Flask, que é um microframework para Python, e utiliza o Peewee como ORM para interagir com um banco de dados SQLite.

# Funcionalidades Principais
- <b>Registro de Usuários</b>: Permite o registro de novos usuários com nome de usuário, senha e função.
- <b>Login de Usuários</b>: Validação de credenciais e autenticação de usuários.
- <b>Dashboard</b>: Exibe uma lista de clientes cadastrados.
- <b>Cadastro de Clientes</b>: Interface para adicionar novos clientes ao sistema.
- <b>Remoção de Clientes</b>: Opção para excluir clientes cadastrados.

# Bibliotecas Utilizadas
As principais bibliotecas e ferramentas utilizadas neste sistema são:
- <b>Flask</b>: Framework para desenvolvimento de aplicações web em Python.
- <b>Peewee</b>: ORM (Object-Relational Mapping) utilizado para interagir com o banco de dados SQLite.
- <b>Werkzeug</b>: Utilizado para hash de senhas e outras utilidades relacionadas à segurança.
- <b>SQLite</b>: Sistema de banco de dados utilizado para armazenar as informações dos usuários e clientes.

# Instalação
<b>Para instalar e executar o sistema localmente, siga os passos abaixo:</b>
1. Clonar o Repositório
   - Primeiro, clone o repositório do GitHub para o seu ambiente local:
     - git clone https://github.com/seu-usuario/nome-do-repositorio.git
     - cd nome-do-repositorio
2. Criar um Ambiente Virtual
   - É recomendável criar um ambiente virtual para instalar as dependências:
     - python -m venv venv
     - source venv/bin/activate  # No Windows: venv\Scripts\activate
3. Instalar as Dependências
   - Instale as bibliotecas necessárias utilizando o pip:
     - pip install -r requirements.txt
   - Se o arquivo requirements.txt ainda não estiver criado, você pode gerar um com o seguinte comando:
     - pip freeze > requirements.txt
4. Configurar o Banco de Dados
   - Inicialize o banco de dados criando as tabelas necessárias:
     - from main import init_db
     - init_db()
5. Executar o Sistema
   - Inicie a aplicação Flask:
     - python main.py
     - Acesse o sistema no navegador através do endereço <b>http://127.0.0.1:5000/</b>.

# Como Usar
- Registro de Usuário: Acesse a página de registro para criar uma nova conta.
- Login: Faça login com suas credenciais na página de login.
- Dashboard: Após o login, você será redirecionado para o dashboard, onde pode ver a lista de clientes.
- Adicionar Cliente: Na página do dashboard, há uma opção para adicionar um novo cliente.
- Excluir Cliente: Utilize a opção de exclusão para remover um cliente da lista.

# Considerações Finais
<b>Este sistema foi desenvolvido como um exemplo básico de CRUD (Create, Read, Update, Delete) utilizando Flask e Peewee. Ele pode ser expandido conforme a necessidade, adicionando novas funcionalidades ou melhorando as já existentes.</b>


