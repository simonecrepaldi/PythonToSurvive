# https://wiki.python.org.br/EstruturaSequencial
# Ex. 12
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
# altura = float(input('Digite seu altura: '))
# peso_ideal = (72.7 * altura) - 58
# print(f"O peso ideal para a altura {altura}m é de {peso_ideal:.2f} Kg")

# Ex. 13
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# Para outros: (65.1*h) - 48.2
# altura = float(input('Digite seu altura: '))
# genero = input('Digite H para homem, M para mulher ou outra letra para outros: ')
# if genero == 'h' or genero == 'H':
#     coef1 = 72.7
#     coef2 = 58
#     desc = 'um homem'
# elif genero == 'm' or genero == 'M':
#     coef1 = 62.1
#     coef2 = 44.7
#     desc = 'uma mulher'
# else:
#     coef1 = 65.1
#     coef2 = 48.2
#     desc = 'alguém'
# peso_ideal = (coef1 * altura) - coef2
# print(f"O peso ideal para {desc} de altura {altura:.2f} m é de {peso_ideal:.2f} Kg")

# Ex. 14
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia
# a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além
# do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
# mensagens adequadas.
# multa_kg = 4
# peso = float(input('Digite o peso de peixes: '))
# if peso < 50:
#     excesso = 0
#     multa = 0
# else:
#     excesso = peso - 50
#     multa = excesso * multa_kg
# print(f'Peso total (em Kg): {peso:.2f} Kg')
# print(f'Excesso: {excesso:.2f} Kg')
# print(f'Multa: R$ {multa:.2f}')

# Ex. 15
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

# valor_hora = float(input('Digite o valor da hora (R$): '))
# horas_trabalhadas = float(input('Digite o total de horas trabalhadas por mês: '))
#
# salario_bruto = valor_hora * horas_trabalhadas
# ir = salario_bruto * 0.11
# inss = salario_bruto * 0.08
# sindicato = salario_bruto * 0.05
#
# salario_liquido = salario_bruto - ir - inss - sindicato
#
# print(f'Salário bruto: R$ {salario_bruto:.2f}')
# print(f'IR (11%): R$ {ir:.2f}')
# print(f'INSS (8%): R$ {inss:.2f}')
# print(f'Sindicato (5%): R$ {sindicato:.2f}')
# print(f'Salário líquido: R$ {salario_liquido:.2f}')
