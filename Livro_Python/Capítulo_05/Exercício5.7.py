n = int(input("Digite um número: "))
inicio = int(input("Início da tabuada: "))
fim = int(input("Fim da tabuada: "))

while inicio <= fim:
    print(f"{n} x {inicio:2} = {n * inicio:2}")
    inicio += 1
