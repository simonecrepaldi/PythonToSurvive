# Exercício 2 -  Nome ao contrário em maiúsculas.
# Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input("Digite o seu nome: ").upper()
nome_contrario = nome[::-1]
print(f"Nome ao contrário: {nome_contrario}")


# Outra forma de resolver
nome = input("Digite o seu nome: ").upper()
novo_nome = ""
for i in range(len(nome)-1, -1, -1):
  novo_nome += nome[i]
print(novo_nome)
