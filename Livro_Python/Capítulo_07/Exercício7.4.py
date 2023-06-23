string = "TTAAC"
a = ""
for letra in string:
    if letra in a:
        continue
    else:
        print(f"{letra}: {string.count(letra)}x")
        a += letra
