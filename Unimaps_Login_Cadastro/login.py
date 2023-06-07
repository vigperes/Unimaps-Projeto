from dados import *


while True:
    print("Bem-vindo ao Unimaps - UNIMAR")
    print("Digite a opção:")
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Esqueci a senha")
    print("4 - Sair do app")

    op = input("Digite o número da opção desejada: ")
    
    if op not in ["1", "2", "3", "4"]:
        print("Opção não existe. Digite um número de 1 a 4")
        continue
        
    op = int(op)

    if op == 1:
        print("Opção de login selecionada.")
        login() 
        break
    elif op == 2:
        print("Opção de cadastro selecionada.")
        cadastro()

        break
    elif op == 3:
        print("Opção de recuperação de senha selecionada.")
        recu_senha()
        break
    else:
        print("Saindo do app.")
        break