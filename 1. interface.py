import os
import time

# Limpar a tela
os.system("clear")

# Listas para armazenar logins e senhas
logins = []
senhas = []

# Temporizador de 3 segundos
temporizador = 3

# Função para fazer o login
def fazer_login():
    os.system("clear")
    print("\n")
    print("Fazendo login\n")
    fazer_login = input("Digite seu login: ")
    senha_login = input("Digite sua senha: ")

    if fazer_login in logins and senha_login in senhas:
        print("\n")
        os.system("clear")
        print("Bem vindo novamente!")
        time.sleep(2)
        os.system("clear")
    else:
        print("ERROR:\n")
        print("Login ou senha inexistente ou incorreto!")

# Função para criar uma nova conta
def criar_conta():
    print("\n")
    os.system("clear")
    print("Criando conta\n")
    criar_login = input("Crie seu login (ex: eliel): ")
    logins.append(criar_login)
    criar_senha = input("Crie sua senha: ")
    senhas.append(criar_senha)
    print("Conta criada!")
    time.sleep(1)
    os.system("clear")

# Loop de temporizador
while temporizador > 0:
    print(temporizador)
    time.sleep(1)
    temporizador -= 1

# Limpar a tela
os.system("clear")
print("\n")
print("===== SENAI | FIEB =====")
print("\n")
print("Bem vindo!")

# Loop principal
while True:
    print("\n")
    os.system("clear")
    print("Login interface")
    print("\n")
    print("1. Fazer login")
    print("2. Criar conta")
    print("\n")

    opcao_login = int(input("Qual a opção desejada? "))

    if opcao_login == 1:
        fazer_login()
    elif opcao_login == 2:
        criar_conta()
    else:
        print("\n")
        os.system("clear")
        print("ERROR:\n")
        print("Erro: opção inexistente!")
