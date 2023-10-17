# Exercício: Analisando Texto
# Crie um programa que analise um arquivo de texto e forneça as seguintes informações:
# Contagem de palavras no texto.
# Contagem de frases no texto.
# Lista das palavras mais frequentes no texto.
# Média de palavras por frase.
# Você pode usar qualquer arquivo de texto como entrada para este programa.
# Certifique-se de realizar o pré-processamento necessário, como remover pontuações e letras maiúsculas, para garantir que as contagens sejam precisas.
# Dica: Você pode usar as bibliotecas re para trabalhar com expressões regulares e collections para ajudar na contagem das palavra

from re import split
from collections import Counter

def le_arquivo(arquivo):
    with open(arquivo, "r", encoding="utf8") as file:
        conteudo = file.read()
        # print(conteudo)
        return conteudo

def conta_palavras(conteudo):
    total = conteudo.split()
    return len(total)

def conta_frases(conteudo):
    total = split("[.:;!?]", conteudo)
    total = list(filter(lambda x: len(x) > 0, total))
    return len(total)

def palavras_frequentes(conteudo):
    total = conteudo.split()
    tot = Counter(total)
    return tot.most_common(1)[0]

def media_palavras(conteudo):
    return conta_palavras(conteudo)/conta_frases(conteudo)

def inicio():
    texto = le_arquivo("frases.txt")

    total_palavras = conta_palavras(texto)
    total_frases = conta_frases(texto)
    frequentes = palavras_frequentes(texto)
    media = media_palavras(texto)

    print(f"Total de palavras: {total_palavras}")
    print(f"Total de frases: {total_frases}")
    print(f"Palavra mais frequente no texto: '{frequentes[0]}' com {frequentes[1]} vez(es)")
    print(f"Média de palavras por frase: {media:.2f}")


inicio()