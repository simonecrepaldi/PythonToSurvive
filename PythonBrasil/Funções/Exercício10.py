# Jogo de Craps.
# Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12.
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random
def jogarDados():
    dado = random.randint(1, 6)
    return dado

def jogo():
    ponto = 0
    while True:
        soma = jogarDados() + jogarDados()
        print(f"Soma dos teus dados: {soma}")

        if ponto == 0:
            if soma == 7 or soma == 11:
                print("Você venceu!")
                break
            elif soma == 2 or soma == 3 or soma == 12:
                print("Craps! Você perdeu!")
                break
            else:
                ponto = soma
                print(f"Continue jogando! Ponto = {ponto}")
                print()
        else:
            if soma == ponto:
                print(f"Você tirou novamente o ponto {ponto}. Você venceu!")
                break
            elif soma == 7:
                print("Craps! Você perdeu!")
                break
            else:
                print(f"Continue jogando! Ponto = {ponto}")
                print()


jogo()
