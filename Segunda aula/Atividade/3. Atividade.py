import os

os.system("cls || clear")

import time

os.system("cls || clear")

idade = int(input("Digite sua idade:"))

print(f"\nAguarde alguns instantes...")

time.sleep(3)

os.system("cls || clear")

if idade > 18 or idade < 65: 
    print("Você é obrigado a votar!")
else: 
    print("Você não é obrigado a votar!")