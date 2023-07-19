# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverso(num):
    string = str(num)
    contrario = string[::-1]
    return contrario


numero = int(input("Informe um número inteiro: "))
print(reverso(numero))
