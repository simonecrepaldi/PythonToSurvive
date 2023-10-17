from palavras import lista
import random

cores = {'vermelho': '\033[31m', 'amarelo': '\033[33m', 'verde': '\033[32m', 'branco': '\033[7m', 'fecha': '\033[m'}
def desenho(tentativas):
    if tentativas <= 4:
        print(f"{cores['vermelho']} O ")
    if tentativas <= 3:
        print("\\", end="")
    if tentativas <= 2:
        print(" /")
    if tentativas <= 1:
        print("J", end="")
    if tentativas <= 0:
        print(" L")
    print(f"{cores['fecha']}")

def jogo():
    tentativas = 5
    erros = []
    palavra = lista[random.randint(0,len(lista)-1)].upper()
    resposta = list("_" * len(palavra))
    print(resposta)

    while tentativas > 0:
        letra = input("Digite uma letra: ").upper()
        if letra in palavra:
            for k,c in enumerate(palavra):
                if letra == c:
                    resposta[k] = c
        else:
            erros.append(letra)
            tentativas -= 1
        desenho(tentativas)


        print(f"{' '.join(resposta)}", end=" ")
        print()
        print(f"Letras utilizadas: {erros}")

        if "_" not in resposta:
            print("Você acertou!")
            break

    if tentativas == 0:
        print(f"Você perdeu! A palavra era {palavra}.")


jogo()