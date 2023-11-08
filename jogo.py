from tabela import tabela
from random import randint
import os

def Sorteador(n1, n2):
    numSorteado = randint(n1, n2)
    return numSorteado

def Dificuldade(nivel):
    if nivel == 1:
        return Sorteador(1, 11)
    elif nivel == 2:
        return Sorteador(1, 51)
    elif nivel == 3:
        return Sorteador(1, 101)

def Tentativas(numTentativas):
    for tentativa in range(numTentativas):
        resposta = input(".")
        if resposta == 1:
            print(".")
            break
        else:
            print(".")
    else:
        print(".")


print(tabela)

nivel = int(input('Digite o codigo: '))
numeroSorteado = Dificuldade(nivel)

if nivel == numeroSorteado:
    print(f'Você acertou {numeroSorteado}')

Tentativas
