import os
import time

logins = "eliel"
senhas = "12345"



os.system("cls || clear")

print(f"Olá!\nAguarde alguns segundos...")
time.sleep(2)

os.system("cls || clear")

print(f"\t\tMENU")
print(f"\n")
print(f"1. Fazer login.")
print(f"2. Criar conta.")
print(f"\n")
opcao = int(input("Qual é a opção desejada? "))

match opcao:
    case 1:
        login = input("Digite seu login: ")
        senha = input ("Digite sua senha: ")
        if login == logins and senha == senhas:
            os.system("clear")
            print("Bem vindo!")
            time.sleep(2)

    

    case 2:
        novologin = input("Crie seu login: ")
        novasenha = input("Crie sua senha: ")

    case _:
        print("Opção inválida!")

os.system("cls || clear")

