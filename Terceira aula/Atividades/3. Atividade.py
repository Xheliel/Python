import os
os.system("cls || clear")

numero = float(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")