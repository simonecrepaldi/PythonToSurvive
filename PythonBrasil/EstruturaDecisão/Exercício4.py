# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

while True:
    letra = input("Digite uma letra: ").upper()
    if letra.isalpha():
        if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            print(f"A letra {letra} é uma VOGAL!")
        else:
            print(f"A letra {letra} é uma CONSOANTE!")
        break
