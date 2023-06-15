x = int(input("Depósito: R$"))
y = int(input("Juros (em %): "))
mensal = int(input("Valor mensal: R$"))

mês = 1
inicial = x

while mês <= 24:
    x = x + mensal
    x *= 1 + (y/100)
    print(f"Mês {mês}: {x:.2f}")
    mês += 1
print(f"Total ganho com juros: R${x - inicial - (24*mensal):.2f}")
