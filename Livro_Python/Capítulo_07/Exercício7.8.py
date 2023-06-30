palavras = ["macarrao", "cerveja", "feijoada", "manteiga", "vinho", "refrigerante",
            "salgadinho", "coxinha", "leite", "lasanha", "omelete", "sorvete",
            "pizza", "empada", "sanduiche", "lamen", "arroz", "bauru"]
numero = int(input("Informe um número inteiro: "))
indice = (numero * 776) % (len(palavras))
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
palavra = palavras[indice]
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 += " /   "
    elif erros >= 6:
        linha3 += " / \ "
    print(f"X{linha3}")
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
