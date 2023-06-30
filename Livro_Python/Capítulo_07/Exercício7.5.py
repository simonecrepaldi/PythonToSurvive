primeira = "AATTGGAA"
segunda = "TG"
terceira = ""
for letra in primeira:
    if letra in segunda:
        continue
    else:
        terceira += letra
print(terceira)
