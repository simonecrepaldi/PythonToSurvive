soma = 0
cont = 0
média = 0
número = int(input("Digite um número inteiro: "))

while número != 0:
    soma = soma + número
    cont += 1
    número = int(input("Digite um número inteiro (Digite 0 para sair): "))
média = soma / cont

print(f"> Quantidade de números digitados: {cont}")
print(f"> Soma = {soma}")
print(f"> Média = {média:.1f}")
