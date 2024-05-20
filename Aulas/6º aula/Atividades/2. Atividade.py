import os
os.system("clear")

QUANT_NUMERO = 6
numeros = []
pares = 0
impares = 0

for i in range(QUANT_NUMERO):
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

os.system("clear")

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")