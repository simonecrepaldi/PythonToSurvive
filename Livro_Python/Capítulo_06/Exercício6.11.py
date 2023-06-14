# Alterar o programa 6.6, usando o FOR
L = []
while True:
    n = int(input("Digite um número (O sai): "))
    if n == 0:
        break
    L.append(n)

for c in L:
    print(c)
