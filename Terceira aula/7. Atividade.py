import os
os.system("cls || clear")

soma = 0

for i in range(4):
    nota = float(input(f"Digite sua {i+1} nota: "))
    soma += nota 

media = soma / 4

os.system("cls || clear")

print("Resultado: ")
print(f"Média: {media}")