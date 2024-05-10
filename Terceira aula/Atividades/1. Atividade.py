import os
os.system("cls || clear")

valorA = float(input("Digite o 1º valor: "))
print("\nMenu: \n\n1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão\n\n")
opcao = int(input("\nDigite a opção desejada: "))
valorB = float(input("\nDigite o 2º valor:"))

os.system("cls || clear")

match (opcao):
    case 1:
        print("\nSoma:", valorA + valorB)
    case 2:
        print("\nSubtração", valorA - valorB)
    case 3:
        print("\nMultiplicação", valorA * valorB)
    case 4:        
        print("\nDivisão", valorA / valorB)
