import os
import time
os.system("clear")

QUANT_NOTAS = 3
notas = []

for i in range(QUANT_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / QUANT_NOTAS

for i, nota in enumerate(notas):
    print(f"Sua {i+1}º nota: {nota}")


print(f"Média: {media}")