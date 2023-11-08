from random import randint

# Nivel da dificuldade
def Dificuldade(nivel):
    if nivel == 1:
        Sorteador(1, 11)
    elif nivel == 2:
        Sorteador(1, 51)
    elif nivel == 3:
        Sorteador(1, 101)

# Sorteador do numero.
def Sorteador(n1, n2):
    numSorteado = randint(n1, n2)
    return numSorteado

# Contador de Tentativas
def Tentativas(numTentativas):
    for tentativa in range(numTentativas):
        resposta = input("Digite algo: ")
        if resposta == 1:
            print("Parabéns! Você acertou.")
            break
        else:
            print("Tentativa inválida. Tente novamente. Você tem", numero_de_chances - tentativa - 1, "chance(s) restante(s).")
    else:
        print("Suas chances se esgotaram. Tente novamente mais tarde.")


numero_de_chances = 3

# Chame a função para iniciar o loop de chances
Tentativas(numero_de_chances)


niveis = """
(1) > Facil   = 7 Tentativas
(2) > Medio   = 4 Tentativas
(3) > Dificil = 3 Tentativas
        """