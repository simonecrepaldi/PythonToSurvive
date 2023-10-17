    # Jogo da velha

def imprime(lista):
    for i in lista:
        if i == 1:
            print("o|", end="")
        elif i == 10:
            print("x|", end="")
        else:
            print(" |", end="")
    print()

lista = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]
jogadorA = True

while True:
    jogada = int(input("Escolha a sua posição (0 a 8): "))
    if lista[jogada] != 0:
        print("Cara, preste mais atenção no jogo!")
        continue

    valor = 1
    if not jogadorA:
        valor = valor * 10
    jogadorA = not jogadorA
    lista[jogada] = valor

    linha1 = lista[0:3]
    linha2 = lista[3:6]
    linha3 = lista[6:9]
    coluna1 = lista[0:9:3]
    coluna2 = lista[1:9:3]
    coluna3 = lista[2:9:3]
    diagonal1 = lista[2:8:2]
    diagonal2 = lista[::4]

    imprime(linha1)
    imprime(linha2)
    imprime(linha3)

    ganhouA = ganhouB = 0


    ganhouB = sum(linha1) == 30 or sum(linha2) == 30 or sum(linha3) == 30 or sum(coluna1) == 30 or sum(coluna2) == 30 or sum(coluna3) == 30 or sum(diagonal1) == 30 or sum(diagonal2) == 30
    ganhouA = sum(linha1) == 3 or sum(linha2) == 3 or sum(linha3) == 3 or sum(coluna1) == 3 or sum(coluna2) == 3 or sum(coluna3) == 3 or sum(diagonal1) == 3 or sum(diagonal2) == 3

    if ganhouA:
        print("Parabéns, jogador A!")
        break

    if ganhouB:
        print("Parabéns, jogador B!")
        break

    if all(lista):
        print("Jogo encerrado! Ninguém ganhou!")
        break
