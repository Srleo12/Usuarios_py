from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash

db =  SqliteDatabase("Usuarios.db")

class User(Model):
    username = CharField(unique=True)
    password = CharField()
    role = CharField()

    class Meta:
        database = db

class Usuario(Model):
    nome = CharField()
    idade= DecimalField()
    email = CharField(unique=True)
    contato= CharField(unique=True)
    CPF= CharField(unique=True)
    endereco=CharField()
    
    class Meta:
        database = db

def create_user(username, password, role='user'):
    hashed_password = generate_password_hash(password)
    user = User.create(username=username, password=hashed_password, role=role)
    return user

def autenticacao_user(username, password):
    user = User.get_or_none(User.username == username)
    if user and check_password_hash(user.password, password):
        return user

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
        contato=contato_usuario,
        CPF=cpf_usuario,
        endereco=endereco_usuario
    )

    usuario.save()

    print("\nUsuário cadastrado com sucesso!")


def listar_usuarios():
    usuarios = Usuario.select()
    return usuarios

def excluir_usuario():
    cpf_usuario = input("\nDigite o CPF do usuário que deseja excluir: ")
    usuario = Usuario.get_or_none(CPF=cpf_usuario)
    if usuario:
        usuario.delete_instance()
        print("\nUsuário excluído com sucesso!")
    else:
        print("\nUsuário não encontrado.")