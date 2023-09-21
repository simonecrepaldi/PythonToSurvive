# Exercício: Analisando Texto
# Crie um programa que analise um arquivo de texto e forneça as seguintes informações:
# Contagem de palavras no texto.
# Contagem de frases no texto.
# Lista das palavras mais frequentes no texto.
# Média de palavras por frase.
# Você pode usar qualquer arquivo de texto como entrada para este programa.
# Certifique-se de realizar o pré-processamento necessário, como remover pontuações e letras maiúsculas, para garantir que as contagens sejam precisas.
# Dica: Você pode usar as bibliotecas re para trabalhar com expressões regulares e collections para ajudar na contagem das palavra

def le_arquivo(arquivo):
    with open(arquivo, "r") as file:
        conteudo = file.readlines()
        print(conteudo)
        # return conteudo

def inicio():
    conteudo = le_arquivo("jogo_wordle/wordle_palavras.py")

    # total_palavras = conta_palavras(conteudo)
    #
    # total_frases = conta_frases
    #
    # frequentes = palavras_frequentes(conteudo)
    #
    # media = media_palavras(conteudo)

    # print()


inicio()