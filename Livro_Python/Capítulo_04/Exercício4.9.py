# Exercício 4.9
valor = float(input("Informe o valor de venda da casa: R$"))
salário = float(input("Informe o seu salário: R$"))
anos = int(input("Informe a quantidade de anos a pagar: "))
prestação = (valor / (anos * 12))
if prestação > salário * 0.30:
    print("Empréstimo negado!")
else:
    print(f"O valor de R${valor} deverá ser pago em {anos*12} prestações mensais de R${prestação:.2f}!")
