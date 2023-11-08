from tabela import tabela
import random
import time
import os

def temporizador(seg):
    inicio =  time.time()
    timeAtual = 0

    while timeAtual < seg:
        timeRestante = seg - timeAtual
        os.system('cls')
        
        print(f'Tempo Restante: {timeRestante}')
        
        resposta = input('Digite o numero: ')
        numSorteado = random.randint(1, 101)
        
        if resposta == numSorteado:
            print(f'Você acertou! O numero sorteado foi {numSorteado}')
            break
        
        timeAtual = time.time() - inicio
        
    if timeAtual >= seg:
        print(f'Tempo esgotado! O número sorteado foi {numSorteado}')

os.system('cls')
print(tabela)
nivel = input('Digite o código: ')

if nivel == '1':
    temporizador(50)
elif nivel == '2':
    temporizador(25)
elif nivel == '3':
    temporizador(15)
