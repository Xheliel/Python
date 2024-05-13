import os
os.system("cls || clear")

pNum = int(input("Digite o 1ª número: "))
sNum = int(input("\nDigite o 2ª número: "))

os.system("cls || clear")

media = (pNum + sNum) / 2
soma = (pNum + sNum)
produto = (pNum * sNum)

print(f"\nMédia: {media}")
print(f"\nSoma: {soma}")
print(f"\nProduto: {produto}")

if (pNum == sNum): 
    print(f"\nAmbos números inseridos são iguais!")
else:
    print(f"\nAmbos números são diferentes!")

if (pNum > sNum):
    print(f"\nO 1ª é o maior número!")
    print(f"\nO menor número é o 2ª!")
else:
    print(f"\nO 2ª número é o maior!")    
    print(f"\nO 1ª número é o menor!")