# Programa 4.7 - Categoria x Preço, usando elif
categoria = int(input("Digite a categoria do produto: "))   #1
if categoria == 1:  #2
    preço = 10  #3
elif categoria == 2:   #4
    preço = 18  #5
elif categoria == 3:  #6
    preço = 23  #7
elif categoria == 4:  #8
    preço = 26  #9
elif categoria == 5:  #10
    preço = 31  #11
else:   #12
    print("Categoria inválida, digite um valor entre 1 e 5!")   #13
    preço = 0   #14
print(f"O preço do produto é: R${preço:.2f}")   #15
