# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = num1

while True:
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3
    break

menor = num1

while True:
    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3
    break

meio = num1 + num2 + num3 - maior - menor

print(maior, meio, menor)




a = float(input('Escreva um número: '))
b = float(input('Escreva um número: '))
c = float(input('Escreva um número: '))

if a < c:
    a, c = c, a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

print(f'A ordem decrescente é {a}, {b} e {c}')