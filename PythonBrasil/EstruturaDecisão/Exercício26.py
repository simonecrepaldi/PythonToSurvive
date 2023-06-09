# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litro = float(input("Quantidade de combustível (em litros): "))

while True:
    tipo = input("Informe o tipo de combustível (A - álcool / G - gasolina): ").upper()
    if tipo == "A":
        preco_alcool = 1.90
        if litro < 20:
            precototal = (preco_alcool * litro) * 0.97
        else:
            precototal = (preco_alcool * litro) * 0.95
        break
    elif tipo == "G":
        preco_gasolina = 2.50
        if litro < 20:
            precototal = (preco_gasolina * litro) * 0.96
        else:
            precototal = (preco_gasolina * litro) * 0.94
        break
    else:
        print("Tipo inválido!")

print(f"Valor a ser pago: R$ {precototal:.2f}")