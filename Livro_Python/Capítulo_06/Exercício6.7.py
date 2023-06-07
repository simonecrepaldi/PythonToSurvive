sequencia = input("Digite a sequencia de parênteses: ")
pilha = []
x = 0
while x < len(sequencia):
    if sequencia[x] == "(":
        pilha.append(sequencia[x])
    if sequencia[x] == ")":
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            pilha.append(sequencia[x])
            break
    x += 1

if len(pilha) == 0:
    print("Ok!")
else:
    print("Erro!")
