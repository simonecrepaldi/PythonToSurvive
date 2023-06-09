# # Ex. 16
# area = float(input("Digite a área a ser pintada: "))
# rendimento_tinta = 3
# volume_lata = 18
# preco_lata = 80
# volume_tinta = area / rendimento_tinta
# qtde_latas = (volume_tinta // volume_lata) + 1
# preco_total = qtde_latas * preco_lata
# print(f"O total de latas é de {qtde_latas:.0f} e o preço total é de R$ {preco_total:.2f}")
#

# Ex. 17
area = float(input("Digite a área a ser pintada: "))
rendimento_tinta = 6
volume_lata = 18
preco_lata = 80
volume_galao = 3.6
preco_galao = 25
margem = 0.1

volume_tinta = (area / rendimento_tinta) * (1 + margem)

# Sit 1 - Qtde latas
qtde_latas = (volume_tinta // volume_lata) + 1
preco_total_latas = qtde_latas * preco_lata

# Sit 2 - Qtde galoes
qtde_galoes = (volume_tinta // volume_galao) + 1
preco_total_galoes = qtde_galoes * preco_galao

# Sit 3 - Misturado
volume_tinta_arredondado = volume_tinta
total_latas_aprov = volume_tinta_arredondado // volume_lata
resto_latas_aprov = volume_tinta_arredondado % volume_lata
total_galoes_aprov = (resto_latas_aprov // volume_galao) + 1

print(f"O total de latas é de {qtde_latas:.0f} e o preço total é de R$ {preco_total_latas:.2f}")
print(f"O total de galões é de {qtde_galoes:.0f} e o preço total é de R$ {preco_total_galoes:.2f}")
print(f"O total com aproveitamento é de {total_latas_aprov:.0f} latas mais {total_galoes_aprov:.0f} galões"
      f" e o preço total é de R$ {total_latas_aprov * preco_lata + total_galoes_aprov * preco_galao:.2f}")
