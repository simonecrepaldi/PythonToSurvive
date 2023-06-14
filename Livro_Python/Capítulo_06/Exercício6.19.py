# Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
# os valores comuns às duas listas (intersecção &)
# os valores que só existem na primeira (diferença -)
# os valores que existem apenas na segunda (diferença -)
# uma lista com os elementos não repetidos das duas listas
# a primeira lista sem os elementos repetidos na segunda

ListaA = [0, 1, 2, 3, 4, 5]
ListaB = [1, 3, 5, 7, 9]

a = set(ListaA)
b = set(ListaB)
c = a & b
d = (a|b) - c
e = a - c

print(f"Lista A: {ListaA}")
print(f"Lista B: {ListaB}")
print()
print(f"Valores comuns às duas listas: {c}")
print(f"Valores que só existem na primeira lista: {a-b}")
print(f"Valores que existem apenas na segunda: {b-a}")
print(f"Lista com os elementos que não se repetem: {d}")
print(f"Lista A sem os elementos repetidos na Lista B: {e}")
