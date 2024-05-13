import os
os.system("clear")

soma = 0

for i in range(3):
    while True :
        nota = float(input("Digite a º nota: "))
        if nota < 0 or nota > 10:
            print("Nota inválida... \n")

        else:
            soma += nota
            break

media = soma / 3

for i in range(3):
    print(f"Sua {i+1}º nota: {nota}")

print("\n")

if (media > 7):
    print(f"Aprovado!")
elif (media >= 5 and media < 6.9):
    print(f"Recuperação!")
else:
    print(f"Reprovado!")