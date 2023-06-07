import random

secreto = random.randint(1, 15)
tentativa = 0
palpite = 0
limite = 3

while tentativa < limite:
    tentativa += 1
    print(secreto)
    print(f'Tentativa {tentativa}')
    palpite = int(input("Digite o palpite (1 a 15): "))

    if secreto == palpite:
        print(f"Acertou na tentativa {tentativa}!")
        break
    elif secreto =! palpite:
            if secreto > palpite:
                print("O número é maior que o palpite")
            elif secreto < palpite:
                print("O número é menor que o palpite")
        else:
            print(f"Perdeu. Passou do limite de {limite} tentativas. O número era {secreto}.")
            break
