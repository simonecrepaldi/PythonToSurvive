# Programa 4.6 - Categoria x Preço
categoria = int(input("Digite a categoria do produto: "))                       #1
if categoria == 1:                                                              #2
    preco = 10                                                                  #3
else:                                                                           #4
    if categoria == 2:                                                          #5
        preco = 18                                                              #6
    else:                                                                       #7
        if categoria == 3:                                                      #8
            preco = 23                                                          #9
        else:                                                                   #10
            if categoria == 4:                                                  #11
                preco = 26                                                      #12
            else:                                                               #13
                if categoria == 5:                                              #14
                    preco = 31                                                  #15
                else:                                                           #16
                    print("Categoria inválida, digite um valor entre 1 e 5!")   #17
                    preco = 0                                                   #18
print(f"O preço do produto é: R${preco:.2f}")                                   #19
