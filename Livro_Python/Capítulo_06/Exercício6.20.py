# Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como a versão após alterações.
# Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
# os elementos que não mudaram
# os novos elementos
# os elementos que foram removidos

Lista_inicial = [0, 3, 8, 15, 18, 20]
Lista_alterada = [1, 2, 3, 6, 15, 18]
a = set(Lista_inicial)
b = set(Lista_alterada)
c = a & b
d = b - a
e = a - b

print(a)
print(b)
print(f"Os elementos que não foram alterados da lista: {c}")
print(f"Os novos elementos: {d}")
print(f"Os elementos que foram removidos da lista: {e}")
