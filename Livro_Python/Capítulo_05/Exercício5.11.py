depósito = float(input("Valor inicial do depósito: R$"))
taxa_juros = float(input("Taxa de juros (em %): "))
mês = 1
valor = depósito
juros = 0

print("Valores dos primeiros 24 meses:")
while mês <= 24:
    juros = valor * (taxa_juros/100)
    valor = valor + juros
    print(f"> Valor atualizado após o mês {mês}: R${valor:.2f}")
    mês +=1

print(f">>> Total ganho com juros no período: R${(valor - depósito):.2f}")


# Resolução Tocha
x = int(input("Depósito: "))
y = int(input("Juros: "))
mês = 1
inicial = x
while mês <= 24:
    x *= 1 + (y/100)
    print(f"Mês {mês}: {x:.2f}")
    mês += 1
print(f"Total ganho com juros: R${x - inicial:.2f}")
