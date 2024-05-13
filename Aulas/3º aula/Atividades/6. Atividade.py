import os
os.system("cls || clear")

pares = 0
impares = 0

for i in range(5): 
    valores = int(input(f"Digite o {i+1}º valor:"))
    if valores % 2 == 0:
        pares += 1
    else:
        impares += 1


print(f"\n\nQuantidade de pares:{pares}")
print(f"\nQuantidade de ímpares:{impares}")