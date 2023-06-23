primeira = "AAACTBF"
segunda = "CBT"
lista = []
for letra in primeira:
    if letra in segunda:
        lista.append(letra)
terceira = "".join(lista)
print(terceira)


# Outra forma de resolver:
primeira = "AAACTBF"
segunda = "CBT"
terceira = ""
for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira += letra
if terceira == "":
    print("Não foram encontrados caracteres comuns.")
else:
    print(f"Caracteres em comum: {terceira}")
