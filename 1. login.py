import os
import time

os.system("clear")

def salvar_login_senha(login, senha):
    with open('logins.txt', 'a') as arquivo:
        arquivo.write(f'{login}:{senha}\n')
    print("Login e senha salvos com sucesso!")

def main():
    print("Bem-vindo! Por favor, insira seu login e senha.")
    login = input("Login: ")
    senha = input("Senha: ")
    
    salvar_login_senha(login, senha)

if __name__ == "__main__":
    main()
