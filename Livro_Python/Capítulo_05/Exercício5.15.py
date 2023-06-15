valor_total = 0
while True:
    codigo_produto = int(input("Código do produto (Digite 0 para encerrar): "))
    valor = 0
    if codigo_produto == 0:
        break
    elif codigo_produto == 1:
        valor = 0.50
    elif codigo_produto == 2:
        valor = 1.00
    elif codigo_produto == 3:
        valor = 4.00
    elif codigo_produto == 5:
        valor = 7.00
    elif codigo_produto == 9:
        valor = 8.00
    else:
        print(">>> Código inválido! <<<")
    if valor !=0:
        qtdade_comprada = int(input("Quantidade do produto: "))
        valor_total = valor_total + (valor * qtdade_comprada)
print(f">>> Valor total a pagar: R${valor_total:5.2f}")
