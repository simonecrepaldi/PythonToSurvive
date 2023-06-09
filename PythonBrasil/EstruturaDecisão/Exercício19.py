# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input("Digite um número inteiro menor que 1000: "))


centena = numero // 100
dezena = ((numero // 10) % 10)
unidade = numero % 10

if centena == 1:
    a = 'centena,'
elif centena == 0:
    centena = ''
    a = ''
else:
    a = 'centenas,'
if dezena == 1:
    b = 'dezena'
elif dezena == 0:
    dezena = ''
    b = ''
else:
    b = 'dezenas'
if unidade == 1:
    c = 'unidade'
elif unidade == 0:
    unidade = ''
    c = ''
else:
    c = 'unidades'

print(f"{numero} = {centena} {a} {dezena} {b} e {unidade} {c}.")

