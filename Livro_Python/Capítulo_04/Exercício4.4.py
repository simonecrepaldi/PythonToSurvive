# Exercício 4.4
salário = float(input("Digite o salário: R$"))
aumento = 0
if salário > 1250:
    aumento = salário * 0.10
    saláriofinal = salário + aumento
if salário <= 1250:
    aumento = salário * 0.15
    saláriofinal = salário + aumento
print(f"O aumento será de R${aumento:.2f}, portanto o salário final será de R${saláriofinal:.2f}")