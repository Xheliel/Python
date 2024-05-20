import os
os.system("clear")

QUANT_NUMEROS = 10
numeros = []
negativos = 0
positivos = 0
somaPositivos = 0

for i in range(QUANT_NUMEROS):
    numero = float(input(f"Digite o {1+i}º número: "))
    numeros.append(numero)
    if numero < 0:
        negativos += 1
    else:
        positivos += 1
        somaPositivos += numero

os.system("clear")

print(f"Quantidade de negativos: {negativos}")
print(f"Quantidade de positivos: {positivos}")
print(f"Soma dos positivos: {somaPositivos}")