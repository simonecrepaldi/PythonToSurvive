string = "TTAAC"
a = ""
for letra in string:
    if letra in a:
        continue
    else:
        print(f"{letra}: {string.count(letra)}x")
        a += letra

# Outra forma de resolver usando "not in"
string = "TTAAC"
a = ""
for letra in string:
    if letra not in a:
        print(f"{letra}: {string.count(letra)}x")
        a += letra
