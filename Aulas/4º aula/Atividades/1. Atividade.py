import os
os.system("cls || clear")

nota = int(input("Digite sua nota: "))  

while (nota < 0 or nota > 10):
    nota = int(input("Digite sua nota: "))