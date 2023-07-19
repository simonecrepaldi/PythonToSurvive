# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def digitosNumero(x):
    numero = str(x)
    return len(numero)


a = int(input("Informe um número inteiro: "))
print(f"O número {a} possui {digitosNumero(a)} digítos.")



# Outra forma de resolver sem converter o int para string
def qtde_digitos(num):
    teste = 1
    casas = 0

    if num !=0:
        while teste <= num:
            teste *= 10
            casas += 1
        return casas
    else:
        return 1


numero = int(input("Digite o número inteiro: "))
print(qtde_digitos(numero))
