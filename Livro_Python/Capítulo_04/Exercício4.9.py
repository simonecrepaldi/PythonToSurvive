# Exercício 4.9
valor = float(input("Informe o valor de venda da casa: R$"))
salario = float(input("Informe o seu salário: R$"))
anos = int(input("Informe a quantidade de anos a pagar: "))
prestacao = (valor / (anos * 12))
if prestacao > salario * 0.30:
    print("Empréstimo negado!")
else:
    print(f"O valor de R${valor} deverá ser pago em {anos*12} prestações mensais de R${prestacao:.2f}!")
