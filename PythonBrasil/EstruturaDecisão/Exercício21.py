# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("Valor a ser sacado (valor máximo R$600 e valor mínimo R$10): R$"))
valor = saque
nota_atual = 100
qtd_notas = 0

while True:
    if valor >= 100:
        qtd_notas += 1
        valor = valor - nota_atual
    else:
        nota_atual = 50
        if valor >= 50:
            qtd_notas += 1
            valor = valor - nota_atual
        else:
            break

print(f"Para sacar a quantia de R${saque}, o programa fornece {qtd_notas} notas de R${nota_atual}")

