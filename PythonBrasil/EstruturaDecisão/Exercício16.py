# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

delta = raiz1 = raiz2 = 0
while True:
    a = int(input("Digite o valor de a: "))
    if a == 0:
        break
    else:
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
    print(f"Equação digitada: {a}x2 + {b}x + {c}")
    delta = (b**2) - 4 * a * c
    raizdelta = delta**(1/2)
    if delta == 0:
        raiz1 = raiz2 = (-b / (2*a))
        print(f"A equação possui apenas uma raiz real: {raiz1}")
    elif delta > 0:
        raiz1 = (-b + raizdelta)/(2*a)
        raiz2 = (-b - raizdelta) / (2 * a)
        print(f"A equação possui duas raizes reais: {raiz1} e {raiz2}")
    else:
        print("A equação não possui raízes reais!")
    break