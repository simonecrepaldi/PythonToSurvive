# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def valor(n):
    if n > 0:
        return "P"
    else:
        return "N"


print(valor(12))
print(valor(-3))
print(valor(0))