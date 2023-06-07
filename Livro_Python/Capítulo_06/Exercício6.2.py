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

ListaC = ListaA[:]
ListaC.extend(ListaB)

print(f"> Lista C = Lista A + Lista B: {ListaC}")