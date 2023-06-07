número = input("Digite um número inteiro: ")
contrário = número[::-1]

if número == contrário:
    print(f"O número {número} é palíndromo!")
else:
    print(f"O número {número} não é palíndromo!")
