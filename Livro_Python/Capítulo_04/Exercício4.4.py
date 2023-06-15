# Exercício 4.4
salario = float(input("Digite o salário: R$"))
aumento = 0
if salario > 1250:
    aumento = salario * 0.10
    salariofinal = salario + aumento
if salario <= 1250:
    aumento = salario * 0.15
    salariofinal = salario + aumento
print(f"O aumento será de R${aumento:.2f}, portanto o salário final será de R${salariofinal:.2f}")
