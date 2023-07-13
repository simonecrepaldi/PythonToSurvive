# Exercício 1
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("Digite o raio do círculo: "))
area = 3.14 * (raio**2)
print(f"Área do círculo: {area:.2f}")


# Exercício 2
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
a = float(input(f"Informe o valor do produto 1: "))
b = float(input(f"Informe o valor do produto 2: "))
c = float(input(f"Informe o valor do produto 3: "))
if a < b and a < c:
    print(f"Você deve comprar o produto 1.")
elif b < a and b < c:
    print(f"Você deve comprar o produto 2.")
else:
    print(f"Você deve comprar o produto 3.")

# Outra forma de resolver
precos = list()
x = 1
while x <= 3:
    preco = float(input(f"Informe o valor do produto {x}: "))
    x += 1
    precos.append(preco)
index = precos.index(min(precos)) + 1
print(f"Você deve comprar o produto {index} que custa R${precos[index-1]:.2f}")


# Exercício 3
# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano = int(input("Informe o ano: "))
if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0) :
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")


# Exercício 4:
# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
x = 1
soma = 0
while x <= 3:
    nota = float(input(f"Digite a nota {x}: "))
    soma += nota
    x += 1
media = (soma/3)
if media == 10:
    print(f"Aprovado com distinção com a média {media:.2f}!")
elif media > 7:
    print(f"Aprovado com a média {media:.2f}!")
else:
    print(f"Reprovado com a média {media:.2}!")


# Exercício 5
# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
A = 80000
B = 200000
x = 0
while B > A:
    A *= 1.03
    B *= 1.015
    x += 1
print(f"Resposta: {x} anos")
