primeira = "AATTCGAA"
segunda = "TG"
terceira = "AC"
quarta = ""
for letra in primeira:
    posicao = segunda.find(letra)
    if posicao != -1:
        quarta += terceira[posicao]
    else:
        quarta += letra
if quarta == "":
    print("Caracteres removidos.")
else:
    print(f"Resultado: {quarta}")
