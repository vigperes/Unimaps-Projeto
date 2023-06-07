from dataclasses import dataclass
from getpass import getpass
from hashlib import sha256
from typing import List

@dataclass 
class Usuario:
    login: str
    senha: bytes


def login() -> Usuario:
    arq_usuario = open('Usuarios.txt','r')
    arq_senha= open ('Senha.txt','r')
    dados1=arq_usuario.read()
    dados2=arq_senha.read()
    arq_usuario.close()
    arq_senha.close()
    usuario = input("Digite o nome do seu usuario:")
    senha = getpass("Digite a sua senha:")
    hashed_senha = sha256(senha.encode()).digest()
    if (dados1.strip() == usuario)and (dados2.strip()==senha):
     print(f'Bem vindo ao Unimaps {usuario}')
    else:
       print('Nao foi possivel achar o usuario')
    return Usuario(usuario, hashed_senha)
    


def cadastro() -> Usuario:
    while True:
        usuario = input('Crie seu nome de usuario:')
        senha = getpass('Crie sua senha:')
        c_senha = getpass('Confirme sua senha:')
        if senha == c_senha:
            hashed_senha = sha256(senha.encode()).digest()           
            with open('Usuarios.txt','a') as arq_usuario:
             arq_senha = open('Senha.txt','a')
             arq_usuario.write(usuario)
             arq_senha.write(senha)
             arq_usuario.write('\n')
             arq_senha.write('\n')
             arq_usuario.close()
             arq_senha.close()
            return Usuario(usuario, hashed_senha)
        else:
            print('As senhas não são iguais.')

def recu_senha():
    usuario= input('Digite seu usuario:')
    print(f'{usuario} sera enviado sua nova senha no seu email onde esta cadastrado')

