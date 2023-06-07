frase = input("Digite uma frase: ")
dic = {}
for letra in frase:
    if letra in dic:
        dic[letra] = dic[letra] + 1
    else:
        dic[letra] = 1
print(dic)
