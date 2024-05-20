import os
os.system("clear")

TAM_VETOR = 5
numeros = []
zero = 0

for i in range(TAM_VETOR):
    numero = float(input(f"Digite o {1+i}º valor: "))
    if numero < 0:
        numero = 0
        numeros.append(numero)
    else: 
        numeros.append(numero)

os.system("clear")

for i, in enumerate(numeros):
    print(f"{1+i}º número: ") 