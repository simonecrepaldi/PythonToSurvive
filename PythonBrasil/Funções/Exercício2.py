# Faça um programa para imprimir, para um n informado pelo usuário:
# 1
# 1 2
# 1 2 3
# .....
# 1 2 3 n n n...n
# para um n informado pelo usuário.
# Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
def linhas(n):
    y = 1
    while y <= n:
        x = 1
        while x <= y:
            print(x, end=" ")
            x += 1
        print("")
        y += 1


linhas(5)