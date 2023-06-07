# Programa 4.5 - Conta de telefone com três faixas de preço
minutos = int(input("Quantos minutos você utilizou este mês: "))
if minutos < 200:
    preço = minutos * 0.20
else:
    if minutos < 400:   # Preço para >= 200min e < 400min
        preço = minutos * 0.18
    else:   # Preço para mais de 400min
        preço = minutos * 0.15
print(f"Você vai pagar este mês R${preço:.2f}, por {minutos} minutos.")