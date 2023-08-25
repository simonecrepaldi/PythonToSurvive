# Faça um programa para imprimir, para um n informado pelo usuário:
# 1
# 2 2
# 3 3 3
# .....
# n n n n n n...n
# Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def impressao(n):
    y = 1
    while y <= n:
        x = 1
        while x <= y:
            print(y, end=" ")
            x += 1
        print("")
        y += 1


impressao(5)
