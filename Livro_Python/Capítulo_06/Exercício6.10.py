L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))
x = y = 0

while x < len(L):
    if L[x] == p:
        print(f"Primeiro valor ({p}) encontrado na posição {x}")
        break
    else:
        print(f"{p} não foi encontrado na lista")
        break
x += 1

while y < len(L):
    if L[y] == v:
        print(f"Segundo valor ({v}) encontrado na posição {y}")
        break
    else:
        print(f"{v} não foi encontrado na lista")
        break
y += 1