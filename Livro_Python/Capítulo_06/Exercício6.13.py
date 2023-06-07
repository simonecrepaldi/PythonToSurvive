T = [-10, -8, 0, 1, 2, 5, -2, -4]
soma = 0
menor = T[0]
maior = [0]
for e in T:
    soma += e
    if e < menor:
        menor = e
    if e > maior:

print(f'{soma/len(T):.1f}')