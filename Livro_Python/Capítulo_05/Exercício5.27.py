numero = input("Digite um número inteiro: ")
contrario = numero[::-1]

if numero == contrario:
    print(f"O número {numero} é palíndromo!")
else:
    print(f"O número {numero} não é palíndromo!")
