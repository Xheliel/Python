import os
os.system("clear")

while True:
    nota1 = float(input("Digite a 1º nota: "))
    if (nota1 < 0 or nota1 > 10):
        print("Nota inválida.")
    else:
        break

os.system("clear")

while True:
    nota2 = float(input("Digite a 2º nota: "))
    if (nota2 < 0 or nota2 > 10):
        print("Nota inválida.")
    else:
        break

print(f"Nota informada: {nota1}")    

print(f"Nota informada: {nota2}")