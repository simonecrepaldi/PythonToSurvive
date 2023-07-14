# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

numeroParcelas = 0
parcelasTotal = 0
valorTotal = 0
def inicioPrograma():
    while True:
        prestacao = float(input("Informe o valor da prestação: R$"))
        if prestacao == 0:
            imprimeRelatorio()
            break
        else:
            dias_atraso = int(input("Informe os dias em atraso: "))
            valorPagamento(prestacao, dias_atraso)

def valorPagamento(valorPrestacao, dias):
    if dias == 0:
        juros = 0
        multa = 0
    else:
        juros = 0.001 * dias * valorPrestacao
        multa = 0.03 * valorPrestacao

    valorFinal = valorPrestacao + multa + juros
    incluiRelatorio(valorFinal)

def incluiRelatorio(total):
    global valorTotal
    global numeroParcelas
    valorTotal += total
    numeroParcelas += 1

def imprimeRelatorio():
    print("Valor total:", valorTotal)
    print("Número de parcelas:", numeroParcelas)


inicioPrograma()



# Outra forma de escrever o programa
def inicioPrograma():
    valorTotal = 0
    numeroParcelas = 0

    while True:
        prestacao = float(input("Informe o valor da prestação: R$"))
        if prestacao == 0:
            break

        dias_atraso = int(input("Informe os dias em atraso: "))
        valorFinal = calcularValorPagamento(prestacao, dias_atraso)
        valorTotal += valorFinal
        numeroParcelas += 1

    imprimeRelatorio(valorTotal, numeroParcelas)

def calcularValorPagamento(valorPrestacao, dias):
    juros = 0.001 * dias * valorPrestacao if dias > 0 else 0
    multa = 0.03 * valorPrestacao if dias > 0 else 0
    valorFinal = valorPrestacao + multa + juros
    return valorFinal

def imprimeRelatorio(valorTotal, numeroParcelas):
    print("Valor total:", valorTotal)
    print("Número de parcelas:", numeroParcelas)


inicioPrograma()
