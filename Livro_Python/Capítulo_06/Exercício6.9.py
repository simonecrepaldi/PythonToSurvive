L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))
x = y = 0
while x < len(L):
    if L[x] == p:
        break
    x += 1
while y < len(L):
    if L[y] == v:
        break
    y += 1

if x < len(L) or y < len(L):
    if x < y:
        print(f"Primeiro valor ({p}) encontrado na posição {x}")
    elif x == y:
        print(f"Primeiro valor igual ao segundo encontrado na posição {x}")
    else:
        print(f"Segundo valor ({v}) encontrado na posição {y}")
else:
    print(f"{p} e {v} não foram encontrados")
