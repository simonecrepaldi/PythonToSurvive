# Exercício 4.10
consumo = int(input("Informe o consumo de energia em kWh: "))
tipo = input("Tipo da instalação (R - Residencial, I - Industrial ou C - Comercial): ").upper()
valor = 0
if tipo == 'R' or 'RESIDENCIAL':
    if consumo < 500:
        valor =  consumo * 0.40
    else:
        valor = consumo * 0.65
elif tipo == 'I' or 'INDUSTRIAL':
    if consumo < 1000:
        valor = consumo * 0.55
    else:
        valor = consumo * 0.60
elif tipo == 'C' or 'COMERCIAL':
    if consumo < 5000:
        valor = consumo * 0.55
    else:
        valor = consumo * 0.60
else:
    print("Tipo de instalação inválida!")
print(f"Valor a ser pago pelo consumo de {consumo}kWh será de R${valor:.2f}")
