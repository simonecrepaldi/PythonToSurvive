# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de  b: "))
c = float(input("Digite o valor de c: "))

tipo = 0

if (a + b) > c and (b + c) > a and (a + c) > b:
    if a == b == c:
        tipo = "equilátero"
    elif (a == b) or (a == c) or (b == c):
        tipo = "isósceles"
    else:
        tipo = "escaleno"
    print(f"Os três valores podem formar um triângulo {tipo}!")
else:
    print("Não é possível formar um triângulo com os três valores.")