import os
from dataclasses import dataclass

os.system("clear || cls")

QUANT_LIVROS = 2

class Livro:
    titulo: str
    autor: str
    paginas: int
    preco: float

livros = []

for i in range(QUANT_LIVROS):
    titulo_livro = input("Digite o título do livro: ")
    autor_livro = input("Digite o nome do autor: ")
    paginas_livro = int(input("Qual a quantidade de paginas do livro? "))
    preco_livro = float(input("Digite o valor do livro: "))
    livro = Livro(titulo  = titulo_livro, autor = autor_livro, paginas = paginas_livro, preco = preco_livro)
    livros.append(livro)

    for dados_livro in livros:
        print(f"Título: {dados_livro.titulo}")
        print(f"Autor: {dados_livro.autor}")
        print(f"Quantidade de pagínas: {dados_livro.paginas}")
        print(f"Preço: {dados_livro.preco}")