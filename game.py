from tabela import tabela
from temp import temporizador
from niveis import niveis
import os

os.system('cls')
print(tabela)
nivel = input('Digite o código: ')

print(niveis(nivel))
