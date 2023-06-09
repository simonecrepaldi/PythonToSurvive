# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Área a ser pintada (em metros quadrados): "))
volume_tinta = area / 3
qtdade_lata = (volume_tinta // 18) + 1

custo_total = qtdade_lata * 80

print(volume_tinta)
print(f"Para pintar uma área de {area:.2f}m2 você precisará de {qtdade_lata:.0f} latas de tinta e gastará R${custo_total:.2f}")
