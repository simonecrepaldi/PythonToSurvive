# x = 1
# while x <= 3:
#     print(x)
#     x

# x = 10
# while x >= 0:
#     print(x)
#     if x == 0:
#         print("Fogo!")
#     x = x - 1

# fim = int(input("Digite o último número a imprimir: "))
# x = 0
# while x <= fim:
#     if x % 2 == 0:
#         print(x)
#     x = x + 2

# fim = int(input("Digite o último número a imprimir: "))
# x = 1
# while x <= fim:
#     print(x)
#     x = x + 2
#
# fim = int(input("Digite o último número a imprimir: "))
# x = 1
# while x <= fim:
#     if x % 2 != 0:
#         print(x)
#     x = x + 2

# x = 3
# multiplo = 1
# while multiplo <= 10:
#     x = multiplo * 3
#     print(x)
#     multiplo = multiplo + 1

# n = int(input("Tabuada de: "))
# x = 1
# while x <= 10:
#     print(f"{n} * {x} = {n * x}")
#     x = x + 1

# pontos = 0
# questao = 1
# while questao <= 3:
#     resposta = input(f"Resposta da questao {questao}: ")
#     if questao == 1 and resposta == "b":
#         pontos = pontos + 1
#     if questao == 2 and resposta == "a":
#         pontos = pontos + 1
#     if questao == 3 and resposta == "d":
#         pontos = pontos + 1
#     questao = questao + 1
# print(f"O aluno fez {pontos} ponto(s)")

# pontos = 0
# questao = 1
# while questao <= 3:
#     resposta = input(f"Resposta da questao {questao}: ").lower()
#     if questao == 1 and (resposta == "c"):
#         pontos = pontos + 1
#     if questao == 2 and (resposta == "f"):
#         pontos = pontos + 1
#     if questao == 3 and (resposta == "c"):
#         pontos = pontos + 1
#     questao = questao + 1
# print(f"O aluno fez {pontos} ponto(s)")

# n = 1
# soma = 0
# while n <= 10:
#     x = int(input(f"Digite o {n} número: "))
#     soma = soma + x
#     n = n + 1
# print(f"Soma: {soma}")

# x = 1
# soma = 0
# while x <= 5:
#     n = int(input(f"{x} Digite o número: "))
#     soma = soma + n
#     x = x + 1
# print(f"Média: {soma/5:.2f}")

# x = x + 1 ---> x += 1
# x = x - 1 ---> x -= 1
# x = x * 1 ---> x *= 1
# x = x / 1 ---> x /= 1
# x = x ** 1 ---> x **= 1
# teste = 27
# teste //= 4
# print(f"{teste:.2f}")

# s = 0
# while True:
#     v = int(input("Digite um número a somar ou 0 para sair: "))
#     if v == 0:
#         break
#     s += v
# print(s)

# total = 0
# codigo_produto = -1
# while codigo_produto != 0:
#     codigo_produto = int(input("Digite o código do produto: "))
#     if codigo_produto == 0:
#         break
#     valor = 0
#     if codigo_produto == 1:
#         valor = 0.5
#     elif codigo_produto == 2:
#         valor = 1
#     elif codigo_produto == 3:
#         valor = 4
#     elif codigo_produto == 5:
#         valor = 7
#     elif codigo_produto == 9:
#         valor = 8
#     else:
#         print("Código inválido")
#     if valor > 0:
#         qtde_produto = int(input("Digite a quantidade do produto: "))
#         total += qtde_produto * valor
# print(f"O total a pagar é de {total:.2f}")


##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2020
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 05\exercicio-05-15.py
##############################################################################

apagar = 0
while True:
    código = int(input("Código da mercadoria (0 para sair): "))
    preço = 0
    if código == 0:
        break
    elif código == 1:
        preço = 0.50
    elif código == 2:
        preço = 1.00
    elif código == 3:
        preço = 4.00
    elif código == 5:
        preço = 7.00
    elif código == 9:
        preço = 8.00
    else:
        print("Código inválido!")
    if preço != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preço * quantidade)
print(f"Total a pagar R${apagar:8.2f}")
