import os
from dataclasses import dataclass
os.system("clear || cls")

@dataclass
class Pet:
    nome: str
    idade: int
    raça: str
    porte: str
    alimentação: str
    
