from database import *

def registrar_usuario():
    print("\n== Registrar ==")
    username = input("Digite o nome do usuário: ")
    password = input("Digite a senha: ")
    role = input("Digite o papel do usuário (admin/user): ")

    if role not in ['admin', 'user']:
        print("Papel inválido. Use 'admin' ou 'user'.")
        return

    if role not in ['admin','user']:
        print("Erro ao selecionar usuário. Use 'admin' ou 'user'.")
        return
    try:
        create_user(username, password, role)
        print("Usuário registrado com sucesso!")
    except IntegrityError:
        print("Erro: Nome de usuário já existe.")

def login():
    print("\n== Login ==")
    username = input("Digite o nome do usuário: ")
    password = input("Digite a senha: ")

    user = autenticacao_user(username, password)
    if user:
        print(f"Bem-vindo, {user.username}! Você é um {user.role}")
        return user
    else:
        print("Nome de usuário ou senha incorretos.")
        return None

if __name__ == "__main__":
    db.connect()
    db.create_tables([User,Usuario])

    user = None
    while True:
        if not user:
            print("\nEscolha uma opção:")
            print("1 - Registrar novo usuário")
            print("2 - Login")            
            print("3 - Sair")
            opcao = int(input("Digite o número da opção desejada: "))

            if opcao == 1:
                registrar_usuario()
            elif opcao == 2:
                user = login()
            elif opcao == 3:
                break
            else:
                print("Opção inválida. Tente novamente.")
        else:
             print("\nEscolha uma opção:")
             print("1 - Cadastrar usuário")
             print("2 - Listar usuários")
             print("3 - Excluir usuários")
             print("4 - Logout")
             opcao = int(input("Digite o número da opção desejada: "))

             if opcao == 1 and user.role == 'admin':
                 CadastrarUsuario()
             elif opcao == 2:
                 usuarios = listar_usuarios()
                 for usuario in usuarios:
                     print(f"\nNome: {usuario.nome} | Email: {usuario.email} | CPF: {usuario.CPF} | Contato: {usuario.contato}")
             elif opcao == 3 and user.role == 'admin':
                 excluir_usuario()
             elif opcao == 4:
                 user = None
             else:
                 print("Opção inválida ou permissão insuficiente. Tente novamente.")
