primeira = "AABBEFAATT"
segunda = "BE"

if segunda in primeira:
    posicao = primeira.find(segunda)
    print(f"{segunda} encontrado na posição {posicao} de {primeira}.")
else:
    print(f"{segunda} não encontrada em {primeira}.")


