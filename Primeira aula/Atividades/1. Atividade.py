import os
os.system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("\nDigite sua idade: "))
pNota = float(input("\nDigite sua 1ª Nota: "))
sNota = float(input("\nDigite sua 2ª Nota: "))


media = (pNota + sNota) / 2

os.system("cls || clear")

print(f"\nNome: {nome}")
print(f"\nIdade: {idade}")
print(f"\n1ª Nota: {pNota}")
print(f"\n2ª Nota: {sNota}")
print(f"\nMédia: {media}")