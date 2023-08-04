def soma(L):
    total = 0
    for numero in L:
        total += numero
    return total


L = [1, 7, 2, 9, 15]
print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4]))
