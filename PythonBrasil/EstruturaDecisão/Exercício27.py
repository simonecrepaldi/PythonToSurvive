# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morangos = float(input("Quantidade de morangos (em kg): "))
macas = float(input("Quantidade de maçãs (em kg): "))

if morangos <= 5:
    preco_morango = 2.5
else:
    preco_morango = 2.2
if macas <= 5:
    preco_maca = 1.8
else:
    preco_maca = 1.5

peso_total = morangos + macas
preco_total = (morangos * preco_morango) + (macas * preco_maca)

if peso_total > 8 or preco_total > 25:
    desconto = preco_total * 0.10
else:
    desconto = 0
print(f"Total a pagar: R${preco_total-desconto:.2f}")



