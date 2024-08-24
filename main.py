from database import *

if __name__ == "__main__":
    db.connect()
    db.create_tables([Usuario])
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Excluir usuários")
        print("4 - Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            CadastrarUsuario()
        elif opcao == 2:
            usuarios = listar_usuarios()
            for usuario in usuarios:
                print(usuario.nome, usuario.email, usuario.Contato)
        elif opcao == 3:
            excluir_usuario()
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")