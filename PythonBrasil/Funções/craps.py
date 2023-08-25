import random

def dados():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1 + d2


def jogar():
    rodada = 0
    pontos = 0

    while True:
        rodada += 1
        if rodada == 1:
            pontos = dados()
            print(f'Rodada 1: Pontos: {pontos}')
            if pontos == 7 or pontos == 11:
                print("7 ou 11: Ganhou!")
                break
            elif pontos == 2 or pontos == 3 or pontos == 12:
                print("2, 3 ou 12: Perdeu!")
                break

        else:
            resultado = dados()
            print(f'Rodada {rodada}: Resultado: {resultado}')
            if resultado == 7:
                print("Perdeu!")
                break

            elif resultado == pontos:
                print("Ganhou!")
                break



jogar()