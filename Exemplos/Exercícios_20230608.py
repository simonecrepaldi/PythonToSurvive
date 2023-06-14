# Exercícios de Dicionários - 08/06/2023

# Exercício 1:
# Crie um dicionário chamado "frutas" com as seguintes chaves e valores:
# "maçã" - 3, "banana" - 6, "laranja" - 4
# Em seguida, imprima o valor associado à chave "banana".

# frutas = {"maça": 3, "banana": 6, "laranja": 4}
# print(frutas["banana"])


# Exercício 2:
# Crie um dicionário chamado "estoque" com as seguintes chaves e valores:
# "camisetas" - 10, "calças" - 5, "sapatos" - 2.
# Utilizando um loop for, imprima cada chave e valor do dicionário em linhas separadas.

# estoque = {"camisetas": 10, "calças": 5, "sapatos": 2}
# for item, quantidade in estoque.items():
#     print(f"{item} - {quantidade}")


# Exercício 3:
# Crie um dicionário chamado "precos" com as seguintes chaves e valores:
# "maçã" - 2.5, "banana" - 1.8, "laranja" - 3.1.
# Utilizando um loop for, calcule e imprima o preço total de todos os itens.

# precos = {"maçã": 2.5, "banana": 1.8, "laranja": 3.1}
# total = 0
# for valor in precos.values():
#     valor_produto = valor
#     total += valor_produto
#
# print(f"Preço total: R${total:.2f}")


#Exercício 4:
#Crie um dicionário chamado "alunos" com as seguintes chaves e valores:
# "João" - 8, "Maria" - 9, "Pedro" - 7.
# Utilizando um loop for, calcule e imprima a média das notas dos alunos.

# alunos = {"João": 7.5, "Maria": 4, "Pedro": 6.3}
# soma = 0
# for nota in alunos.values():
#     soma += nota
# media = (soma/(len(alunos)))
# print(f"A média dos alunos é {media:.2f}")


#Exercício 5:
#Crie um dicionário chamado "palavras" com as seguintes chaves e valores:
# "python" - 6, "programação" - 12, "linguagem" - 9.
# Utilizando um loop for, imprima apenas as chaves que possuem um número par de caracteres.

# palavras = {"python": 6, "programação": 11, "linguagem": 9}
# for chave in palavras.keys():
#     resto = len(chave)%2
#     if resto == 0:
#         print(chave)

# resolução mais simples
# for palavra in palavras:
#     if len(palavra) % 2 == 0:
#         print(palavra)


# Exercício 6:
# Crie um dicionário chamado "estoque" com as seguintes chaves e valores:
# "camisetas" - 20, "calças" - 15, "sapatos" - 10.
# Usando um 'loop' for, verifique se algum item do estoque possui uma quantidade menor ou igual a que 10.
# Se houver, imprima o nome do item.

# estoque = {"camisetas": 20, "calças": 15, "sapatos": 10}
# for produto, quantidade in estoque.items():
#     if quantidade <= 10:
#         print(f"{produto}")


# Exercício 7:
# Crie um dicionário chamado "agenda" com os seguintes pares de chaves e valores:
# Ana" - "555-1234", # "Maria" - "555-5678", "João" - "555-9876".
# Solicite ao usuário que digite um nome e, em seguida, verifique se o nome está presente na agenda.
# Se estiver, imprima o número de telefone correspondente; caso contrário, exiba uma mensagem informando que o nome não foi encontrado.

# agenda = {"Ana": "555-1234", "Maria": "555-5678", "João": "555-9876"}
# nome = input("Digite o nome desejado: ").title()
# if nome in agenda:
#     print(f"{nome} - Telefone: {agenda[nome]}")
# else:
#     print("Nome não encontrado!")


# Exercício 8:
# Crie um dicionário chamado "notas" com os seguintes pares de chaves e valores:
# "João" - [7, 8, 9], "Maria" - [6, 7, 8], "Pedro" - [9, 9, 10].
# Utilizando um 'loop' for, calcule e imprima a média das notas de cada aluno.

# notas = {"João": [7, 8, 9],
#          "Maria": [6, 7, 8],
#          "Pedro": [9, 9, 10]}
# for aluno, notas_aluno in notas.items():
#     soma_aluno = 0
#     for nota in notas_aluno:
#         soma_aluno += nota
#     media = soma_aluno/len(notas_aluno)
#     print(f"{aluno} - Média: {media:.2f}")


# Exercício 9:
# Crie um dicionário chamado "estoque" com as seguintes chaves e valores: "camisetas" - 10, "calças" - 15,
# "sapatos" - 20. Solicite ao usuário que digite o nome de um item e a quantidade desejada. Em seguida, verifique se o
# item existe no estoque e se há a quantidade solicitada disponível. Se estiver, atualize o estoque subtraindo a
# quantidade desejada; caso contrário, exiba uma mensagem informando que o item não está disponível ou que a quantidade
# desejada não está disponível.

# estoque = {"camisetas": 10, "calças": 15, "sapatos": 20}
# while True:
#     item = input("Digite o item desejado (fim para encerrar): ")
#     if item == "fim":
#         print("Venda finalizada!")
#         break
#     if item in estoque:
#         quantidade = int(input(f"Digite a quantidade desejada de {item}: "))
#         if quantidade <= estoque[item]:
#             estoque[item] -= quantidade
#             print()
#             print(f"Estoque atualizado: {estoque}")
#         else:
#             print(f"Quantidade indisponível no estoque.")
#             print(f"Estoque atualizado: {estoque}")
#             print()
#     else:
#         print(f"{item} não está disponível.")


# Exercício 10:
# Crie um dicionário chamado "palavras" com as seguintes chaves e valores: "python" - 6, "programação" - 12,
# "linguagem" - 9. Usando um 'loop' for, imprima apenas as palavras cujo comprimento seja menor
# que o valor associado a elas.

# palavras = {"python": 6, "programação": 12, "linguagem": 9}
# for palavra, valor in palavras.items():
#     if len(palavra) < valor:
#         print(palavra)
