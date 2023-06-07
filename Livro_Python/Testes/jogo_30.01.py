import random

secreto = random.randint(1, 100)
tentativa = 0
palpite = 0
limite = 3

while tentativa < limite:
    tentativa += 1
    print(f'>>> Tentativa {tentativa} <<<')

    palpite = int(input("Digite o seu palpite (1 a 100): "))

    if secreto == palpite:
        print(f">>> Acertou na tentativa {tentativa}!")
        break
    else:
        if limite == tentativa:
            print(f">>> Perdeu! Você atingiu o limite de {limite} tentativas. O número era {secreto}.")
            break
        else:
            if secreto > palpite:
                print("O número é maior que o palpite")
            else:
                print("O número é menor que o palpite")