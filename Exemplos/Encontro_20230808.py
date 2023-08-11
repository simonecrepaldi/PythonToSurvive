# Encontro - 08/08/2023

# Exercício 1
# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit ou vice-versa. Para cada opção, crie uma função. 
# Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.
# Conversão entre Celsius e Farenheit

def CparaF(temperatura):
    tempF = (temperatura * 1.8) + 32
    return tempF

def FparaC(temperatura):
    tempC = (temperatura - 32) / 1.8
    return tempC

def menu ():
    opcao = input("Escolha qual conversão deseja fazer: C para F (digite A) ou F para C (digite B): ").upper()
    temperatura = float(input("Digite a temperatura inicial: "))

    if opcao == "A":
        print(f"A temperatura {temperatura} em Celsius equivale a {CparaF(temperatura)} em Farenheit.")
    elif opcao == "B":
        print(f"A temperatura {temperatura} em Farenheit equivale a {FparaC(temperatura)} em Celsius.")
    else:
        print("opção digitada é inválida!")


assert CparaF(0) == 32, "A conversão está incorreta"
assert FparaC(32) == 0, "A conversão está incorreta"
menu()



# Exercício 2
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos através de uma função.
# Seu script também deve fornecer a média dos três números, através de uma segunda função que chama a primeira.

def soma(num1, num2, num3):
    return num1 + num2 + num3


def media(num1, num2, num3):
    resultado = soma(num1, num2, num3)
    return resultado/3


def argumentos():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    resultadoSoma = soma(num1, num2, num3)
    resultadoMedia = media(num1, num2, num3)

    print(f"A soma dos números é {resultadoSoma} e a média é {resultadoMedia}")


argumentos()


# Outra forma de resolver:
def soma(S):
    return sum(S)

def media(M):
    return soma(M)/len(M)

def menu():
    argumentos = 3
    L = []

    for x in range(0, argumentos):
        L.append(int(input(f"Digite o argumento {x+1}: ")))

    print(soma(L))
    print(media(L))


menu()
