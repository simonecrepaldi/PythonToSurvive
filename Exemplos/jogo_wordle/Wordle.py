from wordle_palavras import lista
import random

cores = {'vermelho': '\033[31m', 'amarelo': '\033[33m', 'verde': '\033[32m', 'branco': '\033[7m', 'fecha': '\033[m'}


def game_instruction():
    print("""Wordle is a single player game
A player has to guess a five letter hidden word
You have six attempts
Your Progress Guide "✔❌❌✔➕"
"✔" Indicates that the letter at that position was guessed correctly
"➕" indicates that the letter at that position is in the hidden word, but in a different position
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word""")


def check_word():
    pos = random.randint(0, len(lista) - 1)
    hidden_word = lista[pos].upper()
    attempt = 6
    while attempt >= 0:
        while True:
            guess = str(input("[?] Palpite: ")).upper()
            if len(guess) == 5 and guess.isalpha():
                break
            else:
                print("A palavra deve ter 5 letras. LETRAS.")
        if guess == hidden_word:
            print(f"{cores['amarelo']}A{cores['verde']}C{cores['vermelho']}E{cores['amarelo']}R{cores['vermelho']}T{cores['verde']}O{cores['vermelho']}U{cores['amarelo']}!{cores['fecha']}")
            break
        if attempt == 0:
            print(f"Fim de jogo. A palavra era {hidden_word}.")
            break
        else:
            print(f"[{attempt}] ", end="")
            attempt = attempt - 1
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    print(f"{cores['verde']}{word.upper()}{cores['fecha']}", end="")
                elif word in hidden_word:
                    print(f"{cores['amarelo']}{word.upper()}{cores['fecha']}", end="")
                else:
                    print(f"{cores['vermelho']}{word.upper()}{cores['fecha']}", end="")
            print("")


game_instruction()
check_word()
