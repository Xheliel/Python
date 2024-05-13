import os

os.system("clear")

soma = 0
contNotas = 0
notas = []

print("\n\n")
print("Menu:")
print("\n")
print("S - Para inserir mais uma nota.")
print("P - Para ver a quantidade de notas inseridas.")
print("N - Para calcular e mostrar média.")

while True:
    resposta = input("Digite a opção desejada para prosseguir: ")

    resposta = resposta.upper()

    if resposta == "S":
        os.system("clear")
        nota = float(input(f"Digite a {contNotas + 1}ª nota: "))
        notas.append(nota)
        contNotas += 1

    elif resposta == "P":
        os.system("clear")
        print(f"Quantidade de notas inseridas: {contNotas}")

    elif resposta == "N":
        os.system("clear")
        if contNotas == 0:
            print("Nenhuma nota foi inserida.")
        else:
            soma = sum(notas)
            media = soma / contNotas
            print(f"Sua média: {media}")

    else:
        print("Opção inválida!")
