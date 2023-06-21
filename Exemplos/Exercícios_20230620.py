# Exercícios utilizando "For" - 20/06/2023

# Exercício 1:
# Imprima os números de 1 a 10 usando um loop for.
for a in range(1,11):
    print(a)


# Exercício 2:
# Dado um lista de nomes, imprima cada nome em uma linha separada usando um loop for.
nomes = ["Ana", "Pedro", "João", "Gabriel", "Rafaela"]
for nome in nomes:
    print(nome)


# Exercício 3:
# Calcule e imprima a soma dos números de 1 a 100 usando um loop for.
soma = 0
for a in range(1, 101):
    soma += a
print(soma)


# Exercício 4:
# Dada uma string, imprima cada caractere em uma linha separada usando um loop for.
string = "string"
for letra in string:
    print(letra)


Exercício 5:
Dada uma lista de números, imprima apenas os números pares usando um loop for.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)

# Usando um range para criar a lista
for numero in range(0, 11):
    if numero % 2 == 0:
        print(numero)


Exercício 6:
Dado um número inteiro digitado pelo usuário, imprima a tabuada desse número até o valor 10.
numero = int(input("Digite um número: "))
for a in range(1, 11):
    print(f"{numero} x {a} = {a*numero}")


# Exercício 7:
# Dada uma lista de números, calcule e imprima o quadrado de cada número utilizando um loop for.
lista = [3, 5, 7, 9]
for numero in lista:
    print(f"{numero**2}")


# Exercício 8:
# Dada uma lista de números, calcule e imprima a média dos elementos utilizando um loop for.
numeros = [2, 8, 15, 23, 36]
soma = 0
for a in numeros:
    soma += a
print(soma/len(numeros))
