# Exercício 4.2
v = int(input("Digite a velocidade do carro em km/h: "))
if v > 80:
    print("Você foi multado!")
    multa = (v-80)*5
    print(f"Valor da multa: R${multa:.2f}.")

    