# Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
# os valores comuns às duas listas
# os valores que só existem na primeira
# os valores que existem apenas na segunda
# uma lista com os elementos não repetidos das duas listas
# a primeira lista sem os elementos repetidos na segunda

ListaA = [0, 1, 2, 3, 4, 5]
ListaB = [1, 3, 5, 7, 9]
a = set(ListaA)
b = set(ListaB)
ListaC = (a-b)|(b-a)

print(f"Valores comuns às duas listas: ")
print(f"Valores que só existem na primeira lista: {a-b}")
print(f"Valores que existem apenas na segunda: {b-a}")
print(f"Lista com os elementos que não se repetem: {ListaC}")
print(f"ListaA sem os elementos repetidos na ListaB: ")
