import os
os.system("clear || cls")
from dataclasses import dataclass
import time

veiculos = []
clientes = []

@dataclass
class Carro:
    placa: str
    cor: str
    qntpassageiros: int
    capacidadetanq: float
    velomax: int
    consumo: float

@dataclass
class Cliente:
    nome: str
    idade: int
    cpf: str
    endereco: str
    telefone: str

def logo():
    print("\n====================")
    print("DETRAN BA")
    print("====================\n")

def registro_veiculo():
    placa_veiculo= input("Digite a placa do veículo: ")
    cor_veiculo = input("Digite a cor do veículo: ")
    qntpassageiros_veiculo = int(input("Capacidade maxíma de passageiros: "))
    capacidadetanq_veiculo = float(input("Digite a capacidade maxíma de combustível: "))
    velomax_veiculo = int(input("Qual a velocidade maxíma: "))
    consumo_veiculo = float(input("Qual é o consumo médio: "))
    veiculo = Carro(placa = placa_veiculo, cor = cor_veiculo, qntpassageiros = qntpassageiros_veiculo, capacidadetanq = capacidadetanq_veiculo, consumo = consumo_veiculo, velomax = velomax_veiculo)
    veiculos.append(veiculo)
    os.system("clear || cls")

def registro_cliente():
    nome_cliente = input("Digite seu nome: ")
    idade_cliente = int(input("Digite sua idade: "))
    cpf_cliente = input("Digite seu cpf: ")
    endereco_cliente = input("Digite seu endereço: ")
    telefone_cliente = input("Digite seu telefone: ")
    cliente = Cliente(nome = nome_cliente, idade = idade_cliente, cpf = cpf_cliente, endereco = endereco_cliente, telefone = telefone_cliente)
    clientes.append(cliente)
    os.system("clear || cls")

def menu():
    print("\tMENU\n")
    print("1. Cadastrar motorista")
    print("2. Cadastrar veículo")
    print("3. Encerrar")

os.system("clear || cls")

# codigo funcional

logo()
print("Bem vindo!")
print("Aguarde alguns segundos ...")
time.sleep(3)

os.system("clear || cls")

logo()
menu()
opcao = int(input("Qual a opção desejada? "))

match opcao:
    case 1:
        registro_cliente()

    case 2:
        registro_veiculo

    case 3:
        os.system("clear || cls")

    case _:
        print("Opção invalída!")