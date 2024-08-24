from peewee import * # type: ignore


db =  SqliteDatabase("RegistroUsuario.db")

class Usuario(Model):
    nome = CharField()
    idade= DecimalField()
    email = CharField(unique=True)
    Contato= CharField(unique=True)
    CPF= CharField(unique=True)
    Endereco=CharField()
    
    class Meta:
        database = db

def CadastrarUsuario():
    nome_usuario = input("Digite o nome do usuário: ")
    idade_usuario = float(input("Digite a idade do usuário: "))
    email_usuario = input("Digite o email do usuário: ")
    contato_usuario = input("Digite o contato do usuário: ")
    cpf_usuario = input("Digite o CPF do usuário: ")
    endereco_usuario = input("Digite o endereço do usuário: ")

    usuario = Usuario(
        nome=nome_usuario,
        idade=idade_usuario,
        email=email_usuario,
        Contato=contato_usuario,
        CPF=cpf_usuario,
        Endereco=endereco_usuario
    )

    usuario.save()

    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    usuarios = Usuario.select()
    return usuarios

def excluir_usuario():
    cpf_usuario = input("Digite o CPF do usuário que deseja excluir: ")
    usuario = Usuario.get_or_none(CPF=cpf_usuario)
    if usuario:
        usuario.delete_instance()
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado.")