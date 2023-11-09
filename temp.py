import time, random, os

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