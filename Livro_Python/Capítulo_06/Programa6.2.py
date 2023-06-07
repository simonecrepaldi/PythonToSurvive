notas = [0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 5:
    notas[x] = float(input(f"Nota {x + 1}: "))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print(f"Nota {x + 1}: {notas[x]:6.2f}")
    x += 1
print(f"Média: {soma / x:5.2f}")
