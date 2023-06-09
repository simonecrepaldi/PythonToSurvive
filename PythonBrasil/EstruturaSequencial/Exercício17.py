# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Área a ser pintada (em metros quadrados): "))
folga = 0.1
volume_tinta = (area / 6) * (1 + folga)


print("Situação 01 - Latas")
qtdade_lata = (volume_tinta // 18) + 1
custo_lata = qtdade_lata * 80
print(f"Quantidade de tinta necessária: {qtdade_lata:.0f} latas.")
print(f"Custo: R${custo_lata:.2f}")

print("Situação 02 - Galões")
qtdade_galao = (volume_tinta // 3.6) + 1
custo_galao = qtdade_galao * 25
print(f"Quantidade de tinta necessária: {qtdade_galao:.0f} galões.")
print(f"Custo: R${custo_galao:.2f}")

print("Situação 03 - Latas e Galões")
qtdade_lata = (volume_tinta // 18)
resto_tinta = (volume_tinta % 18)
qtdade_galao = (resto_tinta // 3.6) + 1
custo_total = (qtdade_lata * 80) + (qtdade_galao * 25)

print(f"Quantidade de tinta necessária: {qtdade_lata:.0f} lata(s) e {qtdade_galao:.0f} galão(ões).")
print(f"Custo: R${custo_total:.2f}")