ListaA = []
ListaB = []

while True:
    numeros = int(input("Digite um número para a Lista A (0 para parar): "))
    if numeros == 0:
        break
    ListaA.append(numeros)
while True:
    numeros = int(input("Digite um número para a Lista B (0 para parar): "))
    if numeros == 0:
        break
    ListaB.append(numeros)

ListaAB = ListaA[:]
ListaAB.extend(ListaB)
ListaC = []

ab = 0
while ab < len(ListaAB):
    c = 0
    while c < len(ListaC):
        if ListaAB[ab] == ListaC[c]:
            break
        c += 1
    if c == len(ListaC):
        ListaC.append(ListaAB[ab])
    ab += 1

print(f"Lista C: {ListaC}")