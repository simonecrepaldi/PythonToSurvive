# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Informe a quantidade pescada em kg: "))
if peso > 50:
    excesso = peso - 50
    multa = 7 * excesso
    print(f"Total pescado {peso:.2f}kg, deverá ser pago R${multa:.2f} de multa pelo peso excendente de {excesso:.2f}kg.")
else:
    print(f"Como o total pescado de {peso:.2f}kg não ultrapassou 50kg permitidos, não será necessário pagar multa.")

