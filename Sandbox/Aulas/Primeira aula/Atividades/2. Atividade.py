import os
os.system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("\nDigite sua idade: "))
pNota = float(input("\nDigite sua 1ª Nota: "))
sNota = float(input("\nDigite sua 2ª Nota: "))
tNota = float(input("\nDigite sua 3ª Nota: "))

media = (pNota + sNota + tNota) / 3

os.system("cls || clear")

print(f"\nNome: {nome}")
print(f"\nIdade: {idade}")
print(f"\n1ª Nota: {pNota}")
print(f"\n2ª Nota: {sNota}")
print(f"\nMédia: {media}")

if media < 7:
    print(f"\nSituação: Reprovado!")
else:
    print(f"\nSituação: Aprovado!")