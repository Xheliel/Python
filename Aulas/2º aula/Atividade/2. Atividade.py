import os
import time

os.system("cls || clear")

loginSalvo: str = "Eliel5"
senhaSalva: str = "123"

login = input("\nDigite login: ")

senha = input("\nDigite sua senha: ")

os.system("cls || clear")

if login == loginSalvo & senha == senhaSalva:
    print(f"Bem-vindo!")
else:
    print(f"Login ou senha incorretos!")