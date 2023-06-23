primeira = "CTA"
segunda = "ABC"
terceira = ""
for letra in primeira:
    if letra not in segunda and letra not in terceira:
        terceira += letra
for letra in segunda:
    if letra not in primeira and letra not in terceira:
        terceira += letra
print(terceira)


# Outra forma de resolver com lista
primeira = "CTA"
segunda = "ABC"
lista = []
for letra in segunda:
    if letra not in primeira:
        lista.append(letra)
for letra in primeira:
    if letra not in segunda:
        lista.append(letra)
terceira = "".join(lista)
print(terceira)
