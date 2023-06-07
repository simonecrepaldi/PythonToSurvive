notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 7:
    notas[x] = float(input(f"Nota {x + 1}: "))
    soma += notas[x]
    x += 1

y = 0
while y < 7:
    print(f"Nota {y + 1}: {notas[y]:3.2f}")
    y += 1
print(f"Média: {soma/y:3.2f}")
