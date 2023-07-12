# Exercícios - Funções

# Exercício 1
# Faça um programa para imprimir, para um n informado pelo usuário:
# 1
# 2 2
# 3 3 3
# .....
# n n n n n n...n
# Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def impressao(n):
    y = 1
    while y <= n:
        x = 1
        while x <= y:
            print(y, end=" ")
            x += 1
        print("")
        y += 1



impressao(5)



# Exercício 2
# Faça um programa para imprimir, para um n informado pelo usuário:
# 1
# 1 2
# 1 2 3
# .....
# 1 2 3 n n n...n
# para um n informado pelo usuário.
# Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
def linhas(n):
    y = 1
    while y <= n:
        x = 1
        while x <= y:
            print(x, end=" ")
            x += 1
        print("")
        y += 1


linhas(5)



# Exercício 3
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma(a, b, c):
    resultado = a + b + c
    return resultado


print(soma(154, 32, 3))



# Exercício 4
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



# Exercício 5
# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImposto, custo):
    valorFinal = custo * (1 +(taxaImposto/100))
    return valorFinal


print(f"Valor Final: R$ {somaImposto(10, 1000):.2f}")



# Exercício 6
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
def conversaoHora(hora, minuto):
    if hora >= 12:
        AMPM = "P.M."
        if hora > 12:
            hora -= 12
    else:
        AMPM = "A.M."
    return impressao(hora, minuto, AMPM)

def impressao(hora, minuto, AMPM):
    print(f"{hora}:{minuto} {AMPM}")


conversaoHora(12, 30)
conversaoHora(18, 30)
conversaoHora(3, 30)

