from tabela import tabela
from temp import temporizador
import os

os.system('cls')
print(tabela)
nivel = input('Digite o código: ')

if nivel == '1':
    temporizador(50)
elif nivel == '2':
    temporizador(25)
elif nivel == '3':
    temporizador(15)
