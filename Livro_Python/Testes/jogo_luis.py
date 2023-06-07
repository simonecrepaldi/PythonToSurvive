import random

qtde_partidas = 10
partida_atual = 0
total_de_palpites = 0

while partida_atual < qtde_partidas:
    partida_atual += 1
    print(f"Esta é a partida {partida_atual}.")

    secreto = random.randint(1, 100)
    palpite_atual = 0
    ultimo_palpite = 0

    chances_por_partida = 7
    chance_atual = 0

    while chance_atual < chances_por_partida:
        chance_atual += 1
        print(f"Chance {chance_atual} de {chances_por_partida}")

        ultimo_palpite = palpite_atual
        palpite_atual = int(input("Digite um número entre 1 e 100: "))

        if palpite_atual == secreto:
            print(f"Acertou em {chance_atual} tentativas!")
            total_de_palpites += chance_atual
            break

        elif palpite_atual < secreto:
            print(f"O número secreto é maior que {palpite_atual}.")
        else:
            print(f"O número secreto é menor que {palpite_atual}.")

    if secreto != palpite_atual:
        total_de_palpites += chance_atual
        print(f"Perdeu a partida {partida_atual}. O número secreto era {secreto}.")

print(f"Terminou jogando {partida_atual} partidas com uma média de {total_de_palpites/partida_atual} palpites por partida.")
