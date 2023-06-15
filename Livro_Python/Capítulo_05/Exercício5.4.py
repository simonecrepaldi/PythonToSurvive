fim = int(input("Digite o último número a imprimir: "))
x = 1

while x <= fim:
    print(x)
    x = x + 2


# Outra forma de escrever
fim = int(input("Digite o último número a imprimir: "))
x = 1

while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 2