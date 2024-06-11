import os
from dataclasses import dataclass

os.system("clear || cls")

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno: 
    nome: str
    idade: int
    peso: float

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome_aluno = input("Digite o nome: ")
    idade_aluno = int(input("Digite a idade: "))
    peso_aluno = float(input("Digite seu peso: "))
    aluno = Aluno(nome = nome_aluno, idade = idade_aluno, peso = peso_aluno)
    alunos.append(aluno)

for dados_aluno in alunos:
    print(f"nome: {dados_aluno.nome}")
    print(f"idade: {dados_aluno.idade}")
    print(f"peso: {dados_aluno.peso}")
