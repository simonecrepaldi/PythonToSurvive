# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
x = 1
lista = []
soma = 0
while x < 5:
    nota = float(input("Informe a nota: "))
    soma += nota
    lista.append(nota)
    x += 1

for i, n in enumerate(lista):
    print(f"Nota {i+1}: {n} ")
print(f"Média: {soma/len(lista)}")
