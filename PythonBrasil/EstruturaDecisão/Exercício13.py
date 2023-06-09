# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

numero = int(input("Digite um número inteiro: "))
if numero == 1:
    print(f'O número 1 corresponde ao Domingo.')
elif numero == 2:
    print(f'O número 2 corresponde a Segunda.')
elif numero == 3:
    print(f'O número 3 corresponde a Terça.')
elif numero == 4:
    print(f'O número 4 corresponde a Quarta.')
elif numero == 5:
    print(f'O número 5 corresponde a Quinta.')
elif numero == 6:
    print(f'O número 6 corresponde a Sexta.')
elif numero == 7:
    print(f'O número 7 corresponde ao Sábado.')
else:
    print(f"O número {numero} é inválido!")