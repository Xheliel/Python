import os
os.system("clear")

nota1 = int(input("Digite sua 1º nota: "))  

while (nota1 < 0 or nota1 > 10):
    nota1 = int(input("Digite sua 1º nota: "))

    os.system("clear")

nota2 = int(input("Digite sua 2º nota: "))  

while (nota2 < 0 or nota2 > 10):
    nota2 = int(input("Digite sua 2º nota: "))

os.system("clear")

print("Resultados:\n")
print(f"Sua 1º nota: {nota1}")
print(f"\nSua 2º nota: {nota2}")

media = (nota1 + nota2) / 2

print(f"\nMédia: {media}")
