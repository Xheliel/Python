import os
os.system("cls || clear")

nome = input("Digite seu nome:")
sexo = input("\nQual seu sexo? utilize M ou F: ")
estadoCivil = input("\nDigit seu estado civil:")

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == "f" and estadoCivil == "casada":
    tempoCasamento = input("\nDigite o tempo de casada (em anos): ")

os.system("cls || clear")

print("\n")
print(f"")