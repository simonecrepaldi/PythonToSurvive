# Exercícios sobre Tuplas - 15/06/2023

# Exercício 1:
# Crie uma tupla chamada "meses" com os nomes dos meses do ano. Em seguida, imprima o terceiro mês da tupla.
# meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
#          "Julho", "Agosto", "Setembro", "Novembro", "Dezembro")
# print(meses[2])


# Exercício 2
# Crie uma tupla chamada "coordenadas" com as coordenadas x e y de um ponto.
# Solicite ao usuário que digite os valores das coordenadas e armazene-os na tupla.
# Em seguida, imprima as coordenadas do ponto.
# x = float(input("Digite a coordenada x do ponto: "))
# y = float(input("Digite a coordenada y do ponto: "))
# coordenadas = (x, y)
# print(f"Coordenadas do ponto: x = {coordenadas[0]} e y = {coordenadas[1]}")
# print("Coordenadas:", coordenadas)


# Exercício
# Crie uma tupla chamada "numeros" com alguns números inteiros.
# Utilizando um loop for, calcule e imprima a soma de todos os números da tupla.
# numeros = (1, 2, 4, 6, 8)
# soma = 0
# for x in numeros:
#     soma += x
# print(f"Soma = {soma}")


# Exercício 4
# Crie uma tupla chamada "ponto" com as coordenadas x, y e z de um ponto no espaço tridimensional.
# Imprima cada coordenada em uma linha separada.
# ponto = (1, 2, 3)
# print("Coordenadas do ponto:")
# print(f"x = ", ponto[0])
# print(f"y = ", ponto[1])
# print(f"z = ", ponto[2])

# Outra forma de resolver usando o for
# for item in ponto:
#     print(item)


# Exercício 5
# Crie uma tupla chamada "nomes" com alguns nomes de pessoas.
# Solicite ao usuário que digite um nome e verifique se o nome está presente na tupla.
# Se estiver, imprima uma mensagem informando que o nome foi encontrado;
# caso contrário, exiba uma mensagem informando que o nome não foi encontrado.
# nomes = ("Maria", "João", "Ana", "Pedro")
# nome = input("Digite um nome: ").title()
#
# if nome in nomes:
#     print(f"O nome {nome} foi encontrado na tupla.")
# else:
#     print(f"O nome {nome} não foi encontrado na tupla.")
