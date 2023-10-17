# # Exercício 1 - Número de Palavras
# Escreva um programa que conte o número de palavras em uma frase fornecida pelo usuário.

def contarPalavras(frase):
    palavras = frase.split(" ")
    return len(palavras)

def inicio():
    entrada = input("Digite a frase: ")
    print(f"A frase tem {contarPalavras(entrada)} palavras.")


inicio()


# Exercício 2 - Média de Notas
# Peça ao usuário para inserir várias notas e, em seguida, calcule e exiba a média dessas notas.

def media(soma_notas, qt_notas):
    return soma_notas/qt_notas

def notas():
    soma = x = 0
    while True:
        nota = int(input("Informe a nota (-1 encerra): "))
        if nota < 0:
            break
        else:
            soma += nota
            x += 1
    print(f"A média das notas informadas é {media(soma, x):.2f}")


notas()


# Exercício 3 - Encontre o maior elemento de uma lista
# Escreva uma função que encontre e retorne o maior elemento em uma lista de números

def maior(lista):
    return max(lista)

def numeros():
    numeros = []
    while True:
        numero = input("Digite um número: ").upper()
        if not numero.isdigit():
            break
        else:
            numeros.append(int(numero))

    print(maior(numeros))


numeros()




