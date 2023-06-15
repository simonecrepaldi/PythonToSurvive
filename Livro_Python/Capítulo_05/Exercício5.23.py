numero = int(input("Digite um número: "))

if numero == 2:
    print(f"{numero} É PRIMO!")
elif numero % 2 == 0:
    print(f"{numero} NÃO É PRIMO!")
else:
    x =3
    while (x < numero):
        if numero % x == 0:
            break
        x += 2
    if x == numero:
        print(f"{numero} É PRIMO!")
    else:
        print(f"{numero} NÃO É PRIMO!")
