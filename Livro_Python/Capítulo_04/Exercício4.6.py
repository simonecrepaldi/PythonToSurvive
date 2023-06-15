# Exercício 4.6
x = int(input("Distância a ser percorrida em km: "))
if x <= 200:
    preco = x * 0.50
else:
    preco = x * 0.45
print(f"A viagem de {x}km custará R${preco:.2f}.")
