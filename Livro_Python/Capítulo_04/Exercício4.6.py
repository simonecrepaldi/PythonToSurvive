# Exercício 4.6
x = int(input("Distância a ser percorrida em km: "))
if x <= 200:
    preço = x * 0.50
else:
    preço = x * 0.45
print(f"A viagem de {x}km custará R${preço:.2f}.")