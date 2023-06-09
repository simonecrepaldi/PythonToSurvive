# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valor_hora = float(input("Informe o valor/hora do seu trabalho: R$"))
horas_trabalho = float(input("Quantidade de horas trabalhada no mês: "))
salario_bruto = valor_hora * horas_trabalho
IR = 0
sindicato = salario_bruto * 0.03
INSS = salario_bruto * 0.10
FGTS = salario_bruto * 0.11

if salario_bruto <= 900:
    IR = 0
elif salario_bruto <= 1500:
    IR = 0.05
elif salario_bruto <= 2500:
    IR = 0.10
else:
    IR = 0.20

salario_liquido = salario_bruto - IR - INSS - sindicato
descontos = (IR * salario_bruto) + INSS + sindicato
print(f"Salário Bruto ({valor_hora:.2f}h x R${horas_trabalho:.2f}): R${salario_bruto:.2f}")
print(f"(-) IR ({IR*100:.0f}%): R${salario_bruto * IR:.2f}")
print(f"(-) INSS (10%): R${INSS:.2f}")
print(f"(-) Sindicato (3%): R${sindicato:.2f}")
print(f"FGTS (11%): R${FGTS:.2f}")
print(f"Total de descontos: R${descontos:.2f}")
print(f"Salário Líquido: R${salario_bruto - descontos:.2f}")