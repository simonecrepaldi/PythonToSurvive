dívida = float(input("Valor da dívida: R$"))
juros = float(input("Juros mensal (em %): "))
pagamento = float(input("Valor a ser pago mensalmente: R$"))
total = 0
meses = 0
inicial = dívida

while dívida >= 0:
    if dívida == 0:
        break
    else:
        if (dívida - pagamento) < 0:
            pagamento = dívida
            total = total + pagamento

        else:
            dívida = (dívida - pagamento) * (1 + (juros/100))
            total = total + pagamento
            meses += 1
            print(f"{dívida:.2f}")

print(f"> Total pago: R$ {total:.2f}")
print(f"> Número de meses: {meses}")
print(f"> Total de juros: R${(total - inicial):.2f}")
