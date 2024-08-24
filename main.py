from database import *
import time


def registrar_usuario():
    print("=== Registro ===")
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    role = input("Digite o papel do usuário (admin/user): ")

    if role not in ['admin', 'user']:
        print("Papel inválido. Use 'admin' ou 'user'.")
        return

    try:
        create_user(username, password, role)
        print("\nUsuário registrado com sucesso!")
    except IntegrityError:
        print("\nErro: Nome de usuário já existe.")

def login():
    print("\n=== Login ===")
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    user = autenticacao_user(username, password)
    if user:
        print(f"\nBem-vindo, {user.username}! Você é um {user.role}.")
        return user
    else:
        print("\nNome de usuário ou senha incorretos.")
        return None


def menu_admin():
    while True:
        print("\n=== Menu Administrador ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Excluir usuário")
        print("4 - Logout")
        opcao = input("Escolha uma opção: ")        

        if opcao == '1':
            CadastrarUsuario()
        elif opcao == '2':
            usuarios = listar_usuarios()
            if usuarios:
                print("\n=== Lista de Usuários ===")
                for usuario in usuarios:
                     print(f"\nNome: {usuario.nome} | Idade: {usuario.idade} | Email: {usuario.email} | CPF: {usuario.CPF} | Contato: {usuario.contato}")
            else:
                print("\nNenhum usuáio cadastrado.")
        elif opcao == '3':
            excluir_usuario()
        elif opcao == '4':
            print("Saindo...")
            time.sleep(2)
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_usuario():
    while True:
        print("\n=== Menu Usuário ===")
        print("1 - Listar usuários")
        print("2 - Logout")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            usuarios = listar_usuarios()
            if usuarios:
                print("\n=== Lista de Usuários ===")
                for usuario in usuarios:
                     print(f"\nNome: {usuario.nome} | CPF: {usuario.CPF} |")
            else:
                print("Nenhum usuáio cadastrado.")
        elif opcao == '2':
            print("Saindo...")
            time.sleep(2)
            break
        else:
            print("Opção inválida ou permissão insuficiente. Tente novamente.")

def main():
    db.connect()
    db.create_tables([User, Usuario])

    user = None
    while True:
        if not user:
            print("\n=== Sistema de Gerenciamento de Usuários ===")
            print("1 - Registrar novo usuário")
            print("2 - Login")
            print("3 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                registrar_usuario()
            elif opcao == '2':
                user = login()
                if user:
                    if user.role == 'admin':
                        menu_admin()
                    else:
                        menu_usuario()
            elif opcao == '3':
                print("Saindo...")
                time.sleep(2)
                break
            else:
                print("Opção inválida. Tente novamente.")
        else:
            if user.role == 'admin':
                menu_admin()
            else:
                menu_usuario()
if __name__=="__main__":
    main()
