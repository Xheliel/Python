import os
os.system("clear")

QUANT_NUMEROS = 5
numeros = []

for i in range(QUANT_NUMEROS):
    numero = float(input(f"Digite o {1+i}º número: "))
    numeros.append(numero)

os.system("clear")

menor_numero = min(numeros)
maior_numero = max(numeros)

print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
